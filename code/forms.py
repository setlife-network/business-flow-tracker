from django import forms

class ConsultationRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    project_description = forms.CharField(widget=forms.Textarea)
    budget = forms.DecimalField(max_digits=10, decimal_places=2)
