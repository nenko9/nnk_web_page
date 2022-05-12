from django.shortcuts import render
from django.views import View
import django.contrib.staticfiles 

# Create your views here.
class MainView(View):
    def get(self, request):
        page_template='dj_app/main.html'
        page_context={}
        return render(request,page_template, page_context)