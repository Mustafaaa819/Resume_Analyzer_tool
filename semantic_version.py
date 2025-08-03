import pandas as pd
import numpy as np
import openai
import time
import os
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("KEY")

#get embeddings: numeric representation of words, sentences or meanings.
def get_embeddings(text):
    reply = openai.embeddings.create(input=text, model='text-embedding-ada-002')
    return reply

#compare two texts by meaning, not just by spelling.
def semantic_similarity(text1, text2):
    emb1 = np.array(get_embeddings(text1))
    emb2 = np.array(get_embeddings(text2))
    return cosine_similarity(emb1, emb2)


def calculate_score(row):
    resume_skills = [skill.strip().lower() for skill in row['Skills'].split(',')]
    resume_education = [edu.strip().lower() for edu in row['Education'].split(',')]
    resume_experience = int(row['Experience'])

    semantic_match_score = 0
    for r_skill in resume_skills:
        for req_skill in required_skills:
            try:
                similarity = semantic_similarity(r_skill, req_skill)
                if similarity > 0.75:
                    semantic_match_score += 1
            except:
                continue
    skill_score = semantic_match_score * 10

    # Experience_Score:
    experience_score = resume_experience * 5

    # Education_Score:
    education_score = 0
    for edu in resume_education:
        if edu in required_education:
            if edu in ['bachleor of science', 'bs']:
                education_score += 5
            elif edu in ['master of science', 'ms']:
                education_score += 7
            elif edu in ['phd']:
                education_score += 10

    # Degree_Score:
    degree_score = 0
    for deg in resume_education:
        if deg in required_degrees:
            if deg in ['mba', 'civil', 'mechanical', 'electrical']:
                degree_score += 5
            elif deg in ['computer science', 'cs', 'software engineering', 'se', 'artificial intelligence', 'ai']:
                degree_score += 10

    return skill_score + experience_score + education_score + degree_score


print("-----Welcome to Resume Ranker based on Skills, Experience and Education----")
time.sleep(1.5)
print("Write down the Skills you want in a person, and we'll find that for you asap😉.")
time.sleep(1.5)

# Required Skills:
skills_input = input("Enter the Skills you are looking for: ")
required_skills = [skill.strip().lower() for skill in skills_input.split(',')]

# Required Education:
education_input = input("Enter the Education you are looking for: ")
required_education = [edu.strip().lower() for edu in education_input.split(',')]

# required_Degrees:
degree_input = input("Enter the Degrees you are looking for: ")
required_degrees = [deg.strip().lower() for deg in degree_input.split(',')]

print("Working on it....")

df = pd.read_csv('resume_data.csv')
df['Score'] = df.apply(calculate_score, axis=1)

df_sorted = df.sort_values(by='Score', ascending=False).reset_index(drop=True)

print("\n🍾Here are the Ranked Candidates:")
time.sleep(1.5)
print(df_sorted[['Name', 'Education', 'Experience', 'Skills', 'Score']])
df_sorted.to_csv("Rankings.csv", index=False)
























