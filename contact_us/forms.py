from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    
    contact_widget_form = {'class': 'form-control', 'rows': 6, 'cols': 100,
                        'style': 'box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);' 'resize:none; padding: 10px;', 
                        'onfocus': 'this.style.borderColor="#019cbb";', 
                        'onfocusout': 'this.style.borderColor="";'
                    }
    name = forms.CharField(label='Nume', max_length=100, widget=forms.TextInput(attrs=contact_widget_form))
    email = forms.EmailField(label='Email', max_length=100, validators=[EmailValidator()], widget=forms.EmailInput(attrs=contact_widget_form))
    message = forms.CharField(label='Mesaj', widget=forms.Textarea(attrs=contact_widget_form))