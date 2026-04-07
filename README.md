# Email Triage Environment

## 📧 Overview
This environment simulates real-world email classification.

## 🎯 Tasks
- Easy: classify category
- Medium: category + priority
- Hard: category + priority + action

## ⚙️ Run
pip install pydantic
python inference.py

## 📊 Score
Each step gives reward:
- Category: 0.4
- Priority: 0.3
- Action: 0.3