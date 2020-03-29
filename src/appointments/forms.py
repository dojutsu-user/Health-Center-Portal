from django import forms
from django.contrib.admin import widgets
from bootstrap_datepicker_plus import DateTimePickerInput
from django.utils import timezone

from appointments.models import Appointment
from doctor.models import Doctor


class AppointmentCreateForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            'doctor',
            'date_of_appointment',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_appointment'].widget = DateTimePickerInput()
        self.fields['date_of_appointment'].label = 'Select Preferred Date & Time'
        self.fields['date_of_appointment'].required = True
        self.fields['doctor'].widget.attrs.update({
            'class': 'tdl-new form-control mb-5',
        })

    def clean_date_of_appointment(self):
        data = self.cleaned_data['date_of_appointment']
        now = timezone.now()

        if not data > now:
            raise forms.ValidationError('Please select the correct values of date and time.')
        return data
