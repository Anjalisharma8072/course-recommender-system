import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from io import StringIO

df = pd.read_csv("C:\\Users\\hp\\Downloads\\courseeee recommender system\\3.1-data-sheet-udemy-courses-web-development.csv")
df['course_title'] = df['course_title'].fillna('')

def vectorize_text_to_cosine_mat(data):
    count_vect = CountVectorizer()
    cv_mat = count_vect.fit_transform(data)
    cosine_sim_mat = cosine_similarity(cv_mat)
    return cosine_sim_mat


def get_recommendation_by_skills(skills, cosine_sim_mat, df, num_of_rec=10):
   
    query = ' '.join(skills)

    
    query_vector = count_vect.transform([query])
    cosine_scores = cosine_similarity(query_vector, cv_mat)

    
    course_indices = cosine_scores.argsort()[0][-num_of_rec-1:-1][::-1]  # Exclude the query itself
    recommended_courses = df.iloc[course_indices][['course_title', 'url', 'price', 'num_subscribers']]

    return recommended_courses




count_vect = CountVectorizer()
cv_mat = count_vect.fit_transform(df['course_title'])



num_recommendations = 5 

