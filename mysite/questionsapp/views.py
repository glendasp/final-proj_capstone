from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import Question, Answer, IdealAnswer
from .forms import UsersAnsform


def home(request):
    if request.user.is_authenticated():
        form = UsersAnsform(request.POST or None)
        # check if it is valid if so get response from the form
        if form.is_valid():
            print(form.cleaned_data)
            # getting the questions and answers
            question_id = form.cleaned_data.get('question_id')  # form.cleaned_data['question_id']
            answer_id = form.cleaned_data.get('answer_id')
            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)
            print(answer_instance.text, question_instance.text)

            question_id = form.cleaned_data['question_id']
        queryset = Question.objects.all().order_by('-date_created')
        print(queryset)  # for debugging
        instance = queryset[0]
        print(instance)  # for debugging
        context = {
            "form": form,
            "instance": instance,
            # "queryset": queryset

        }
        return render(request, "questions/home.html", context)
    else:
        raise Http404


# Adicionando id
# id esta relacionado com a intance que vou precisar trabalhar depois
def Quiz(request, id):
    print(id)
    # Se não encontrar pergunta mostra pag de erro
    # try:
    #     instance = Question.object.get(id=id)
    # except:
    #     raise Http404
    # instance = Question.object.get(id=id)

    if request.user.is_authenticated():
        queryset = Question.objects.all().order_by('-date_created')
        print(queryset)  # for debugging
        instance = get_object_or_404(Question, id=id)
        print(instance)  # for debugging
        form = UsersAnsform(request.POST or None)

        try:
            user_answer = IdealAnswer.objects.get(user=request.user, question=instance)
            updated_q = True
        except IdealAnswer.DoesNotExist:
            user_answer = IdealAnswer()
            updated_q = False
        except IdealAnswer.MultipleObjectsReturned:
            user_answer = IdealAnswer.objects.filter(user=request.user, question=instance)[0]
            updated_q = True
        except:
            user_answer = IdealAnswer()
            updated_q = False

        form = UsersAnsform(request.POST or None)

        # check if it is valid if so get response from the form
        if form.is_valid():
            print(form.cleaned_data)
            # getting the questions and answers

            question_id = form.cleaned_data.get('question_id')  # form.cleaned_data['question_id']

            answer_id = form.cleaned_data.get('answer_id')
            importance_level = form.cleaned_data.get('importance_level')

            their_importance_level = form.cleaned_data.get('their_importance_level')
            their_answer_id = form.cleaned_data.get('their_answer_id')

            question_instance = Question.objects.get(id=question_id)
            answer_instance = Answer.objects.get(id=answer_id)

            # creating instance
            user_answer.user = request.user
            user_answer.question = question_instance
            user_answer.my_answer = answer_instance
            user_answer.my_answer_importance = importance_level

            # question_id = form.cleaned_data['question_id']

            if their_answer_id != -1:
                their_answer_istance = Answer.objects.get(id=their_answer_id)
                user_answer.their_answer = their_answer_istance
                user_answer.their_importance = their_importance_level
            else:
                user_answer.their_answer = None
                user_answer.their_importance = "Not Important"
            user_answer.save()

            user_matches_update.send(user=request.user, sender=user_answer.__class__)

            if updated_q:
                messages.success(request, "Your response was updated successfully.<br/><a href='#'>Hello</a>",
                                 extra_tags='safe updated')

            else:
                messages.success(request, "Your response was saved successfully.")

            next_q = Question.objects.get_unanswered(request.user).order_by("?")
            if next_q.count() > 0:
                next_q_instance = next_q.first()
                return redirect("question_single", id=next_q_instance.id)
            else:
                return redirect("home")

        # queryset = Question.objects.all().order_by('-date_created')
        #     print(queryset)  # for debugging
        #     instance = Question.object.get(id=id)
        #     print(instance)  # for debugging
        context = {
            "form": form,
            "instance": instance,
            "user_answer": user_answer,
            # "queryset": queryset
        }


        return render(request, "questions/quiz.html", context)
    else:
        raise Http404

