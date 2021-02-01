from django.contrib import admin
from .models import Student, Course, Enrollment, User, Teacher, Teach


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Teach)
admin.site.register(Enrollment)
