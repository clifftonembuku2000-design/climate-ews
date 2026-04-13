import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# AUTO REFRESH
from streamlit_autorefresh import st_autorefresh

# DATA LAYER
from data_loader import get_chirps_rainfall, get_temperature, get_soil_moisture
from climate_database import generate_national_table, PROVINCES, get_district_data

from indices import compute_spi
from ml_model import predict_drought_risk
from forecast import predict_future_drought
from maps import generate_drought_map
from alerts import send_alert
from gee_ndvi import get_ndvi_gee
from pest_disease_engine import get_pest_disease_risk


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Operational Climate EWS", layout="wide")

st.title("🌍 Operational Climate Early Warning System (Mozambique)")
st.success(f"System Active: {datetime.now()}")

# AUTO REFRESH EVERY 10 MIN
st_autorefresh(interval=600000, key="datarefresh")


# =========================
# 📡 DATA SOURCES
# =========================
st.info("""
📡 **Data Sources**
- 🌧 Rainfall: CHIRPS / ERA5
- 🌡 Temperature: ERA5 Reanalysis
- 🌱 NDVI: MODIS / Sentinel (simulated)
- 💧 Soil Moisture: Model-based estimation
- 🛰 Forecast: Statistical + ML model
""")


# =========================
# INPUTS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    province = st.selectbox("Province", PROVINCES)

with col2:
    district = st.text_input("Enter District (any district in selected province)")

with col3:
    crop = st.text_input("Enter Crop (any crop in Mozambique)")


# =========================
# DATA LAYER
# =========================

rain = get_chirps_rainfall(province)
temp = get_temperature(province)
ndvi = get_ndvi_gee(province)
soil = get_soil_moisture(province)

# REAL DISTRICT DATA
district_data = get_district_data(province, district)

soil_moisture = float(soil[-1])


# =========================
# INDICATORS
# =========================

spi = compute_spi(rain)

ndvi_avg = float(sum(ndvi) / len(ndvi)) if hasattr(ndvi, "__len__") else float(ndvi)
temp_last = float(temp[-1]) if hasattr(temp, "__len__") else float(temp)

risk = predict_drought_risk(spi, ndvi, temp_last)


# =========================
# DASHBOARD OUTPUT
# =========================

st.subheader("📊 Climate Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric("SPI", round(float(spi), 2))
c2.metric("Risk (%)", round(float(risk), 2))
c3.metric("NDVI", round(ndvi_avg, 2))
c4.metric("Soil Moisture", round(float(soil_moisture), 2))


# =========================
# 📍 DISTRICT INTELLIGENCE (CORRECT LOCATION ✅)
# =========================

st.subheader("📍 District Climate Data")

if district_data:
    st.write(district_data)
else:
    st.warning("Please enter a district to view data.")


# =========================
# 🐛 PEST & DISEASE
# =========================

pest, disease = get_pest_disease_risk(
    crop,
    province,
    district,
    ndvi_avg,
    temp_last,
    rain[-1] if hasattr(rain, "__len__") else rain
)

st.subheader("🐛 Pest & Disease Status")

p1, p2 = st.columns(2)

p1.metric("Pest Risk", pest)
p2.metric("Disease Risk", disease)


# =========================
# FORECAST
# =========================

future = predict_future_drought(rain, ndvi, temp)

st.subheader("🔮 Forecast Risk")
st.write(future)


# =========================
# NATIONAL DASHBOARD
# =========================

st.subheader("📊 National Climate Dashboard")

df = generate_national_table()

if "District" in df.columns:
    df = df.drop(columns=["District"])

st.dataframe(df)


# =========================
# MAP
# =========================

st.subheader("🗺 Mozambique Drought Map")

map_object = generate_drought_map()
map_object.save("map.html")

with open("map.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=500)


# =========================
# ALERT
# =========================

st.subheader("🚨 Alert System")
st.write(send_alert(province, risk))