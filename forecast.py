import numpy as np

# =========================
# SAFE UTILITY FUNCTIONS
# =========================

def safe_array(x):
    """
    Ensures input is always a numpy array
    Handles: list, float, int, None
    """
    if x is None:
        return np.array([0])

    if isinstance(x, (int, float)):
        return np.array([x])

    try:
        return np.array(x)
    except:
        return np.array([0])


def safe_mean(x):
    """
    Safe mean for both scalars and arrays
    """
    x = safe_array(x)

    if len(x) == 0:
        return 0

    return float(np.mean(x))


def safe_last(x):
    """
    Safe last value extraction
    """
    x = safe_array(x)

    if len(x) == 0:
        return 0

    return float(x[-1])


# =========================
# FORECAST MODEL (IMPROVED)
# =========================

def predict_future_drought(rain, ndvi, temp):
    """
    FAO-style drought forecasting model (robust version)

    Handles:
    - single values
    - lists
    - numpy arrays
    - None values
    """

    # Convert all inputs safely
    rain = safe_array(rain)
    ndvi = safe_array(ndvi)
    temp = safe_array(temp)

    # =========================
    # TIME WINDOW (last 6 periods)
    # =========================
    rain_window = rain[-6:] if len(rain) > 6 else rain
    ndvi_window = ndvi[-6:] if len(ndvi) > 6 else ndvi
    temp_window = temp[-6:] if len(temp) > 6 else temp

    rain_mean = safe_mean(rain_window)
    ndvi_mean = safe_mean(ndvi_window)
    temp_mean = safe_mean(temp_window)

    # =========================
    # DROUGHT RISK MODEL
    # =========================
    # Physical logic:
    # - less rain → higher risk
    # - low NDVI → higher risk
    # - high temperature → higher risk

    trend = (
        (-0.35 * rain_mean) +
        (-45.0 * ndvi_mean) +
        (2.2 * temp_mean)
    )

    # =========================
    # NORMALIZATION (0–100)
    # =========================
    risk = 1 / (1 + np.exp(-trend / 18)) * 100

    return round(float(max(0, min(100, risk))), 2)