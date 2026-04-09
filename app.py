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

# Get API Key from secrets - try multiple possible key names
api_key = (st.secrets.get("OPENROUTER_API_KEY") or 
           st.secrets.get("OPENROUTER_API_KEY", "") or
           st.secrets.get("MOBAPPKEY", ""))

# Debug: Show if key is found (first 20 chars only for security)
if api_key:
    st.success(f"✅ API Key loaded successfully! (Key starts with: {api_key[:20]}...)")
    # Replace the placeholder with the actual API key
    html_content = html_content.replace("{{OPENROUTER_API_KEY}}", api_key)
else:
    st.error("❌ API Key NOT found in secrets!")
    st.warning("⚠️ Please check your Streamlit Secrets configuration.")
    st.info("**Expected format in Secrets:**\n```\nOPENROUTER_API_KEY = \"sk-or-v1-your-key-here\"\n```")
    # Still replace with empty string to avoid placeholder in code
    html_content = html_content.replace("{{OPENROUTER_API_KEY}}", "")

# Render the HTML interface
st.components.v1.html(html_content, height=1200, scrolling=True)
