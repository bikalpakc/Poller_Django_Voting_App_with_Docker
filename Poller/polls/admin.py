from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['publish_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choices)
admin.site.register(Question, QuestionAdmin)