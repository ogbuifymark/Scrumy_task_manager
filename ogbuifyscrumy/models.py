# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class GoalStatus (models.Model):
    status=models.TextField(null=False)


    def __repr__(self):
        return '<Status %r>' % self.status
class Role(models.Model):
    name = models.CharField(max_length=200)

class ScrumyUser(models.Model):
    name = models.CharField(max_length=200)
    email=models.TextField(blank=False, default='ogbuifymark@gmail.com')
    user_name=models.TextField(null=False,default='mark')
    password = models.TextField(null=False, default='1234')
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)

class Task(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.ForeignKey(ScrumyUser, on_delete=models.CASCADE)


class ScrumyGoal(models.Model):
    user_id=models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)
    status_id=models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_on = models.DateTimeField(null=True)
    description = models.TextField(default="")
