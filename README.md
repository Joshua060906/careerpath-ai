# CareerPath AI – AI-Based Career Guidance System

## Live Demo

Live Project Link: [https://your-deployment-link.com](https://careerpath-ai-0zcv.onrender.com)

---

## Screenshots

### Home Dashboard
<img width="1875" height="856" alt="image" src="https://github.com/user-attachments/assets/0cb9bb3f-5f3c-4516-bc1a-5cac1697839c" />


### Career Prediction Page
<img width="1876" height="862" alt="image" src="https://github.com/user-attachments/assets/f03bfd4e-dd63-452d-98bc-ca21fb6bc1dc" />

---

# Overview

CareerPath AI is an intelligent career guidance platform designed to help students discover suitable career paths based on their skills, interests, and academic strengths. The system uses Machine Learning algorithms to analyze student profiles and provide personalized career recommendations, skill-gap analysis, resume insights, and learning roadmaps.

This project was developed using Python, Flask, and Machine Learning technologies with a production-ready architecture for cloud deployment.

---

# Features

- AI-Based Career Prediction
- Student Skill Analysis
- Resume Parsing & Skill Extraction
- Personalized Learning Roadmaps
- Skill Gap Detection
- Career Recommendation Dashboard
- REST API Integration
- Docker Support for Deployment
- Cloud Deployment Ready
- User-Friendly Interface

---

# Machine Learning Capabilities

The system analyzes multiple parameters such as:

- Python Skills
- Java Skills
- Mathematical Ability
- Logical Reasoning
- Communication Skills

Based on these inputs, the ML model predicts careers like:

- Software Engineer
- Data Scientist
- AI Engineer
- Cybersecurity Analyst
- UI/UX Designer

---

# Tech Stack

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

## Database
- SQLite / MySQL

## Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

## Deployment
- Docker
- Render / Railway / AWS Ready

---

# Project Structure

CareerPath-AI/

│

├── app/

│   ├── main.py

│   ├── models/

│   ├── routes/

│   ├── services/

│   ├── templates/

│   └── static/

│

├── data/

├── train_model.py

├── requirements.txt

├── Dockerfile

├── run.py

└── README.md

---

# Installation

## 1. Clone Repository

git clone https://github.com/yourusername/CareerPath-AI.git

cd CareerPath-AI

---

## 2. Create Virtual Environment

python -m venv venv

### Activate Environment

### Windows

venv\Scripts\activate

### Linux/Mac

source venv/bin/activate

---

## 3. Install Dependencies

pip install -r requirements.txt

---

# Run the Project

python run.py

---

# Train Machine Learning Model

python train_model.py

---

# Docker Deployment

## Build Docker Image

docker build -t careerpath-ai .

## Run Docker Container

docker run -p 5000:5000 careerpath-ai

---

# API Example

## POST /predict

### Request

{
  "python": 9,
  "java": 7,
  "math": 8,
  "communication": 6,
  "logic": 9
}

### Response

{
  "recommended_career": "Data Scientist",
  "required_skills": [
    "Python",
    "SQL",
    "Statistics"
  ]
}

---

# Future Improvements

- AI Career Chatbot
- Real-Time Job Recommendation
- LinkedIn API Integration
- Resume ATS Score Checker
- Interview Preparation Module
- Admin Dashboard
- Student Progress Tracking

---

# Author

Joshua G Jiju

- B.Tech Student
- Interested in AI & Machine Learning
- Passionate about Full Stack Development

---

# Project Highlights

- Production-Ready Architecture
- Cloud Deployment Support
- Scalable Flask Backend
- Machine Learning Integration
- Student-Centric Design

---

# License

This project is licensed under the MIT License.

---

# Support

If you like this project, give it a star on GitHub and share it with others.
