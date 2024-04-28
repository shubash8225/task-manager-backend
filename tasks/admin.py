from django.contrib import admin
from .models import Tasks
from .models import Category

# Register your models here.

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass