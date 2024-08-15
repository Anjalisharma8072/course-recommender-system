from flask import Flask, render_template,request
import os
import pandas as pd

# File path to the Python script
popular_script_path = os.path.join(os.path.dirname(__file__), 'popular.py')
popular_script_path2 = os.path.join(os.path.dirname(__file__), 'content.py')
# popular_script_path3 = os.path.join(os.path.dirname(__file__), 'quiz.py')

# Execute the Python script and obtain the DataFrame
with open(popular_script_path, 'r') as script_file:
    exec(script_file.read(), globals())
with open(popular_script_path2, 'r') as script_file:
    exec(script_file.read(), globals())

app = Flask(__name__)

df['course_title'] = df['course_title'].fillna('')

# Vectorize the course titles for cosine similarity
count_vect = CountVectorizer()
cv_mat = count_vect.fit_transform(df['course_title'])

# Recommendation Sys
def get_recommendation_by_skills(skills, count_vect, cv_mat, df, num_of_rec=10):
    # Combine the skills into a query
    query = ' '.join(skills)

    # Find courses similar to the query using cosine similarity
    query_vector = count_vect.transform([query])
    cosine_scores = cosine_similarity(query_vector, cv_mat)

    # Get the top courses
    course_indices = cosine_scores.argsort()[0][-num_of_rec-1:-1][::-1]  # Exclude the query itself
    recommended_courses = df.iloc[course_indices][['course_title', 'url', 'level', 'num_subscribers']]

    return recommended_courses

    

@app.route("/")
def index():
    return render_template('index.html', 
    course_title=list(popularity_df['course_title'].values),
    url = list(popularity_df['url'].values),
    level = list(popularity_df['level'].values),
    num_subscribers  = list(popularity_df['num_subscribers'].values)
    )

@app.route("/contact")
def contact_us():
    return render_template('contact.html')

@app.route("/about")
def about_us():
    return render_template('about.html')

@app.route("/quiz")
def quiz_ui():
    return render_template('quiz.html')

@app.route('/recommend')
def recommend_ui():
    return render_template('index2.html')
    



@app.route('/recommend_course', methods=['POST'])

def recommend():
    try:
        user_skills = request.form.get('user_skills')
        print(f"User skills received: {user_skills}")  
        num_recommendations = 5

        recommended_courses = get_recommendation_by_skills(user_skills.split(','), count_vect, cv_mat, df, num_recommendations)

        return render_template('index2.html',
                               course_title=list(recommended_courses['course_title'].values),
                               url=list(recommended_courses['url'].values),
                               level = list(recommended_courses['level'].values),
                               num_subscribers=list(recommended_courses['num_subscribers'].values))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)
