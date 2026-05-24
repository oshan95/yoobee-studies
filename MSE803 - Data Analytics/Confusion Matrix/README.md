# Week 7 – Activity 1: Confusion Matrix

## Overview

This activity demonstrates how to construct and interpret a **confusion matrix** for a binary classification model developed for a healthcare system. The model classifies patients into two categories — **Healthy** or **Sick** — based on medical test results and symptoms.

---

## Dataset

| Split | Records |
|-------|---------|
| Total | 100 patient records (routine health screenings) |
| Training | 70 records |
| Testing | 30 records |

---

## Model Performance

After training, the model was evaluated on **30 unseen test records**. It made **3 incorrect predictions**:

- **2 sick patients** were predicted as Healthy → **False Negatives (FN)**
- **1 healthy patient** was predicted as Sick → **False Positive (FP)**

---

## Confusion Matrix

|  | Predicted: Healthy | Predicted: Sick |
|---|---|---|
| **Actual: Healthy** | 14 — True Negative (TN) | 1 — False Positive (FP) |
| **Actual: Sick** | 2 — False Negative (FN) | 13 — True Positive (TP) |

### Cell Definitions

| Term | Abbreviation | Description |
|------|-------------|-------------|
| True Negative | TN = 14 | Healthy patients correctly predicted as Healthy |
| False Positive | FP = 1 | Healthy patient incorrectly predicted as Sick |
| False Negative | FN = 2 | Sick patients incorrectly predicted as Healthy |
| True Positive | TP = 13 | Sick patients correctly predicted as Sick |

> ⚠️ **Note:** The 2 False Negatives are the most critical errors in a healthcare context — a missed diagnosis can delay treatment for sick patients.

---

## Performance Metrics

| Metric | Formula | Calculation | Result |
|--------|---------|-------------|--------|
| **Accuracy** | (TP + TN) / Total | (13 + 14) / 30 | **90.0%** |
| **Precision** | TP / (TP + FP) | 13 / (13 + 1) | **92.9%** |
| **Recall (Sensitivity)** | TP / (TP + FN) | 13 / (13 + 2) | **86.7%** |
| **Specificity** | TN / (TN + FP) | 14 / (14 + 1) | **93.3%** |
| **F1 Score** | 2 × (Precision × Recall) / (Precision + Recall) | 2 × 0.929 × 0.867 / (0.929 + 0.867) | **89.7%** |

---

## Key Takeaways

- The model achieves **90% overall accuracy** on the test set.
- **Precision (92.9%)** is high — when the model predicts Sick, it is correct most of the time.
- **Recall (86.7%)** is slightly lower — the model misses about 13% of actual Sick patients.
- In healthcare, **Recall is typically the priority metric** because false negatives (missed diagnoses) carry a higher risk than false positives.
- The **F1 Score of 89.7%** reflects a good balance between Precision and Recall.

---

## Files

| File | Description |
|------|-------------|
| `confusion_matrix_healthcare.xlsx` | Colour-coded confusion matrix with metrics table |
| `README.md` | This file — activity summary and interpretation |


