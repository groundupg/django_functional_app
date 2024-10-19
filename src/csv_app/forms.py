from django import forms

class CSVForm(forms.Form):



    csv = forms.FileField(label='csv_upload', widget=forms.ClearableFileInput())

    remove_duplicates = forms.BooleanField(label="Remove Duplicates", widget=forms.CheckboxInput(), required=False)
