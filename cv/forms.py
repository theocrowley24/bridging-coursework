from django import forms
from .models import Cv
from .models import Qualification
from .models import Experience

class EditForm(forms.ModelForm):

    class Meta:
        model = Cv
        fields = ('name', 'address', 'phoneNumber', 'emailAddress', 'aboutMe')

class AddQualification(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('name', 'startDate', 'endDate', 'description')

class AddExperience(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('name', 'startDate', 'endDate', 'description')