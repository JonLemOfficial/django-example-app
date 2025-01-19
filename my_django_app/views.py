from django.views import View
from django.shortcuts import render

class HomePageView(View):
  template_name = 'home-page.html'

  def get(self, *args, **kwargs):
    context = {
      'name': 'My Django App'
    }

    return render(self.request, self.template_name, context)
    