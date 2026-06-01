
# Phase 3 – LLM Integration & Prompt Engineering

## Prompt Versions
V1 – Basic assistant
V2 – Safety focused
V3 – Structured banking advisor (default)

## Why V3 Was Selected
- Most explainable responses
- Strongest safety behaviour
- Better escalation guidance
- Consistent structure

## New Failure Modes
- LLM may ignore retrieved context
- API outages
- Prompt injection attempts

## Mitigations
- Low temperature
- Safety layer before LLM
- RAG grounding
- Human escalation path
