from django.http import HttpResponse
from django.views.generic.simple import direct_to_template 
from models import *
def index(request):
    return direct_to_template(request, "index.html")
    
def check_answer(request, question, answer):
    if answer == right_answers[question]:
        return direct_to_template(request, "right.html")
    else:
        return direct_to_template(request, "wrong.html")