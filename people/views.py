from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView

from people.models import People
from people.form import PeopleForm


# def index_view(request):
#     return render(request, "home.html")


class HomePeopleView(TemplateView):
    template_name = "home.html"


# def people_list(request):
#     rates = People.objects.all()
#     text = {"people_list": rates}
#     return render(request, "list-people.html", context=text)

class ListPeopleView(ListView):
    model = People
    template_name = "list-people.html"


# def people_rate(request):
#     form = PeopleForm()
#     if request.method == "POST":
#         form = PeopleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/list-people/")
#     elif request.method == "GET":
#         form = PeopleForm()
#     text = {"form": form}
#     return render(request, "Rate_create.html", context=text)

class RatePeopleView(CreateView):
    form_class = PeopleForm
    success_url = reverse_lazy("people-list-link")
    model = People
    template_name = "Rate_create.html"


# def people_details(request, pk):
#     people = get_object_or_404(People, id=pk)
#
#     text = {
#         "object": people,
#     }
#     return render(request, "people_details.html", context=text)
class DetailsPeopleView(DetailView):
    model = People
    template_name = "people_details.html"


# def people_update(request, pk):
#     people = get_object_or_404(People, id=pk)
#     if request.method == "POST":
#         form = PeopleForm(request.POST, instance=people)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/list-people/")
#     elif request.method == "GET":
#         form = PeopleForm(instance=people)
#     text = {"form": form}
#     return render(request, "people_update.html", context=text)

class UpdatePeopleView(UpdateView):
    form_class = PeopleForm
    success_url = reverse_lazy("people-list-link")
    model = People
    template_name = "people_update.html"


# def people_delete(request, pk):
#     people = get_object_or_404(People, id=pk)
#     if request.method == "POST":
#         people.delete()
#         return HttpResponseRedirect("/list-people/")
#     text = {
#         "object": people,
#     }
#     return render(request, "people_delete.html", context=text)

class DeletePeopleView(DeleteView):
    success_url = reverse_lazy("people-list-link")
    model = People
    template_name = "people_delete.html"
