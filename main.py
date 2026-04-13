import africastalking
import pandas as pd

# =========================
# 1. INITIALIZE SMS SYSTEM
# =========================
username = "sandbox"
api_key = "atsk_c2804fcbef245c4b61e0c1364ba1b83bf20bde75f05d6245332b271c3aa5ceefdff79875"

africastalking.initialize(username, api_key)
sms = africastalking.SMS

# =========================
# 2. CLIMATE DATA (PHASE 1)
# =========================
rainfall = 35          # mm
soil_moisture = 28     # %
temperature = 31       # °C
humidity = 82          # %

# =========================
# 3. DROUGHT MODEL
# =========================
def drought_risk(rainfall, soil_moisture, temperature):
    if rainfall < 40 and soil_moisture < 30 and temperature > 30:
        return "⚠️ HIGH DROUGHT RISK"
    elif rainfall < 70:
        return "🟡 MODERATE DROUGHT RISK"
    else:
        return "🟢 LOW DROUGHT RISK"

# =========================
# 4. PEST MODEL
# =========================
def pest_risk(temperature, humidity):
    if temperature > 28 and humidity > 80:
        return "⚠️ HIGH PEST RISK (Armyworm)"
    elif temperature > 25:
        return "🟡 MODERATE PEST RISK"
    else:
        return "🟢 LOW PEST RISK"

# =========================
# 5. RUN MODELS
# =========================
drought_status = drought_risk(rainfall, soil_moisture, temperature)
pest_status = pest_risk(temperature, humidity)

# =========================
# 6. CREATE ALERT MESSAGE
# =========================
message = f"""
CLIMATE ALERT:

Drought: {drought_status}
Pest: {pest_status}

Action:
- Mulch soil immediately
- Monitor crops daily
- Use drought-resistant crops
"""

# =========================
# 7. LOAD FARMERS
# =========================
farmers = pd.read_csv("farmers.csv")
numbers = farmers["phone"].tolist()

# =========================
# 8. SEND SMS
# =========================
response = sms.send(message, numbers)

print("SMS sent:", response)