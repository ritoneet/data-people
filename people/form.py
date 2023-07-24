from django import forms
from people.models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = (
            'name',
            'age',
            'city',
            'salary',
            'business',
        )