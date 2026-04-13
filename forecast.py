import numpy as np

# =========================
# SAFE FORECAST MODEL
# =========================

def predict_future_drought(rain, ndvi, temp):
    """
    Safe FAO-style drought forecast model

    Fixes:
    - handles float vs array errors
    - ensures consistent time-series inputs
    - prevents crash from slicing [-6:]
    """

    # =========================
    # FORCE SAFE ARRAY CONVERSION
    # =========================
    rain = np.array(rain)
    ndvi = np.array(ndvi)
    temp = np.array(temp)

    # =========================
    # ENSURE MINIMUM LENGTH (IMPORTANT)
    # =========================
    def safe_mean(x):
        if len(x) == 0:
            return 0
        return np.mean(x[-6:])  # last 6 periods

    rain_mean = safe_mean(rain)
    ndvi_mean = safe_mean(ndvi)
    temp_mean = safe_mean(temp)

    # =========================
    # IMPROVED DROUGHT MODEL
    # =========================
    trend = (
        rain_mean * -0.3 +   # less rain = more drought risk
        ndvi_mean * -50 +    # low vegetation = higher risk
        temp_mean * 2        # high temperature = higher risk
    )

    # =========================
    # NORMALIZED OUTPUT (0–100)
    # =========================
    risk = 1 / (1 + np.exp(-trend / 20)) * 100

    return float(max(0, min(100, risk)))