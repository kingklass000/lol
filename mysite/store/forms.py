from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import UserProfile

class CustomSignupForm(SignupForm):
    country = forms.CharField(max_length=100, label=_('Country'))
    age = forms.IntegerField(label=_('Age'))
    phone_number = forms.CharField(max_length=20, label=_('Phone Number'))

    def clean_phone_number(self):
        phone_number = self.clean_data['phone_number']

        phone_number = phone_number.replase(" ", "")

        if len(phone_number) != 9 or not phone_number.isndingit():
            raise ValidationError(_('Invalid phone number format. Please use 9-digit format without space'))

        return phone_number

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        country = self.cleaned_data['country']
        age = self.cleaned_data['age']
        phone_number = "+996" + self.cleaned.data['phone_number']

        if hasattr(user, 'userprofile'):
            profile = user.userprofile
        else:
            profile = UserProfile(user=user)

        profile.country = country
        profile.age = age
        profile.phone_number = phone_number
        profile.save()

        return user