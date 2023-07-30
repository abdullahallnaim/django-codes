from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse('''
                        <h1>This is courses page</h1> 
                        <a href = '/second_app/feedback/'>Feedback </a>
                        <a href = '/first_app/about/'>About </a>
                        <a href = '/first_app/contact/'>Contact </a>
                        ''')
def feedback(request):
    return HttpResponse('''
                        <h1>This is feedback page</h1> 
                        <a href = '/second_app/courses/'>Courses </a>
                        <a href = '/first_app/about/'>About </a>
                        <a href = '/first_app/contact/'>Contact </a>
                        ''')