import streamlit as st
import pandas as pd
from PIL import Image
import datetime
import random

# ====================================
# 🔧 MOTEUR IA CALL/PUT
# ====================================

class KGFSignalEngine:
    def __init__(self):
        self.history = []

    def fused_prediction(self, pair_name):
        prob_call = random.uniform(0.45, 0.9)
        prob_put = random.uniform(0.1, 0.55)
        signal_type = "CALL" if prob_call > prob_put else "PUT"
        score = self.compute_signal_score(prob_call, prob_put)

        self.history.append({
            "pair": pair_name,
            "type": signal_type,
            "score": round(score, 3),
            "prob_call": round(prob_call, 3),
            "prob_put": round(prob_put, 3),
            "timestamp": datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        })

        return signal_type, score

    def compute_signal_score(self, prob_call, prob_put):
        dominance = abs(prob_call - prob_put)
        confidence = max(prob_call, prob_put)
        return dominance * confidence

    def get_summary(self):
        total = len(self.history)
        call_count = sum(1 for s in self.history if s["type"] == "CALL")
        put_count = total - call_count
        avg_score = round(sum(s["score"] for s in self.history) / total, 3) if total > 0 else 0
        return total, call_count, put_count, avg_score

# ====================================
# 🌐 PAGE PRINCIPALE
# ====================================

st.set_page_config(page_title="KGFsignalCraft", layout="wide")

# 🎬 Bannière animée
st.video("kgf_banner.mp4")

# 📣 Titre et accroche
st.markdown("<h1 style='text-align:center;'>KGF Trading Signal Bot</h1>", unsafe_allow_html=True)
st.markdown("<center><em>Du silence des moqueries à la puissance des résultats</em></center>", unsafe_allow_html=True)
st.markdown("---")

# 📊 SECTION : Performance classique
st.subheader("📈 Ratios & Performances de marché")
try:
    df = pd.read_csv("performance.csv")
    st.dataframe(df)

    if "ratio" in df.columns:
        st.line_chart(df["ratio"])

    st.success("✅ Fichier 'performance.csv' chargé avec succès.")
except Exception as e:
    st.warning(f"⚠️ Erreur lors du chargement : {e}")

st.markdown("---")

# 🧠 SECTION : Analyse IA CALL/PUT
st.subheader("🧠 Réflexion stratégique IA (Simulations CALL/PUT)")
kgf_engine = KGFSignalEngine()

pairs = ["EUR/USD", "BTC/USD", "AUD/JPY", "GBP/CHF", "USD/CAD"]
for pair in pairs:
    signal, score = kgf_engine.fused_prediction(pair)
    couleur = "#2ECC71" if signal == "CALL" else "#E74C3C"
    icone = "🟢" if signal == "CALL" else "🔴"

    st.markdown(
        f"<div style='border:1px solid {couleur};padding:10px;border-radius:8px;margin-bottom:10px;'>"
        f"<strong>{icone} {pair} → {signal}</strong><br>"
        f"<span style='color:{couleur};font-weight:bold;'>Score : {score}</span>"
        f"</div>",
        unsafe_allow_html=True
    )

# 🔁 Résumé des signaux générés
total, call_count, put_count, avg_score = kgf_engine.get_summary()
st.markdown("### 🔎 Résumé IA du jour")
st.metric("Total Signaux", total)
st.metric("CALL", call_count)
st.metric("PUT", put_count)
st.metric("Score Moyen", avg_score)

st.markdown("---")

# 📱 FOOTER TELEGRAM
st.markdown("📩 Rejoins notre QG sur Telegram → [KGF Empire Digital](https://t.me/kgfempiredigital)")
