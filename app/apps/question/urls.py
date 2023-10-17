from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='questionList'),
    path('create', views.QuestionCreate, name='questionCreate'),
    path('<slug:slug>', views.QuestionDetailView.as_view(), name='questionView'),
    path('edit/<slug:slug>', views.QuestionUpdate.as_view(), name='questionEdit'),
    path('delete/<slug:slug>', views.QuestionDelete.as_view(), name='questionDelete'),

]