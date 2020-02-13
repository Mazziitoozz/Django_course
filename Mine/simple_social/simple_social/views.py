from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "index.html"
class TestPage(TemplateView):
    template_name = "afterlogin.html"
class ThanksPage(TemplateView):
    template_name = "afterlogout.html"