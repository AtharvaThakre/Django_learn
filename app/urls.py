from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello_world_view, name = "hello_world"),
    path("", views.hello_py_view, name = "heypy"),
    path("htmlrender", views.hello_html, name = "hello_html"),
    path("special", views.special, name = "special"),
    path("helloname/<str:name>", views.hello_name, name = "hello_name"),
    path("sum/<int:num1>/<int:num2>", views.sum, name = "sum"),
    path("query", views.query, name = "query"),
]