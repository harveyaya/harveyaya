from django.shortcuts import render

from django.views.generic import View

class EnterPageView(View):
    template_name = "enter_page.html";
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

class HomePageView(View):
    template_name = 'external_homepage.html'
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)