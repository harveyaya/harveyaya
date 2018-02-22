from django.shortcuts import render

from django.views.generic import View
# Create your views here.

class diaryHomeView(View):
    template_name = "diary_home.html"
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
