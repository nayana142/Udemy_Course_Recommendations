from django.shortcuts import render
from .models import Course
import pandas as pd

# Data Preprocessing
def preprocess_data(df):
    df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
    return df

# def homepage(request):
#     return render(request, 'search.html')

# Model Building
def recommend_courses(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        df = pd.read_csv('udemy_courses.csv.xls')
        df = preprocess_data(df)
        filtered_df = df[df['subject'] == subject]
        results = filtered_df[['course_title', 'url', 'price']].values.tolist()
        return render(request, 'recommendation.html', {'results': results})
    else:
        return render(request, 'search.html')