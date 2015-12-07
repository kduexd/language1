# -*- coding: UTF-8 -*- 
from django.shortcuts import render
import datetime

def main(request):
    now=datetime.datetime.now()
    context = {'message':'Django 很棒','now':now}
    return render (request, 'main/main.html' ,  context)