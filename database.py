import sqlite3

conn = sqlite3.connect("climate_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS climate_records (
    province TEXT,
    crop TEXT,
    spi REAL,
    ndvi REAL,
    temp REAL,
    risk REAL
)
""")

def save_record(province, crop, spi, ndvi, temp, risk):
    cursor.execute("""
        INSERT INTO climate_records VALUES (?, ?, ?, ?, ?, ?)
    """, (province, crop, spi, ndvi, temp, risk))

    conn.commit()