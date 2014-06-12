from django.contrib import admin

from .models import Seed, Question, Reply


admin.site.register(Seed)
admin.site.register(Question)
admin.site.register(Reply)
