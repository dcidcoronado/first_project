from django.shortcuts import render, HttpResponse, redirect
def root(request):
    return redirect ("/blogs")


def index(request):
    respuesta = "placeholder para luego mostrar una lista de todos los blogs"
    return HttpResponse(respuesta)


def new(request):
    respuesta = "placeholder para mostrar un nuevo formulario para crear un nuevo blog"
    return HttpResponse(respuesta)


def create(request):
    return redirect ("/")


def show(request, number):
    respuesta = f"placeholder para mostrar el blog numero: {number}"
    return HttpResponse(respuesta)


def edit(request, number):
    respuesta = f"placeholder para editar el blog {number}"
    return HttpResponse(respuesta)

def destroy(request, number):
    return redirect ("/blogs")





# def edad(request, name, age):
#     agemayor = str(age + 1)
#     respuesta = name + " tiene " + agemayor + " años"
#     return HttpResponse(respuesta)

# Create your views here.
