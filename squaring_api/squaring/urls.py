from django.urls import path
# from django.urls import path
from squaring.views import SquaringView, HelloWorldView, WelcomeView

urlpatterns = [
    path('<int:num>', SquaringView.as_view()),
    path('home', HelloWorldView.as_view()),
    path('', WelcomeView.as_view())
]