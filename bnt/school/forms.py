from django.forms import ModelForm, Textarea
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('student_first_name', 'student_last_name', 'student_mail', 'student_marks', 'student_address')
        widgets = {'student_address': Textarea(), }
        labels = {'student_first_name': ('First Name'), 'student_last_name': ('Last Name'), 'student_mail': ('Mail'),
                  'student_marks': ('Marks'), 'student_address': ('Address')}
