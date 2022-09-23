from django.contrib import admin
# Register your models here.
from .models import Question, Choice, Vote


class ChoiceInline(admin.TabularInline):
    """Choice model of admin."""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Question model for admin."""

    fieldsets = [
        (None,{'fields': ['question_text']}),
        ('Date information',
        {'fields': ['pub_date', 'end_date'], 'classes': ['collapse']}
        ),
    ]
    inlines = [ChoiceInline]
    list_display = (
        'question_text',
        'pub_date',
        'was_published_recently',
        'is_published',
        'can_vote'
    )
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.site_header = "KU Poll Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the KU Poll Admin Area"


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)

