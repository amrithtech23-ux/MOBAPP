import streamlit as st
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Mobile App Forge | Bold Frame Studio",
    page_icon="📱",
    layout="wide"
)

# Load HTML file
html_path = Path("index.html")
if not html_path.exists():
    st.error("❌ index.html not found. Please upload it to the repository.")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

# Get API Key from secrets (using the correct name from your screenshot)
api_key = st.secrets.get("OPENROUTER_API_KEY", "")

if api_key:
    # Replace the placeholder with the actual API key
    html_content = html_content.replace("{{OPENROUTER_API_KEY}}", api_key)
else:
    st.warning("⚠️ `OPENROUTER_API_KEY` not found in secrets. Generation will fail.")
    st.info("Please add your API key in Settings → Secrets as: OPENROUTER_API_KEY = 'your-key-here'")

# Render the HTML interface
st.components.v1.html(html_content, height=1200, scrolling=True)
