from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class SquaringView(View):
    def get(self, request, num):
        return HttpResponse(int(num) ** 2)


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello World')

class WelcomeView(View):
    def get(self, request):
        return HttpResponse ('Welcome to the squaring app home page')
