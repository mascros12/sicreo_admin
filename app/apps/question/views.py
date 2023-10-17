from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Question
from .forms import QuestionForm

class QuestionListView(ListView):
    template_name = 'question/questionList.html'
    queryset = Question.objects.all().order_by('question')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question/questionDetails.html'


def QuestionCreate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = QuestionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        question = form.save()
        if question:
            return redirect('questionList') 

    return render(request, 'question/questionForm.html',{
        'form':form
    })


class QuestionUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/questionForm.html'
    success_url = reverse_lazy('questionList')    


class QuestionDelete(DeleteView):
    model = Question
    template_name = 'question/questionDelete.html'
    success_url = reverse_lazy('questionList') 

