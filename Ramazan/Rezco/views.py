from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def tam (request, name, age, interest):
    return HttpResponse(f'{name}. {age} Лет. {interest}.')
def tyt (request, gor, iop, op):
    return HttpResponse(f'{gor}.{iop}.{op}')
def kak (request, number):
    return HttpResponse(f'мои контакты: {number}')

