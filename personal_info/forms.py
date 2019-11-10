from django import forms

from .models import PersonalInfo
from datetime import datetime, timedelta


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "email",
            "phone",
            "occupation",
            "name_of_employer",
            "job_title",
            "income",
            "sin_number"
        ]

    # def __init__(self, *args, **kwargs):
    #     super(PersonalInfoForm, self).__init__(*args, **kwargs)
    # #
    # def clean_first_name(self):
    #     if self.cleaned_data.get('first_name', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_last_name(self):
    #     if self.cleaned_data.get('last_name', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_date_of_birth(self):
    #     if self.cleaned_data.get('date_of_birth', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_email(self):
    #     if self.cleaned_data.get('email', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_phone(self):
    #     if self.cleaned_data.get('phone', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_occupation(self):
    #     if self.cleaned_data.get('occupation', '') == '':
    #         raise forms.ValidationError("Required filed")
    #
    #     return self.cleaned_data
    #
    # def clean_name_of_employer(self):
    #     if self.cleaned_data.get('name_of_employer', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_job_title(self):
    #     if self.cleaned_data.get('job_title', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_sin_number(self):
    #     if self.cleaned_data.get('sin_number', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean_income(self):
    #     if self.cleaned_data.get('income', '') == '':
    #         raise forms.ValidationError("Required filed")
    #     return self.cleaned_data
    #
    # def clean(self):
    #     super(PersonalInfoForm, self).clean()
    #     data = self.cleaned_data
    #     date_of_birth = data.get('date_of_birth', '')
    #     if not date_of_birth:
    #         self.add_error('date_of_birth', 'Required field')
    #     if datetime.strptime(date_of_birth, '%Y-%m-%d') - datetime.today() < timedelta(days= 365 * 18):
    #         self.add_error('date_of_birth', 'Must be older than 18-year-old')
    #
    #     return self.cleaned_data
