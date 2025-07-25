import joblib
import pandas as pd
from datetime import datetime

# 🤖 Chargement du modèle IA
model = joblib.load("kgf_model.pkl")

# 📈 Fonction pour extraire les indicateurs d’un signal brut
def extract_indicators(signal_data):
    indicators = {
        "rsi": signal_data["rsi"],
        "macdh": signal_data["macdh"],
        "ema_trend": signal_data["ema"],
        "atr": signal_data["atr"],
        "adx": signal_data["adx"],
        "price": signal_data["price"]
    }
    return pd.DataFrame([indicators])

# 🔮 Fonction IA pour prédire CALL ou PUT
def predict_direction(signal_data):
    features = extract_indicators(signal_data)
    prediction = model.predict(features)[0]
    return "CALL" if prediction == 1 else "PUT"

# ✅ Exemple de signal à traiter par ton bot
incoming_signal = {
    "rsi": 53.4,
    "macdh": 0.18,
    "ema": 102.6,
    "atr": 1.05,
    "adx": 26.1,
    "price": 105.2
}

# 🔮 Prédiction IA
decision = predict_direction(incoming_signal)
timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
print(f"[{timestamp} UTC] Signal IA détecté 👉 {decision}")
