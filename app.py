import streamlit as st
import requests

# Streamlit App Title
st.title("🚀 Langflow Astra API - Chronic Disease Monitoring Agent")

# User input
user_input = st.text_input("💬 Enter your request:", "Analyze patient health data using the provided context to identify risk trends and provide safe, non-diagnostic lifestyle recommendations aligned with clinical guidelines.")

# API endpoint & headers
url = "https://api.langflow.astra.datastax.com/lf/3e1ee4ba-21f0-4b05-a479-14553904059c/api/v1/run/9c5bad27-1fa5-4e72-846f-1d82606dcb2c"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {LANGFLOW_TOKEN}"
}

# Button to send input
if st.button("Send to Langflow"):
    payload = {
        "input_value": user_input,
        "output_type": "chat",
        "input_type": "chat"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        # Extract only the "text" field from nested JSON
        try:
            text_output = result["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
            st.success("✅ Results Generated")
            st.write(text_output)  # Only show text
        except (KeyError, IndexError):
            st.error("⚠️ Could not extract text from response")
            st.json(result)  # fallback: show full JSON

    except requests.exceptions.RequestException as e:
        st.error(f"❌ API request error: {e}")
    except ValueError as e:
        st.error(f"❌ Response parsing error: {e}")

