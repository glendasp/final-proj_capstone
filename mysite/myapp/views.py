from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from questionsapp.models import Question
from .models import SignUp
from .forms import ContactForm, SignUpForm


# from questionsapp.models import Question



# Create your views here.
def home(request):
    # Setting contents to my html doc
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    # if request.user.is_authenticated():
    #     title = "Welcome %s" %(request.user)

    context = {
        "title": title,
        "form": form
    }

    # Validating
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you",
            # "form": form
        }

    '''
    Check if user is authenticated and if user is a stuff member
    If authenticated, it will take user to a


    https://docs.djangoproject.com/en/1.10/ref/models/querysets/
    '''

    if request.user.is_authenticated():  # and request.user.is_staff:
        queryset = Question.objects.all()  # .filter(full_name__iexact="Glendex")
        # print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
        context = {
            "queryset": queryset
        }
        return render(request, "questions/quiz.html", context)

    return render(request, "quiz.html", context)


# For contact form
def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        # 	print key, value
        # 	#print form.cleaned_data.get(key)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        print(form_email, form_message, form_full_name)

        # # setting up email part ----- todo --> note to myself: finish this on second phase of the project
        # subject = 'Site contact form'
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [from_email, 'glendasp@gmail.com']
        # contact_message = "%s: %s via %s" % (
        #     form_full_name,
        #     form_message,
        #     form_email)
        # some_html_message = """<h1>hello world</h1>"""
        # send_mail(subject,
        #           contact_message,
        #           from_email,
        #           to_email,
        #           html_message=some_html_message,
        #           fail_silently=True)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)
