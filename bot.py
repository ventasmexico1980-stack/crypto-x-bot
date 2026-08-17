import os
from datetime import datetime

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def crear_grafico():
    # Datos de ejemplo.
    # Más adelante los reemplazaremos por datos reales del mercado.
    horas = ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00"]
    precio = [118000, 118500, 117900, 119200, 120100, 121000]

    plt.figure(figsize=(12, 6))
    plt.plot(horas, precio, marker="o", linewidth=3)

    plt.title("BITCOIN MARKET UPDATE", fontsize=20, fontweight="bold")
    plt.xlabel("Time")
    plt.ylabel("BTC Price (USD)")
    plt.grid(True, alpha=0.25)

    plt.tight_layout()

    os.makedirs("images", exist_ok=True)

    archivo = "images/btc_market_update.png"
    plt.savefig(archivo, dpi=160, bbox_inches="tight")
    plt.close()

    return archivo


def crear_publicacion():
    fecha = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    texto = f"""🚨 BITCOIN MARKET UPDATE

📊 BTC is showing strong market activity.

💰 Price: $121,000
📈 Market momentum: Positive
🌎 Crypto market: Active

Updated: {fecha}

Track crypto markets with Velocoin.ai

#Bitcoin #BTC #Crypto #Trading #Velocoin
"""

    with open("post.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    return texto


if __name__ == "__main__":
    imagen = crear_grafico()
    publicacion = crear_publicacion()

    print("✅ Gráfico creado:", imagen)
    print("✅ Publicación creada:")
    print(publicacion)
