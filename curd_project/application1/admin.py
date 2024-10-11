from django.contrib import admin
from application1.models import stumodel

class stumoed_admin(admin.ModelAdmin):
  list_display=['first_name','last_name','country']
admin.site.register(stumodel,stumoed_admin)
