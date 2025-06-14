
import streamlit as st

st.title("📈 Forex Wizard Signal App")
st.subheader("🧠 Strong Buy/Sell Signals Based on Chart Screenshot")
st.write("Enter your strategy-based prediction below.")

entry = st.text_input("📌 Entry Price")
tp = st.text_input("🎯 Take Profit (TP)")
sl = st.text_input("🛑 Stop Loss (SL)")
signal = st.selectbox("📊 Signal Type", ["Buy", "Sell"])
note = st.text_area("📋 Additional Notes or Reason")

if st.button("Generate Signal"):
    st.success(f"{signal} Signal Generated ✅")
    st.markdown(f"""
    **Entry Price:** {entry}  
    **Take Profit (TP):** {tp}  
    **Stop Loss (SL):** {sl}  
    **Note:** {note}
    """)
