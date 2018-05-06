# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import ScrumyUser, Role, ScrumyGoal,Task,GoalStatus
from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import render
from .forms import AddUser,AddTask

# Create your views here.
# @login_required
def index(request,template_name='index.html'):
    try:
        users_list = ScrumyUser.objects.all()
    except BaseException as e:
        raise e

    try:
        for i in range(1, len(users_list)):
            user = ScrumyUser.objects.get(id = i)
    except BaseException as e:
        raise e
        #     lab 13

    user_scrummy = users_list[0]
    status = GoalStatus.objects.get(status="weekly target")
    goals = user_scrummy.scrumygoal_set.filter(status_id =status.id)
    return render(request, template_name, {'goals':goals})


def move_goal(request, task_id):
    task = Task.objects.get(pk = task_id)
    return HttpResponse(task)

# def add_user(request):
#     try:
#         user = ScrumyUser()
#         role = Role.objects.get(id=1)
#         user.name = "ogbuify markanthony"
#         user.email = "ogbuifymark@gmail.com"
#         user.password = "desmond"
#         user.user_name = "ogbuify"
#         user.role = role
#         user.save()
#     except:
#         transaction.rollback()
#         raise
#     else:
#         transaction.commit()
#     finally:
#         transaction.set_autocommit(True)
#         scrumy_user_list = ScrumyUser.objects.all()
#         output = ', '.join([eachuser.user_name for eachuser in scrumy_user_list])
#         return HttpResponse(output)


def add_user(request,template_name="add_user.html"):
    roles = Role.objects.all()
    if request.method == 'POST':
        add_user_form = AddUser(request.POST)
        if add_user_form.is_valid():
            add_user_form.save()
            users = ScrumyUser.objects.all()
            return render(request, template_name, {'msg': "User created successfully",'scrumy_users':users,'roles':roles})
        else:
            users = ScrumyUser.objects.all()
            return render(request, template_name, {'form':add_user_form, 'scrumy_users': users,'roles':roles})

    else:
        users=ScrumyUser.objects.all()

        return render(request, template_name,{'scrumy_users':users,'roles':roles})

def add_task(request,template_name="add_task.html"):

    if request.method == 'POST':
        add_task_form = AddTask(request.POST)
        if add_task_form.is_valid():
            user=ScrumyUser.objects.get(pk=1)
            new_task=add_task_form.save(commit=False)
            new_task.created_by=user
            new_task.save()
            tasks = Task.objects.all()
            return render(request, template_name,
                          {'msg': "Task created successfully", 'tasks': tasks,})
        else:
            tasks = Task.objects.all()
            return render(request, template_name, {'form': add_task_form, 'tasks': tasks})

    else:
        tasks = Task.objects.all()
        return render(request, template_name, {'tasks': tasks})

def edit_task(request,task_id,template_name="edit_task.html"):

    if request.method == 'POST':
        task_update = Task.objects.get(pk=task_id)
        add_task_form = AddTask(request.POST,instance=task_update)
        if add_task_form.is_valid():
            add_task_form.save()
            tasks = Task.objects.all()
            return render(request,"add_task.html",
                          {'msg': "Task updated successfully", 'tasks': tasks,})
        else:
            task = Task.objects.get(pk=task_id)
            return render(request, template_name, {'form': add_task_form, 'tasks': task})

    else:
        task = Task.objects.get(pk=task_id)
        return render(request, template_name, {'task': task,'task_id':task_id})
