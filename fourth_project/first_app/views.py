from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, './first_app/home.html', {"name" : "I am Rahim", "marks" : 86,"courses" : [
        {
        "id" : 1,
        "course" : "C",
        "teacher" : "Rahim"
        },
        {
        "id" : 2,
        "course" : "C++",
        "teacher" : "Kahim"
        },
        {
        "id" : 3,
        "course" : "Python",
        "teacher" : "Fahim"
        },
        ]})
    
def about(request):
    return render(request, './first_app/about.html', {'author' : 'glenn maxwell'})