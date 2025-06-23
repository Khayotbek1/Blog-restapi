from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ArticleCreate.as_view()),
    path('all/', ArticleListAPIView.as_view()),
    path('my/', MyArticleListAPIView.as_view()),
    path('tags/', TagCreateList.as_view()),
    path('<slug:slug>/', ArticleRetrieveAPIView.as_view()),

]
