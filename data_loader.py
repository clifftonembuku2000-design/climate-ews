import numpy as np
import os

# =========================
# CONFIG (SAFE MODE)
# =========================

CDS_ENABLED = False  # 👈 keep FALSE until ERA5 fully stable

AREA = [-10, 30, -27, 41]  # Mozambique bounding box


# =========================
# 🌧 RAINFALL (SAFE MODE)
# =========================

def get_chirps_rainfall(province):
    """
    SAFE MODE: synthetic rainfall time series
    Replace later with ERA5 / CHIRPS API
    """
    np.random.seed(hash(province) % 1000)
    rain = np.random.uniform(20, 120, 12)
    return rain


# =========================
# 🌡 TEMPERATURE (SAFE MODE)
# =========================

def get_temperature(province):
    """
    SAFE MODE: synthetic temperature series
    """
    np.random.seed(hash(province) % 2000)
    temp = np.random.uniform(22, 38, 12)
    return temp


# =========================
# 💧 SOIL MOISTURE (NEW - SAFE ERA5 STRUCTURE)
# =========================

def get_soil_moisture(province):
    """
    SAFE VERSION (STRUCTURED LIKE ERA5)
    Later connect to real ERA5 soil moisture dataset
    """

    np.random.seed(hash(province) % 3000)

    # realistic soil moisture range (m³/m³)
    soil = np.random.uniform(0.1, 0.5, 12)

    return soil


# =========================
# OPTIONAL CDS FUNCTION (DISABLED FOR NOW)
# =========================

def download_era5(variable):
    """
    CDS is DISABLED to prevent crash.
    Activate later when .cdsapirc is stable.
    """
    raise Exception("CDS disabled. Enable after full configuration.")


def extract(file, var):
    """
    Placeholder for ERA5 extraction (future upgrade)
    """
    pass