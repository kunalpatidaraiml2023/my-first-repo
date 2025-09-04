from django import forms
from .models import Student, Profile, Course

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'profile', 'courses']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

