# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ScrumyUser, Role, ScrumyGoal,GoalStatus
# Register your models here.

admin.site.register(ScrumyUser)
admin.site.register(Role)
admin.site.register(ScrumyGoal)
admin.site.register(GoalStatus)

