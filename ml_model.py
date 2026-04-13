import numpy as np

# =========================
# SAFE DROUGHT ML MODEL
# =========================

def predict_drought_risk(spi, ndvi, temp):
    """
    Stable ML-style drought risk model

    Fixes:
    - numpy array ambiguity error
    - ensures scalar output
    - supports both float and array inputs
    """

    # =========================
    # FORCE SAFE SCALARS
    # =========================
    spi = float(np.mean(spi)) if isinstance(spi, (list, np.ndarray)) else float(spi)
    ndvi = float(np.mean(ndvi)) if isinstance(ndvi, (list, np.ndarray)) else float(ndvi)
    temp = float(temp)

    # =========================
    # NORMALIZED SCORING
    # =========================

    spi_score = max(0, min(100, (1 - abs(spi)) * 100))
    ndvi_score = max(0, min(100, (1 - ndvi) * 100))
    temp_score = max(0, min(100, temp / 40 * 100))

    # =========================
    # FINAL WEIGHTED RISK MODEL
    # =========================
    risk = (
        0.40 * spi_score +
        0.35 * ndvi_score +
        0.25 * temp_score
    )

    # =========================
    # RETURN SAFE SCALAR
    # =========================
    return float(max(0, min(100, risk)))