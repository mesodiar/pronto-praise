from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from praises.models import Praise


class PraiseListView(TemplateView):
    template_name = 'praises.html'

    def get(self, request):
        return render(
            request,
            self.template_name
        )


class PraiseAddView(TemplateView):
    template_name = 'praise_add.html'

    def get(self, request):
        return render(
            request,
            self.template_name
        )


class PraiseAddHeart(TemplateView):
    def get(self, request, praise_id):
        praise = Praise.objects.get(id=praise_id)
        praise.number_of_hearts = praise.number_of_hearts+1
        praise.save()
        return redirect('/')
