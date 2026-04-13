import numpy as np

# =========================
# FAO WEIGHTED DROUGHT INDEX
# =========================
def compute_fao_drought_index(spi, ndvi, temp):

    # -------------------------
    # 1. Normalize SPI
    # -------------------------
    spi_norm = 1 - (spi + 3) / 6
    spi_norm = np.clip(spi_norm, 0, 1)

    # -------------------------
    # 2. Normalize NDVI (healthy = low risk)
    # -------------------------
    ndvi_norm = 1 - ndvi
    ndvi_norm = np.clip(ndvi_norm, 0, 1)

    # -------------------------
    # 3. Normalize temperature (assume 10–45°C range)
    # -------------------------
    temp_norm = (temp - 10) / 35
    temp_norm = np.clip(temp_norm, 0, 1)

    # -------------------------
    # 4. FAO weighted index
    # -------------------------
    risk = (
        0.40 * spi_norm +
        0.35 * ndvi_norm +
        0.25 * temp_norm
    ) * 100

    return risk