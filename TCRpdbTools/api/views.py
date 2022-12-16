from django.shortcuts import render
import urllib.parse
from api.controllers import PDB_URL


# Create your views here.
def index(request):
    return render(request, 'index.html')


def pdbviewer(request):
    # if request.GET.get('pdb', None):
    #     pdbfile_url = urllib.parse.unquote(request.GET.get('pdb', None))
    # else:
    # try:
    #     pdbfile_url = urllib.parse.unquote(request.GET.get('pdb', None))
    # except:
    pdbfile_url = "../static/PDBS/1ao7.pdb"
    return render(request, 'pdbviewer.html', {"pdb": pdbfile_url})
