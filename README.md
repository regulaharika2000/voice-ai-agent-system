# 🏥 Real-Time Multilingual Voice AI Agent

A real-time voice AI system for clinical appointment booking with multilingual support, memory, and tool-based reasoning.

---

## 📌 Problem Statement

Build a real-time voice AI agent that:
- Handles clinical appointment booking
- Works in English, Hindi, and Tamil
- Maintains session + long-term memory
- Supports outbound/inbound interactions
- Handles scheduling conflicts intelligently
- Operates with low latency (<450ms target)

---

## ⚙️ Tech Stack

- Python (FastAPI)
- WebSockets (real-time communication)
- JavaScript (frontend test client)
- In-memory session store (mock Redis alternative)
- Custom scheduler engine
- Mock LLM (no API dependency)

---

## 🧠 System Architecture

User speaks or types → WebSocket → Orchestrator → Intent Engine → Tool Layer → Scheduler → Memory → Response → Frontend

---

## 🧩 Key Features

### 🔹 1. Real-Time Voice Agent
- WebSocket-based streaming
- Instant request-response cycle

### 🔹 2. Appointment Scheduling Engine
- Doctor-wise calendar
- Conflict detection
- Smart slot suggestions

### 🔹 3. Memory System
- Session-based memory
- Stores:
  - last doctor
  - last appointment time
  - last action
  - conversation history

### 🔹 4. Multilingual Support
- English / Hindi / Tamil detection (rule-based)
- Language stored per session

### 🔹 5. Tool Calling System
- book_appointment()
- cancel_appointment()
- check_availability()

### 🔹 6. Performance Tracking
- End-to-end latency measurement
- SLA target: <450ms

---

## ⏱️ Latency Design

- WebSocket receive → processing → response send
- Logged per request
- SLA violation detection included

---

## 🧠 Memory Design

Session-based dictionary:

- user input history
- last intent
- last doctor
- last booking time
- conversation state

---

## 🧪 How to Run

```bash
cd backend
python run.py