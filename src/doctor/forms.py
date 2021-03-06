"""Forms related to doctor app."""

from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from doctor.models import Doctor


class DoctorUpdateProfileForm(forms.ModelForm):

    """Update form for doctors."""

    class Meta:
        model = Doctor
        fields = (
            'image',
            'name',
            'about',
            'education',
            'available_description'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'tdl-new form-control'
        })
        self.fields['about'].widget.attrs.update({
            'class': 'tdl-new form-control edit-profile-textarea'
        })
        self.fields['education'].widget.attrs.update({
            'class': 'tdl-new form-control edit-profile-textarea',
        })
        self.fields['available_description'].widget.attrs.update({
            'class': 'tdl-new form-control edit-profile-textarea'
        })


class CustomPasswordChangeForm(PasswordChangeForm):

    """Password change form for doctors."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({
            'class': 'tdl-new form-control',
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'tdl-new form-control',
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'tdl-new form-control',
        })
