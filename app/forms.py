from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email Address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class PIModelForm(ModelForm):
    class Meta:
        model = PIModel
        fields = '__all__'
        exclude = ('model_pk', 'last_updated_on', 'last_updated_by', 'insourcing_overlap_perc',
                    'deployed_yes_or_no', 'deployed_on', 'total_savings_deployed', 
                    'sub_model_pk')
                        
    def __init__(self, *args, **kwargs):
        super(PIModelForm, self).__init__(*args, **kwargs)
        read_only_fields = []
        date_input_fields = []
        for field in iter(self.fields):
            if field in read_only_fields:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'readonly' : True,
                })
            elif field in date_input_fields:
                self.fields[field].widget = forms.DateInput(attrs={'type': 'date','class': 'form-control'})
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : field.replace('_',' ').title(),
                })
            choices_y_n = (
                ('Yes', 'Yes'),
                ('No', 'No'),
            )
            self.fields['insourcing_or_not'] = forms.ChoiceField(choices=choices_y_n,widget=forms.RadioSelect())

class PISubModelForm(ModelForm):
    class Meta:
        model = PISubModel
        fields = '__all__'
        exclude = ('model_pk', 'sub_model_pk', 'last_updated_on', 'last_updated_by', 'insourcing_overlap_perc',
                    'insourcing_comm_saved', 'insourcing_incremental_savings', 'opportunity_size'           
                    )
                        
    def __init__(self, *args, **kwargs):
        super(PISubModelForm, self).__init__(*args, **kwargs)
        print(self.fields)
        read_only_fields = []
        date_input_fields = []
        for field in iter(self.fields):
            if field in read_only_fields:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'readonly' : True,
                })
            elif field in date_input_fields:
                self.fields[field].widget = forms.DateInput(attrs={'type': 'date','class': 'form-control'})
            else:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder' : field.replace('_',' ').title(),
                })
            choices_code_type = (
                ('sql', 'sql'),
                ('python', 'python'),
            )
            self.fields['code_type'] = forms.ChoiceField(choices=choices_code_type,widget=forms.RadioSelect())
