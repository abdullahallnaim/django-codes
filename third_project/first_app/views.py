from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, './first_app/index.html', {"name" : "I am Rahim", "marks" : 86, "lst" : [24,3,10,5], "blog" : "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Harum quae tempora fugit laborum voluptas mollitia. Explicabo earum assumenda obcaecati et.", "courses" : [
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