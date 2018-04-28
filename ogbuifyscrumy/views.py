# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import ScrumyUser, Role, ScrumyGoal,Task
from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import render

# Create your views here.
# @login_required
def index(request):
    mygoal= ScrumyGoal.objects.all()
    return HttpResponse(mygoal)

def move_goal(request, task_id):
    task = Task.objects.get(pk = task_id)
    return HttpResponse(task)

def add_user(request):
    try:
        user = ScrumyUser()
        role = Role.objects.get(id=1)
        user.name = "ogbuify markanthony"
        user.email = "ogbuifymark@gmail.com"
        user.password = "desmond"
        user.user_name = "ogbuify"
        user.role = role
        user.save()
    except:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)
        scrumy_user_list = ScrumyUser.objects.all()
        output = ', '.join([eachuser.user_name for eachuser in scrumy_user_list])
        return HttpResponse(output)


