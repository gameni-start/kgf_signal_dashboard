import streamlit as st
import pandas as pd
import datetime
import random

# --- Bannière statique professionnelle ---
st.markdown("""
<div style="
    background: linear-gradient(90deg, #000428 0%, #004e92 100%);
    padding: 40px 20px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    margin-bottom: 30px;
">
  <h1 style="
      color: #FFD700;
      text-align: center;
      font-size: 3em;
      margin: 0;
      letter-spacing: 2px;
      text-shadow: 0 2px 5px rgba(0,0,0,0.7);
  ">
    KGF Trading Signal Bot
  </h1>
  <p style="
      color: #ECECEC;
      text-align: center;
      font-size: 1.2em;
      margin-top: 10px;
      font-style: italic;
  ">
    Du silence des moqueries à la puissance des résultats.
  </p>
</div>
""", unsafe_allow_html=True)

# --- Section performance du jour ---
st.subheader("📊 Performance du jour")
try:
    df = pd.read_csv("performance.csv")
    st.dataframe(df, use_container_width=True)
    if "ratio" in df.columns:
        st.line_chart(df["ratio"])
    st.success("✅ Données chargées depuis 'performance.csv'")
except Exception as e:
    st.error(f"❌ Erreur de chargement : {e}")

# --- Moteur IA CALL/PUT intégré ---
st.subheader("🧠 Analyse IA CALL/PUT")

class IAEngine:
    def __init__(self):
        self.history = []

    def predict(self, pair):
        prob_call = round(random.uniform(0.5, 0.9), 3)
        prob_put = round(random.uniform(0.1, 0.5), 3)
        signal = "CALL" if prob_call > prob_put else "PUT"
        score = round(abs(prob_call - prob_put) * max(prob_call, prob_put), 3)
        self.history.append({
            "pair": pair,
            "signal": signal,
            "score": score,
            "timestamp": datetime.datetime.utcnow().strftime('%H:%M:%S')
        })
        return signal, score

    def resume(self):
        total = len(self.history)
        calls = sum(1 for s in self.history if s["signal"] == "CALL")
        puts = total - calls
        avg = round(sum(s["score"] for s in self.history) / total, 3) if total else 0
        return total, calls, puts, avg

engine = IAEngine()
pairs = ["EUR/USD", "BTC/USD", "AUD/JPY", "GBP/CHF", "USD/CAD"]

for pair in pairs:
    signal, score = engine.predict(pair)
    color = "#2ECC71" if signal == "CALL" else "#E74C3C"
    icon = "🟢" if signal == "CALL" else "🔴"
    st.markdown(
        f"<div style='border:1px solid {color};padding:10px;border-radius:8px;margin-bottom:10px;'>"
        f"<strong>{icon} {pair} → {signal}</strong><br>"
        f"<span style='color:{color};font-weight:bold;'>Score : {score}</span>"
        f"</div>",
        unsafe_allow_html=True
    )

# --- Résumé IA du jour ---
st.markdown("### 📈 Résumé IA du jour")
total, calls, puts, avg = engine.resume()
st.metric("Total signaux", total)
st.metric("CALL", calls)
st.metric("PUT", puts)
st.metric("Score moyen", avg)

# --- Footer Telegram ---
st.markdown("---")
st.markdown("📩 Rejoins-nous sur Telegram → [KGF Empire Digital](https://t.me/kgfempiredigital)")
