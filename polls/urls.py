from django.urls import path
from polls import views
app_name = 'polls'
urlpatterns = [
    path('json/', views.Question_json, name='json'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('json/', views.vote, name='vote'),
]

'''urlpatterns = [
    path('polls/', views.Question_list),
    path('polls/<int:pk>/', views.Question_detail),
]'''
