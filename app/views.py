from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def hello_world_view(request):
    return HttpResponse("hello world")

def hello_py_view(request):
    return HttpResponse("heyy Pythonn")

def hello_html(request):
    return render(request, "app/hello.html")

def hello_name(request, name):
    return HttpResponse(f"Hello {name}")

def sum(request, num1, num2):
    return HttpResponse(f"Sum is {num1 + num2}!")

def query(request):
    return HttpResponse(f"Your query is {request.GET.get("q")}!")

def special(request):
    return redirect(hello_html)