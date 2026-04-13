def get_pest_disease_risk(crop, province, district, ndvi, temp, rain):

    crop = crop.lower() if crop else ""

    pest = "Low"
    disease = "Low"

    # =========================
    # MAIZE
    # =========================
    if "maize" in crop:
        if temp > 28 and ndvi < 0.4:
            pest = "High Fall Armyworm Risk"
        if rain > 20:
            disease = "Moderate Leaf Blight Risk"

    # =========================
    # RICE
    # =========================
    elif "rice" in crop:
        if rain > 30:
            disease = "High Rice Blast Risk"
        if temp > 30:
            pest = "Brown Planthopper Risk"

    # =========================
    # CASSAVA
    # =========================
    elif "cassava" in crop:
        if ndvi < 0.3:
            disease = "Cassava Mosaic Virus Risk"
        pest = "Whitefly Risk"

    # =========================
    # GENERAL (ALL CROPS)
    # =========================
    if ndvi < 0.3:
        pest = "General Pest Stress Risk"

    return pest, disease