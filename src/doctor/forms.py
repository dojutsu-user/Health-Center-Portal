from django import forms

from doctor.models import Doctor


class DoctorUpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ('image', 'name', 'about', 'education', 'available_description')

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
