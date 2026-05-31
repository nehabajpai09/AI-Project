# AI Banking Support & Advisory Agent

## Overview

The AI Banking Support & Advisory Agent is a production-style Applied AI system designed for non-transactional banking support workflows.

The project demonstrates:

* Retrieval-Augmented Generation (RAG),
* tool-based AI orchestration,
* EMI calculation,
* fraud escalation,
* safety guardrails,
* and PII-safe logging.

The system is intentionally restricted from:

* money transfers,
* transaction approvals,
* legal advice,
* or customer data access.

---

# Features

## Supported Capabilities

* Banking FAQ assistance
* EMI calculation
* Loan guidance
* Credit score guidance
* Fraud escalation
* Retrieval-based banking knowledge search
* PII-safe logging
* Safety-first refusals

---

# Safety Constraints

The agent:

* refuses unsafe financial actions,
* avoids hallucinating customer information,
* escalates suspicious activity,
* and sanitizes logs.

Restricted actions include:

* money movement,
* OTP bypassing,
* legal advice,
* customer data disclosure,
* transaction approvals.

---

# Project Architecture

```text
bank_ai_agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── core/
│   ├── agent.py
│   ├── safety.py
│   ├── router.py
│   ├── prompts.py
│   └── logger.py
│
├── tools/
│   ├── emi_tool.py
│   ├── rag_tool.py
│   ├── faq_tool.py
│   └── escalation_tool.py
│
├── data/
│   └── banking_faqs.txt
│
├── logs/
│   └── agent_logs.json
│
├── vector_store/
│   └── chroma_db/
│
├── scripts/
│   └── build_vector_db.py
│
└── evaluation/
    ├── test_cases.py
    ├── safety_tests.py
    ├── retrieval_tests.py
    └── evaluation_report.md
```

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
cd bank_ai_agent
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

## Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Build Vector Database

Before running the agent, initialize the Chroma vector database:

```bash
python scripts/build_vector_db.py
```

This creates:

```text
vector_store/chroma_db/
```

---

# Run the Application

```bash
python app.py
```

---

# Example Queries

## Banking FAQ

```text
What is a good credit score?
```

---

## EMI Calculation

```text
Calculate EMI for 800000 at 9% for 120 months
```

---

## Fraud Escalation

```text
My account was hacked
```

---

## Unsafe Request

```text
Transfer money to another account
```

---

# Technologies Used

| Component       | Technology            |
| --------------- | --------------------- |
| Language        | Python                |
| Embeddings      | Sentence Transformers |
| Vector Database | ChromaDB              |
| Framework       | LangChain             |
| Logging         | JSON                  |
| Retrieval       | Semantic Search       |

---

# Evaluation

Evaluation includes:

* retrieval testing,
* safety testing,
* EMI validation,
* escalation testing,
* hallucination prevention,
* and governance checks.

See:

```text
evaluation/evaluation_report.md
```

---

# Current Limitations

* Small banking knowledge base
* Rule-based routing
* No conversational memory
* No live banking APIs
* No multilingual support
* CLI-only interface

---

# Future Improvements

Planned upgrades:

* LangGraph orchestration
* Conversational memory
* FastAPI deployment
* Streamlit dashboard
* LLM-based routing
* Hybrid retrieval
* LangSmith tracing
* Real-time monitoring

---
