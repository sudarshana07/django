from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group

from .models import Student, Management, Testimonial

# Register your models here.


AdminSite.site_header = "B&T Administration"
AdminSite.site_title = "admin"
AdminSite.index_title = "Student Administration"


def mark_as_topper(modeladmin, request, queryset):
    queryset.update(status='T')


mark_as_topper.short_description = 'Mark as Topper'


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [('Name Info:', {'fields': ['student_first_name', 'student_last_name']}),
                 ('Other Info:', {'fields': ['student_mail', 'student_marks', 'student_address']}), ]

    list_filter = ['student_marks']

    search_fields = ['student_mail', 'student_first_name']

    actions = [mark_as_topper]

    list_display = ['student_first_name', 'student_last_name', 'student_mail', 'student_marks', 'student_address']


class ManagementAdmin(admin.ModelAdmin):
    fields = ['name', 'designation', 'photo']
    list_display = ['name', 'designation']


class TestimonialAdmin(admin.ModelAdmin):
    fields = ['testimonial_name', 'posted_on', 'testimonial_text', 'photo']
    list_display = ['testimonial_name', 'posted_on', 'testimonial_text']


admin.site.register(Student, StudentAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
