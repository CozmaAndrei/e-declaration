from django import forms

class MyForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'myTextarea',
                                                        'class': 'form-control',
                                                        'rows': 8,
                                                        'style': 'padding: 10px;'
                                                        }))