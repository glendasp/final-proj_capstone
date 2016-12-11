from django.shortcuts import render

# Create your views here.
from mysite.questionsapp.models import Question


def home(request):
    if request.user.is_authenticated():
        queryset = Question.objects.all().order_by('-timestamp')
        context = {
            "queryset": queryset
        }
        return render(request, "questions/home.html", context)
    else:
        pass

