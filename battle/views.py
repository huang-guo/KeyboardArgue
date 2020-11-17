from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DateDetailView, DetailView, ListView
from battle.models import Battle


# Create your views here.
@login_required(login_url='login')
def index_view(request):
    return HttpResponse("<h1>欢迎光临</h1>")


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BattleListView(CommonViewMixin, ListView):
    template_name = "battle/battle_list.html"
    model = Battle


class BattleDetailView(CommonViewMixin, DetailView):
    template_name = "battle/battle_detail.html"
    pk_url_kwarg = "pk"
    context_object_name = "battle"
    model = Battle
