from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.


@api_view
def get_default_view(request):
    if request.method == "GET":
        pass
