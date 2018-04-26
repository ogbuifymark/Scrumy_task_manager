# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import ScrumyUser, Role, ScrumyGoal
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# @login_required
def index(request):
    mygoal= ScrumyGoal.objects.all()
    return HttpResponse(mygoal)