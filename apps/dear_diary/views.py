from django.shortcuts import render

from django.views.generic import View
# Create your views here.

class diaryHomeView(View):
    template_name = "diary_home.html"
    breadcrumb = {"pageName": "Dear Diary", "pageURL": 'dear_diary'}
    def get(self, request):
        context = {"breadcrumb": self.breadcrumb}
        print(context)
        return render(request, self.template_name, context)
