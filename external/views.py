from django.shortcuts import render

from django.views.generic import View
from django.http import FileResponse, HttpResponse

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

class ResumePDFVIew(View):
    def get(self,request):
        return self.pdf_view(request)

    def pdf_view(self, request):
        return FileResponse(open("./site_static/res/Yu_Hou_Resume.pdf", "r"), content_type='application/pdf')