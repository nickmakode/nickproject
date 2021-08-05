from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from web.models import BaseData


class BaseDataForm(forms.ModelForm):
    class Meta:
        model = BaseData
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError as e:
            raise ValidationError("Email already registered")
        else:
            return email

    def clean_number(self):
        number = self.cleaned_data['number']

        if len(str(number)) != 10:
            raise ValidationError("Kindly submit valid Mobile Number.")
        return number

    def clean_name(self):
        name = self.cleaned_data['name']
        print(name)

        if name == '' or name is None:
            raise ValidationError("please fill name")
        return name

    def clean_description(self):
        name = self.cleaned_data['description']

        if name == '' or name is None:
            raise ValidationError("please fill description")
        return name

