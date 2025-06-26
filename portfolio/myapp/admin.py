from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'contactno', 'branch')  # columns to show
    search_fields = ('name', 'age', 'branch')        # search bar
    list_filter = ('age',)          # filter sidebar

admin.site.register(Student, StudentAdmin)

