import numpy as np

# =========================
# SPI (Standardized Precipitation Index)
# =========================
def compute_spi(rain_series):
    rain_series = np.array(rain_series)

    mean = np.mean(rain_series)
    std = np.std(rain_series)

    # Prevent division by zero (VERY IMPORTANT for real systems)
    if std == 0:
        return 0

    spi = (rain_series[-1] - mean) / std

    return spi


# =========================
# NDVI ANOMALY (Basic version if already used elsewhere)
# =========================
def compute_ndvi_anomaly(ndvi_series):
    ndvi_series = np.array(ndvi_series)

    mean = np.mean(ndvi_series)
    if mean == 0:
        return 0

    anomaly = ndvi_series[-1] - mean
    return anomaly


# =========================
# FAO-STYLE WEIGHTED DROUGHT INDEX (UPGRADED MODEL)
# =========================
def compute_fao_drought_index(spi, ndvi, temp):
    """
    FAO-style weighted drought index:
    40% rainfall (SPI)
    35% NDVI
    25% temperature
    """

    # -------------------------
    # Normalize SPI (drought sensitivity)
    # -------------------------
    spi_score = max(0, min(100, (1 - abs(spi)) * 100))

    # -------------------------
    # NDVI stress (convert to dryness indicator)
    # NDVI is usually 0–1 or anomaly
    # -------------------------
    ndvi_score = max(0, min(100, (1 - ndvi) * 100))

    # -------------------------
    # Temperature stress (assume max ~40°C)
    # -------------------------
    temp_score = max(0, min(100, (temp / 40) * 100))

    # -------------------------
    # Weighted FAO drought index
    # -------------------------
    drought_index = (
        0.40 * spi_score +
        0.35 * ndvi_score +
        0.25 * temp_score
    )

    return drought_index