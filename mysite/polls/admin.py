from django.contrib import admin
# Register your models here.
from .models import Question, Choice, Vote
  
# admin.site.register(Question)
# admin.site.register(Choice)
  
admin.site.site_header = "KU Poll Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the KU Poll Admin Area"
  
  
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)

