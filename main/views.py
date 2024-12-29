from django.shortcuts import render
from .models import Education, Experience, TechnicalSkill, Project

def home(request):
    # Technical Skills
    technical_skills = [
        {
            'category': 'Computer Vision',
            'skills': 'Python, OpenCV, YoloV4'
        },
        {
            'category': 'Data Science',
            'skills': 'Python, PowerBI, Selenium, Streamlit, SQL'
        }
    ]

    # Experience
    experience = [
        {
            'position': 'Summer Intern',
            'company': 'Olgu Yönetim Bilişim Sistemleri',
            'location': 'Izmir, Turkey, Remote',
            'start_date': '2023-10-01',
            'end_date': '2023-11-01',
            'description': 'During this internship, an autonomous web scraping project was developed. Product information, price and photo were taken from a clothing company\'s website and saved as a json file.'
        },
        {
            'position': 'Bootcamp Participant',
            'company': 'Veri Bilimi Okulu',
            'location': 'Istanbul, Turkey, Remote',
            'start_date': '2022-02-01',
            'end_date': '2022-06-01',
            'description': 'During this bootcamp, real-time topics in the field of machine learning and data science were examined in detail, and many projects and homework projects were carried out.'
        },
        {
            'position': 'Software Team Member',
            'company': 'BEU Otomasyon And R&D Team',
            'location': 'Zonguldak, Turkey, Remote',
            'start_date': '2021-11-01',
            'end_date': '2022-02-01',
            'description': 'I was assigned to develop a traffic sign recognition application with YoloV4 function using OpenCV.'
        }
    ]

    # Projects
    projects = [
        {
            'title': 'Face Recognition System',
            'description': 'Designed a feature-based object detection algorithm using Haar Cascade to detect objects from images. The system can effectively recognize and track faces in real-time using computer vision techniques.',
            'technologies': 'Python, OpenCV, Haar Cascade',
            'date': '2023-07-01'
        },
        {
            'title': 'Object Distance Measurement',
            'description': 'Developed a computer vision application that calculates the distance of objects shown to the camera in real-time. The system uses camera calibration and geometric calculations for accurate measurements.',
            'technologies': 'Python, OpenCV',
            'date': '2023-06-01'
        },
        {
            'title': 'CRM Analytics',
            'description': 'RFM with Flo data review, Cohort and RFM metrics analysis. Calculation of CLTV value.',
            'technologies': 'Python, Data Analysis',
            'date': '2023-01-01'
        },
        {
            'title': 'Measurement Problems',
            'description': 'Examination of smokers with AB Testing (Independent Two Sample T-Test)',
            'technologies': 'Python, Statistical Analysis',
            'date': '2023-01-01'
        },
        {
            'title': 'Recommended Systems',
            'description': 'ARL (Association Rule Learning), content-based, item-based and user-based recommendation applications with online retail dataset.',
            'technologies': 'Python, Machine Learning',
            'date': '2023-01-01'
        },
        {
            'title': 'Feature Engineering',
            'description': 'Examining data, removing or deleting features, examining outliers, LOF analysis, One Hot Encoding, Standard Scaler functions.',
            'technologies': 'Python, Data Engineering',
            'date': '2023-01-01'
        },
        {
            'title': 'Machine Learning',
            'description': 'Random Forests, GBM, LightGBM, CatBoost, CART, Logistic Regression, KNN, Linear Regression with Unsupervised Learning applications.',
            'technologies': 'Python, Machine Learning',
            'date': '2023-01-01'
        },
        {
            'title': 'Graduation Project',
            'description': 'The graduation project was carried out by classifying real Amazon product reviews as positive and negative. The data containing the comments were pre-processed, and unnecessary and empty comments were deleted. Later, unnecessary words in the comments were deleted. Then the machine learning CNN model was prepared for training. The model was able to classify comments as positive and negative with 88% accuracy.',
            'technologies': 'Python, Deep Learning, NLP',
            'date': '2023-06-01'
        }
    ]

    context = {
        'technical_skills': technical_skills,
        'experience': experience,
        'projects': projects,
    }
    return render(request, 'main/home.html', context) 