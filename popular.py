import pandas as pd
course = pd.read_csv("C:\\Users\\hp\\Downloads\\courseeee recommender system\\3.1-data-sheet-udemy-courses-web-development.csv")
num_rating_df = course.groupby('course_title')['Rating'].count().reset_index()
num_rating_df.rename(columns={'Rating': 'num_ratings'}, inplace=True)
avg_rating_df = course.groupby('course_title').agg({'Rating': 'mean', 'url': 'first','level':'first','num_subscribers':'first'}).reset_index()
avg_rating_df.rename(columns={'Rating': 'avg_rating'}, inplace=True)
popularity_df = num_rating_df.merge(avg_rating_df , on="course_title")
popularity_df=popularity_df[popularity_df['avg_rating']>=0.85].sort_values('avg_rating',ascending=False).head(10)
