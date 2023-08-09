from django import forms

from .models import DBC, DBG, DBGC
# from functools import partial
from datetime import datetime, timedelta



# DateInput = partial(forms.DateInput, {'class': 'datepicker'})

# class DateRangeForm(forms.Form):
#     # startDate = forms.DateField(widget=DateInput())
#     # endDate = forms.DateField(widget=DateInput())
#     startDate = forms.DateField(label='Дата начала', widget=forms.DateInput(attrs={'type': 'date', 'class':'daterange', 'id': 'daterange','value': datetime.datetime.now().strftime("%d-%m-%Y")}))
#     endDate = forms.DateField(label='Дата конца', widget=forms.DateInput(attrs={'type': 'date', 'class':'daterange', 'id': 'daterange','value': datetime.datetime.now().strftime("%d-%m-%Y")}))
#     # startDate = forms.DateField()
#     # startDate = forms.DateField(label='Дата начала', widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), required=False)
#     # endDate = forms.DateField(label='Дата конца', widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), required=False)
#     # startDate = forms.DateField(label='Дата начала', widget=forms.DateInput(attrs={'type': 'date', 'value': datetime.datetime.now().strftime("%d-%m-%Y")}), required=False)
#     # endDate = forms.DateField(label='Дата конца', widget=forms.DateInput(attrs={'type': 'date', 'value': datetime.datetime.now().strftime("%d-%m-%Y")}), required=False)

# class DatePickerForm( forms.Form):
#     date_range_picker = forms.CharField()

def current_date():
    # return datetime.date(year=datetime.today.year, month=datetime.today.month, day=datetime.today.day)
    return datetime.now()



class FormDateRange(forms.Form):
    date_range_start = forms.DateField(label='Дата начала', initial=current_date, widget=forms.DateInput(attrs={'type':'date',}))
    # date_range_stop = forms.DateField(label='Дата конца', widget=forms.DateInput(attrs=dict(type='date')))
    date_range_stop = forms.DateField(label='Дата конца', initial=current_date, widget=forms.DateInput(attrs={'type':'date',}))

class CheckFieldsDBIC( forms.Form):
    check_current = forms.BooleanField(required=False, label='ток', widget=forms.CheckboxInput())
    check_powerP = forms.BooleanField(required=False, label='мощностьР',  widget=forms.CheckboxInput())
    check_powerQ = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    check_powerS = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    check_cos = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    check_tarif = forms.BooleanField(required=False, widget=forms.CheckboxInput())

class CheckCounter(forms.Form):
    check_nameCounter = forms.ModelChoiceField(empty_label=None, queryset=DBC.objects.all())

class DBCForm(forms.ModelForm):
    class Meta:
        model = DBC
        # fields = '__all__'
        # fields = ['name_counter_full', 'group', 'schem', 'net_adress']
        fields = [
    'name_counter_full' ,
    'schem' ,
    'group',
    'net_adress' ,
    'manuf_number' ,
    'manuf_data' ,
    'klass_react' ,
    'klass_act' ,
    'nom_u' ,
    'nom_i' ,
    'ku' ,
    'ki' ,
    'koefA' ,
    'datetime' ,
    'adress_last_record' ,
    'datetime_adr0' ,
    'version_data' 
    ]
        widgets = {
            'name_counter_full': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'label': 'Название счетчика'}),
            # 'group': forms.Select(attrs={'class': 'form-control', 'label': 'Название группы'}),
            'group': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'label': 'Название группы'}),
            'schem': forms.TextInput(attrs={'class': 'form-control', 'label': 'Название схемы'}),
            'net_adress': forms.TextInput(attrs={'class': 'form-control', 'label': 'Сетевой адрес'}),
            'manuf_number'          : forms.NumberInput(attrs={'class': 'form-control'}),
            'manuf_data'            : forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'klass_react'           : forms.NumberInput(attrs={'class': 'form-control'}),
            'klass_act'             : forms.NumberInput(attrs={'class': 'form-control'}),
            'nom_u'                 : forms.NumberInput(attrs={'class': 'form-control'}),
            'nom_i'                 : forms.NumberInput(attrs={'class': 'form-control'}),
            'ku'                    : forms.NumberInput(attrs={'class': 'form-control'}),
            'ki'                    : forms.NumberInput(attrs={'class': 'form-control'}),
            'koefA'                 : forms.NumberInput(attrs={'class': 'form-control'}),
            'datetime'              : forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'adress_last_record'    : forms.NumberInput(attrs={'class': 'form-control'}),
            'datetime_adr0'         : forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'version_data'          : forms.NumberInput(attrs={'class': 'form-control'})

        }

class DBGForm(forms.ModelForm):
    class Meta:
        model = DBG
        # fields = '__all__'
        # fields = ['name_counter_full', 'group', 'schem', 'net_adress']
        fields = ['name_group_full']
        widgets = {
            'name_group_full': forms.TextInput(attrs={'class': 'form-control', 'label': 'Название группы'}),
            # 'group': forms.Select(attrs={'class': 'form-control', 'empty_label': 'Выберите группу'}),
            # 'schem': forms.TextInput(attrs={'class': 'form-control'}),
            # 'net_adress': forms.TextInput(attrs={'class': 'form-control'})
        }

class DBGCForm(forms.ModelForm):
    class Meta:
        model = DBGC
        # fields = '__all__'
        # fields = ['name_counter_full', 'group', 'schem', 'net_adress']
        fields = ['group', 'counter']
        widgets = {
            # 'group': forms.TextInput(attrs={'class': 'form-control', 'label': 'Название группы'}),
            'group': forms.Select(attrs={'class': 'form-control', 'label': 'Название группы'}),
            # 'counter': forms.TextInput(attrs={'class': 'form-control', 'label': 'Название счетчика'})
            'counter': forms.Select(attrs={'class': 'form-control', 'label': 'Название счетчика'})
        }
