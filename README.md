# MedAI – Chronic Disease Monitoring Agent

MedAI is an AI-powered assistant designed to **monitor chronic disease health data**, identify **early risk trends**, and provide **assistive (non-diagnostic) insights** using Retrieval-Augmented Generation (RAG).

The system is built using **IBM Granite models**, **LangFlow**, and a **vector database** to analyze patient health logs such as glucose levels, blood pressure, peak flow readings, and medication adherence.

---

## What This Project Does

MedAI helps with:
- Continuous analysis of patient health data
- Detecting abnormal trends and risk escalation
- Generating early warning alerts
- Providing personalized lifestyle and self-care recommendations
- Summarizing patient health trends for caregivers or clinicians

⚠️ This tool is **assistive only** and does not provide medical diagnoses.

---

## How It Works (High Level)

1. Patient health data is ingested (manual input or file-based)
2. Data is converted into vector embeddings
3. Embeddings are stored in a vector database (Astra DB)
4. When a query is made:
   - Relevant patient history is retrieved using semantic search
   - Retrieved context is combined with the user query
5. An IBM Granite instruction-tuned model analyzes:
   - Short-term and long-term health trends
   - Threshold breaches and risk escalation
6. The system outputs:
   - Health insights
   - Early risk alerts
   - Lifestyle recommendations via a chat interface

---

## Tech Stack

### AI & ML
- **IBM Granite 3 (8B Instruct)** – Reasoning and response generation
- **IBM watsonx.ai** – Model hosting and inference
- **IBM watsonx Embeddings** – Vector embedding generation
- **Retrieval-Augmented Generation (RAG)**

### Orchestration
- **LangFlow**
  - Chat Input
  - Prompt Templates
  - Parser
  - Chat Output
  - URL Loader
  - Split Text

### Data Storage
- **Astra DB** – Vector database for semantic retrieval

### Cloud
- **IBM Cloud**

---

## How to Use

### Prerequisites
- IBM Cloud account
- watsonx.ai access
- Astra DB account
- LangFlow installed locally or deployed

### Basic Usage

1. Set up Astra DB and create a vector collection
2. Configure IBM watsonx credentials in LangFlow
3. Import the LangFlow workflow provided in the project
4. Upload or input patient health data (logs, reports, or text)
5. Start the LangFlow application
6. Interact with the system via the chat interface:
   - Ask for trend analysis
   - Request risk alerts
   - Get lifestyle recommendations

---

## Example Use Cases

- Diabetes and hypertension monitoring
- Asthma and respiratory condition tracking
- Medication adherence monitoring
- Lifestyle risk assessment based on activity trends

---

## Limitations

- Does not replace medical professionals
- Depends on quality and accuracy of input data
- Threshold logic is generalized and not patient-specific by default

---

## Future Improvements

- Real-time wearable and IoT data integration
- Predictive analytics before threshold breaches
- Multilingual and voice-based interfaces
- Mobile application deployment
- EHR and hospital system integration

---

## Disclaimer

This project is intended for **educational and assistive purposes only** and should not be used as a medical diagnostic tool.
