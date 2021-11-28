from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from markdown2 import Markdown
from django import forms
from django.urls import reverse
import random

from . import util


class NewEntryForm(forms.Form):
    title = forms.CharField(
        label="Entry Title",
        widget=forms.TextInput(attrs={"class": "form-control col-md-8 col-lg-8 mb-4"}),
    )
    contents = forms.CharField(
        label="Contents",
        widget=forms.Textarea(
            attrs={"class": "form-control col-md-8 col-lg-8", "rows": 10}
        ),
    )


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, entry):
    if util.get_entry(entry):
        markdowner = Markdown()
        content = markdowner.convert(util.get_entry(entry))
    else:
        content = "<h1>Error: Entry Does Not Exist</h1>"

    return render(
        request,
        "encyclopedia/test.html",
        {"content": content, "entry": entry},
    )


def create_entry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            util.save_entry(form.cleaned_data["title"], form.cleaned_data["contents"])
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, "encyclopedia/add.html", {"form": form})
    return render(request, "encyclopedia/add.html", {"form": NewEntryForm()})


def random_entry(request):
    entries = util.list_entries()
    selected_entry = random.choice(entries)
    return redirect("encyclopedia:entry", entry=selected_entry)

def search(request):
    pass