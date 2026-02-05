# Bookxpert AIML Assignment

**Applicant Name:** Saurav Patel  
**Role:** AIML Developer  

---

## 📖 Overview

This repository contains **two standalone Python projects** demonstrating practical applications of:

- String similarity matching
- Rule-based recommendation systems  

Both projects are implemented using modern Python libraries and are fully local.

---

## 📂 Projects Overview

| Task | Description | Tech Stack |
|-----|-------------|------------|
| Task 1 | Fuzzy Name Matching System | RapidFuzz, Python |
| Task 2 | Local Recipe Recommendation Chatbot API | FastAPI, Uvicorn |

---

## 📌 Task 1: Name Matching System

### 📝 Description

A command-line tool that identifies the **closest matching person names** from a predefined dataset using **fuzzy string matching**.  
Designed to handle spelling variations, typos, and phonetic similarities.

### ✨ Features

- Fast and accurate matching using **RapidFuzz**
- Returns:
  - Best matching name
  - Ranked list of similar names with similarity scores
- Lightweight and fully offline

### ⚙️ Installation

```bash
pip install rapidfuzz
