from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'short_description']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Make 'salary' and 'designation' read-only when editing an existing employee
            self.fields['salary'].disabled = True
            self.fields['designation'].disabled = True