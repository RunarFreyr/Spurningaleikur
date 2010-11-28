from django.http import HttpResponse
from django.views.generic.simple import direct_to_template 

def index(request):
    return direct_to_template(request, "index.html")
    
def check_answer(request, question, answer):
    right_answers = {
        "1":"d",
        "2":"d",
        "3":"d",
        "4":"b",
        "5":"c",
        "6":"a"
    }
    if answer == right_answers[question]:
        return direct_to_template(request, "right.html")
    else:
        return direct_to_template(request, "wrong.html")