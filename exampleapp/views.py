# Create your views here.
from django.http import HttpResponse


def index_view(request):
    return HttpResponse("Voila!!! It worked!!!!")