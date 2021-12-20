from django.contrib import admin

# Register your models here.
from main.models import Semester, Subject, Student, Teacher

admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
