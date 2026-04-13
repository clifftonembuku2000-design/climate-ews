import numpy as np

# =========================
# SAFE MODE NDVI (NO CRASH)
# =========================

def get_ndvi_gee(province):
    """
    NDVI TIME SERIES (SAFE + FORECAST COMPATIBLE)

    NOTE:
    - Currently uses synthetic NDVI
    - Structured for future upgrade to Google Earth Engine
    """

    # Ensure reproducibility per province
    np.random.seed(hash(province) % 999)

    # Generate realistic NDVI values (Mozambique vegetation range)
    ndvi = np.random.uniform(0.2, 0.85, 12)

    return ndvi