import pandas as pd
import numpy as np
import time

df = pd.read_csv('dummy_resume.csv')

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

#Score_Calculation:
def calculate_score(row):
    #Skill_Score:
    resume_skills = [skill.strip().lower() for skill in row['Skills'].split(',')]
    skills_match = sum(1 for skill in required_skills if skill in resume_skills)
    skill_score = skills_match*10

    #Experience_score:
    resume_experience = int(row['Experience'])
    experience_score = resume_experience*5

    #Education_Score:
    resume_education = [edu.strip().lower() for edu in row['Education'].split(',')]
    education_match = sum(1 for edu in required_education if edu in resume_education)
    education_score = education_match*10

    total_score = skill_score + experience_score + education_score
    return total_score

df['Score'] = df.apply(calculate_score, axis=1)
df_sort = df.sort_values(by='Score', ascending=False).reset_index(drop=True)

print('Ranked Candidates:')
print(df_sort[['Name', 'Skills', 'Education', 'Experience', 'Score']])
df_sort.to_csv('final.csv')


