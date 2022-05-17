from django.contrib import admin

from product.models import  User, Quiz, Question, Answer, Result

class Answer_admin(admin.TabularInline):
    model = Answer

class Question_admin(admin.ModelAdmin):
    inlines = [Answer_admin]

admin.site.register(User)

admin.site.register(Quiz)
admin.site.register(Question,Question_admin)
admin.site.register(Answer)
admin.site.register(Result)
