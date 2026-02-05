# Bookxpert AIML Assignment

**Applicant Name:** Saurav Patel  
**Role:** AIML Developer  

Author: Saurav Patel

This repository contains two standalone Python projects demonstrating practical applications of string similarity matching and rule-based recommendation systems using modern Python libraries.

📂 Projects Overview
Task	Description	Tech Stack
Task 1	Fuzzy Name Matching System	RapidFuzz, Python
Task 2	Local Recipe Recommendation Chatbot API	FastAPI, Uvicorn
📌 Task 1: Name Matching System
📝 Description

A command-line tool that identifies the closest matching person names from a predefined dataset using fuzzy string matching.
Designed to handle spelling variations, typos, and phonetic similarities.

✨ Features

Fast and accurate matching using RapidFuzz

Returns:

Best matching name

Ranked list of similar names with similarity scores

Lightweight and fully offline

⚙️ Installation
pip install rapidfuzz

▶️ Usage
python name_matching.py


Example

Enter a name to search: Geeta


Output

Best Match:
{'name': 'Geeta', 'similarity_score': 100}

Other Similar Matches:
{'name': 'Geetha', 'similarity_score': 92}
{'name': 'Gita', 'similarity_score': 89}

📌 Task 2: Local Recipe Chatbot (FastAPI)
📝 Description

A lightweight REST API chatbot that suggests recipes based on ingredients provided by the user.
It uses set-based similarity matching to determine the most relevant recipe.

✨ Features

Built with FastAPI

Ingredient overlap–based scoring

Returns:

Suggested recipe

Matched ingredients

Confidence level

No external APIs or machine learning required

⚙️ Installation
pip install fastapi uvicorn

▶️ Run the Server
python recipe_chatbot.py


Server runs at:

http://127.0.0.1:8000

🔌 API Endpoint

POST /get_recipe

Request Body
{
  "ingredients": "egg, onion, salt"
}

Sample Response
{
  "chatbot_reply": "👩‍🍳 Here's a recipe you can try!",
  "your_ingredients": ["egg", "onion", "salt"],
  "matched_ingredients": ["egg", "onion", "salt"],
  "suggested_recipe": "Egg Omelette: Beat eggs, add chopped onions and salt. Fry until golden.",
  "confidence_level": "3 ingredient(s) matched"
}

📘 Interactive API Docs

FastAPI automatically generates Swagger UI:

http://127.0.0.1:8000/docs

🧱 Project Structure
.
├── name_matching.py
├── recipe_chatbot.py
├── README.md

🚀 Potential Enhancements

Add phonetic algorithms (Soundex / Metaphone) for name matching

Enable weighted ingredient matching

Support multiple recipe suggestions

Persist recipes using a database

Build a simple frontend UI
