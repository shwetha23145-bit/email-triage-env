---
title: Email Triage Env
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
tags:
  - openenv
tasks:
  - id: email-classification
    type: text-classification
    grader: grader.py
  - id: urgency-detection
    type: text-classification
    grader: grader.py
  - id: spam-filtering
    type: text-classification
    grader: grader.py
---

# 📧 Intelligent Email Triage OpenEnv

## 🚀 Overview
The **Email Triage Env** is a sophisticated simulation of a high-volume corporate communication hub. This environment is designed to evaluate Large Language Model (LLM) agents on their ability to act as a **first-line digital responder**. 

Unlike simple classifiers, this environment tests for **contextual intelligence**, **professional drafting**, and **adversarial detection** (distinguishing between urgent technical issues and high-pressure phishing attempts).

---

## 🛠 The 3-Tier Benchmark
We have implemented three distinct tasks to measure the agent's progression from basic classification to complex decision-making:

### 1. `email-classification` (Foundational)
- **Goal:** Accurately identify the intent of the sender.
- **Challenge:** The agent must categorize emails into *Spam, Personal, Work,* or *Urgent* categories with zero-shot accuracy.

### 2. `urgency-detection` (Analytic)
- **Goal:** Contextual summarization and professional response drafting.
- **Challenge:** The agent is evaluated on its ability to summarize technical downtime reports and draft a response that uses empathetic, professional corporate language.

### 3. `spam-filtering` (Advanced Routing)
- **Goal:** Enterprise-level department routing and security triage.
- **Challenge:** The "Hard" tier. The agent must identify the specific internal department (Security, Billing, Engineering) based on nuanced clues within the email body, such as IP logs or billing discrepancies.

---

## 🧠 Technical Architecture
This project is built using the **OpenEnv** framework and served via a **Dockerized FastAPI** backend.

- **Environment Logic:** Implemented in Python, simulating a stateful inbox where the agent must process a sequence of varied emails.
- **Granular Reward System:** The `grader.py` utilizes a multi-factor reward function that rewards not just the correct "label," but also the length, professional tone, and routing accuracy of the agent's output.
- **Agentic Workflow:** Designed to be compatible with advanced LLM architectures like Qwen-72B and Llama-3, enforcing strict JSON output schemas for downstream business automation.

---

## 📈 Evaluation
The environment provides a float-based reward strictly within the `(0, 1)` range, ensuring fine-grained feedback for RL-based agent training. A success score of **0.4 or higher** is required for an agent to be considered "proficient" at the triage task.

---
*Developed for the Meta PyTorch Hackathon x Scaler School of Technology.*
