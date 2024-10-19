from django import forms

class CSVForm(forms.Form):

    csv = forms.FileField(label='csv_upload')