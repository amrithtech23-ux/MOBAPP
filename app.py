import streamlit as st
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Mobile App Forge | Bold Frame Studio",
    page_icon="📱",
    layout="wide"
)

# Load HTML & Inject Secure API Key
html_path = Path("index.html")
if not html_path.exists():
    st.error("❌ index.html not found. Please upload it to the repository.")
    st.stop()

html_content = html_path.read_text()
api_key = st.secrets.get("MOBAPPKEY", "")

if api_key:
    html_content = html_content.replace("{{OPENROUTER_API_KEY}}", api_key)
else:
    st.warning("⚠️ `MOBAPPKEY` not found in secrets. Generation will fail.")

# Render the exact UI
st.components.v1.html(html_content, height=1100, scrolling=True)
