from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/post_list.html', {})
