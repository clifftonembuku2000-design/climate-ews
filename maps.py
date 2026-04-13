import folium
import pandas as pd

def generate_drought_map():

    # Mozambique provinces (simple model for now)
    data = {
        "Province": [
            "Maputo", "Gaza", "Inhambane", "Sofala",
            "Manica", "Tete", "Zambezia",
            "Nampula", "Niassa", "Cabo Delgado"
        ],
        "Risk": [12, 35, 28, 55, 60, 70, 45, 50, 30, 65]
    }

    df = pd.DataFrame(data)

    # Create base map centered on Mozambique
    m = folium.Map(location=[-18.5, 35.0], zoom_start=5)

    # Color function
    def color(risk):
        if risk > 70:
            return "red"
        elif risk > 50:
            return "orange"
        elif risk > 30:
            return "yellow"
        else:
            return "green"

    # Add markers
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[-18.0, 35.0],  # simplified center (we upgrade later with real boundaries)
            radius=10,
            popup=f"{row['Province']}: {row['Risk']}%",
            color=color(row["Risk"]),
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

    return m