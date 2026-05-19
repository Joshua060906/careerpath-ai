import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {

    "marks": [
        9,8,9,8,7,
        6,7,5,6,5,
        9,9,8,9,8,
        5,4,5,6,5,
        8,7,8,9,8,
        6,7,6,7,6,
        9,8,9,8,9,
        7,6,7,6,7,
        8,9,8,9,8,
        5,6,5,6,5,

        8,7,8,7,8,
        9,8,9,8,9,
        6,5,6,5,6,
        7,8,7,8,7,
        8,9,8,9,8,
        5,4,5,4,5,
        9,9,8,8,9,
        7,6,7,6,7,
        8,7,8,7,8,
        6,5,6,5,6
    ],

    "coding": [
        9,8,9,8,7,
        5,6,5,6,5,
        9,8,9,8,9,
        3,2,3,4,3,
        8,7,8,7,8,
        6,5,6,5,6,
        9,8,9,8,9,
        7,6,7,6,7,
        8,9,8,9,8,
        4,5,4,5,4,

        7,6,7,6,7,
        9,8,9,8,9,
        5,4,5,4,5,
        6,7,6,7,6,
        8,9,8,9,8,
        3,2,3,2,3,
        9,8,9,8,9,
        7,6,7,6,7,
        8,7,8,7,8,
        5,4,5,4,5
    ],

    "communication": [
        7,8,7,8,7,
        9,8,9,8,9,
        6,7,6,7,6,
        9,9,8,8,9,
        7,8,7,8,7,
        9,8,9,8,9,
        5,6,5,6,5,
        7,8,7,8,7,
        6,7,6,7,6,
        9,9,8,8,9,

        8,9,8,9,8,
        5,6,5,6,5,
        9,8,9,8,9,
        7,8,7,8,7,
        6,7,6,7,6,
        9,9,8,8,9,
        5,6,5,6,5,
        7,8,7,8,7,
        6,7,6,7,6,
        9,8,9,8,9
    ],

    "career": [

        0,0,0,0,0,      # Software Engineer
        1,1,1,1,1,      # Data Scientist
        2,2,2,2,2,      # Cyber Security Analyst
        3,3,3,3,3,      # UI/UX Designer
        4,4,4,4,4,      # Cloud Engineer
        5,5,5,5,5,      # Digital Marketer
        6,6,6,6,6,      # AI Engineer
        7,7,7,7,7,      # Business Analyst
        8,8,8,8,8,      # DevOps Engineer
        9,9,9,9,9,      # Graphic Designer

        10,10,10,10,10, # Web Developer
        11,11,11,11,11, # Mobile App Developer
        12,12,12,12,12, # Database Administrator
        13,13,13,13,13, # Network Engineer
        14,14,14,14,14, # Game Developer
        15,15,15,15,15, # Content Writer
        16,16,16,16,16, # Machine Learning Engineer
        17,17,17,17,17, # Product Manager
        18,18,18,18,18, # Blockchain Developer
        19,19,19,19,19  # Ethical Hacker
    ]
}

df = pd.DataFrame(data)

X = df[["marks", "coding", "communication"]]

y = df["career"]

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X, y)

with open("career_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("20 Career AI Model Trained Successfully")