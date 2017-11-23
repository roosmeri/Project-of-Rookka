from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, visitor. You're at the RookkaProject's index.")
