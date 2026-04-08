---
title: Hospital OpenEnv
emoji: 🏥
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🏥 AI Hospital Triage & Resource Allocation Environment

## 📌 Problem Statement

This project presents a real-world OpenEnv environment simulating hospital triage and resource allocation. The objective is to train an AI agent to make sequential decisions for prioritizing patients and allocating limited medical resources under dynamic and constrained conditions.

The system models real-life emergency scenarios where decisions directly impact patient survival, waiting time, and resource efficiency.

---

## 🌍 Real-World Relevance

Hospital triage is a critical task in healthcare systems, especially during emergencies and high patient influx situations. This environment captures:

- Patient prioritization based on severity  
- Resource constraints (ICU beds, doctors)  
- Time-sensitive decision-making  
- Trade-offs between efficiency and fairness  

---

## ⚙️ Environment Design (OpenEnv Compliant)

The environment fully implements OpenEnv specifications:

- `reset()` → initializes environment  
- `step(action)` → returns `(state, reward, done, info)`  
- `state()` → returns current state  
- `openenv.yaml` → defines environment schema  

---

## 🧩 Observation Space

```json
{
  "patients": [
    {"id": int, "severity": float, "wait_time": int, "condition": str}
  ],
  "resources": {
    "icu_beds": int,
    "doctors": int
  }
}

## Evaluation Metrics

- Survival optimization
- Resource efficiency
- Waiting time penalties

## Advanced Evaluation

This environment incorporates multi-objective evaluation including:
- Decision explainability
- Efficiency optimization
- Fairness in patient prioritization

This project not only simulates decision-making but also captures ethical and operational trade-offs in real-world healthcare systems.