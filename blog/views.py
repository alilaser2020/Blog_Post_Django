from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    A class view for home page of site
    """
    template_name = 'home.html'
