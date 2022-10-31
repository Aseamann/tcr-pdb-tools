from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from app.forms import PdbToolsForm, PostPdbForm
from PDBS.process_pdb_request import *


def home_redirect_view(request):
    return redirect("pdb_form")


def pdb_tools_view(request):
    form = PdbToolsForm()
    form_class = PostPdbForm
    context = {"form": form, "title": "PDB Form"}
    theme = getattr(settings, "MARTOR_THEME", "bootstrap")
    return render(request, "%s/form.html" % theme, context)


def post_pdb_view(request):
    if request.method == "POST":
        form = PdbToolsForm(request.POST)
        if form.is_valid():
            pdb = request.POST.get('pdb')
            actions = [request.POST.get('action1'), request.POST.get('action2'), request.POST.get('action3')]
            context = {"pdb": pdb, "actions": actions}
            pdb_loc = process_modification(context)

            with open(pdb_loc, "r") as f:
                data = f.read()
            response = HttpResponse(data)
            response['Content-Disposition'] = ('attachment; filename="%s"' % (pdb + ".pdb"))
            return response
        else:
            form = PdbToolsForm()
        context = {"form": form, "title": "Post Pdb"}
        theme = getattr(settings, "MARTOR_THEME", "bootstrap")
        return render(request, "%s/form.html" % theme, context)
