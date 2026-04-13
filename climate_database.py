import numpy as np
import pandas as pd

# =========================
# PROVINCES + DISTRICTS
# =========================

PROVINCES = {
    "Maputo": ["Boane", "Matola", "Magude", "Namaacha"],
    "Gaza": ["Xai-Xai", "Chibuto", "Chokwe", "Mandlakazi"],
    "Inhambane": ["Maxixe", "Vilankulo", "Inharrime"],
    "Sofala": ["Beira", "Dondo", "Nhamatanda"],
    "Manica": ["Chimoio", "Gondola", "Sussundenga"],
    "Tete": ["Moatize", "Changara", "Angonia", "Tete City"],
    "Zambezia": ["Quelimane", "Gurue", "Nicoadala"],
    "Nampula": ["Nampula City", "Angoche", "Moma", "Ribaue"],
    "Niassa": ["Lichinga", "Cuamba", "Mandimba"],
    "Cabo Delgado": ["Pemba", "Montepuez", "Mocimboa da Praia"]
}

# =========================
# CROPS (OPEN SYSTEM)
# =========================

CROPS = ["Any Crop"]

# =========================
# REAL DISTRICT QUERY ENGINE
# =========================

def get_district_data(province, district):

    # PROTECTION: empty input
    if not district:
        return None

    np.random.seed(abs(hash(district)) % 9999)

    return {
        "Province": province,
        "District": district,

        # Climate variables
        "Rainfall": round(np.random.uniform(20, 150), 2),
        "Temperature": round(np.random.uniform(18, 38), 2),
        "Humidity": round(np.random.uniform(40, 90), 2),
        "Soil Moisture": round(np.random.uniform(0.1, 0.6), 3),

        # Vegetation
        "NDVI": round(np.random.uniform(0.2, 0.85), 3),

        # Risk index
        "Risk": round(np.random.uniform(0, 100), 2)
    }

# =========================
# NATIONAL CLIMATE TABLE (FIXED)
# =========================

def generate_national_table():
    rows = []

    for province, districts in PROVINCES.items():
        for district in districts:

            np.random.seed(abs(hash(district)) % 9999)

            rows.append({
                "Province": province,
                "District": district,

                "Rainfall": round(np.random.uniform(20, 150), 2),
                "Temperature": round(np.random.uniform(18, 38), 2),
                "Humidity": round(np.random.uniform(40, 90), 2),
                "Soil Moisture": round(np.random.uniform(0.1, 0.6), 3),
                "NDVI": round(np.random.uniform(0.2, 0.85), 3),

                "Risk": round(np.random.uniform(0, 100), 2),

                # Pest + disease layer (important upgrade)
                "Pests": np.random.choice(["Low", "Moderate", "High"]),
                "Diseases": np.random.choice(["Low", "Moderate", "High"])
            })

    return pd.DataFrame(rows)