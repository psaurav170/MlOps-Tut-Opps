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
---

## 📌 Task 2: Local Recipe Recommendation Chatbot API

### 📝 Description

A lightweight **REST API chatbot** that suggests recipes based on ingredients provided by the user.
It uses set-based similarity matching to determine the most relevant recipe.

### ✨ Features

- Built using **FastAPIz**
- Ingredient overlap–based scoring
- Returns:
  - Suggested recipe
  - Matched ingredients
  - Confidence level
- No external APIs or machine learning required

### ⚙️ Installation

pip install fastapi uvicorn

### ⚙️ Run the Server

python recipe_chatbot.py
http://127.0.0.1:8000

### ⚙️ API Endpoint
POST /get_recipe
{
  "ingredients": "egg, onion, salt"
}
#### Sample Response
{
  "chatbot_reply": "👩‍🍳 Here's a recipe you can try!",
  "your_ingredients": ["egg", "onion", "salt"],
  "matched_ingredients": ["egg", "onion", "salt"],
  "suggested_recipe": "Egg Omelette: Beat eggs, add chopped onions and salt. Fry until golden.",
  "confidence_level": "3 ingredient(s) matched"
}

### ⚙️ Interactive API Documentation
FastAPI automatically generates Swagger UI:
http://127.0.0.1:8000/docs


