from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from .models import ExtraUserInformations
from django.contrib.auth.forms import PasswordChangeForm
        

class EditUserInfoForm(forms.ModelForm):
    '''The user profile editing form'''
    #user_widget_form used to style some of the fields"
    user_widget_form = {'class': 'form-control', 
                        'size': '30', 
                        'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                        'onfocus': 'this.style.borderColor="#019cbb";', 
                        'onfocusout': 'this.style.borderColor="";'
                    }
    
    username = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_form))
    first_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_form))
    last_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput(attrs=user_widget_form))
    email = forms.EmailField(widget=forms.EmailInput(attrs=user_widget_form))
    
    date_of_birth= forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=range(datetime.now().year, 1900, -1),
                                                                                       attrs={'class': 'form-select',
                                                                                            'size': '1',
                                                                                            'style': 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);', 
                                                                                            'onfocus': 'this.style.borderColor="#019cbb";', 
                                                                                            'onfocusout': 'this.style.borderColor="";'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth']
        
    def __init__(self, *args, **kwargs):
        '''We use the __init__ method to get the date_of_birth from the ExtraUserInformations model and set it as initial value for the date_of_birth field in the form.'''
        
        super().__init__(*args, **kwargs)
        if self.instance:
            try:
                extra_info = ExtraUserInformations.objects.get(user=self.instance)
                self.fields['date_of_birth'].initial = extra_info.date_of_birth
            except ExtraUserInformations.DoesNotExist:
                pass

    def save(self, commit=True):
        '''We override the save method to save the date_of_birth in the ExtraUserInformations model.'''
        
        user = super().save(commit=commit)
        if commit:
            extra_info, created = ExtraUserInformations.objects.get_or_create(user=user)
            extra_info.date_of_birth = self.cleaned_data['date_of_birth']
            extra_info.save()
        return user
    
    def clean_date_of_birth(self):
        '''We use the clean_date_of_birth method to check if the user is at least 18 years old. If not, we raise a ValidationError.'''
        
        birth_date = self.cleaned_data["date_of_birth"]
        actual_date = datetime.now().date()
        dif = actual_date - birth_date
        age = dif.days // 365
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to create an account.")
        
        return birth_date

class ChangeUserPassForm(PasswordChangeForm):
    '''The change password form using the PasswordChangeForm imported from django.contrib.auth.forms'''
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
    
    #applied Bootstrap
    def __init__(self, *args, **kwargs):
        '''We use the __init__ method to apply the Bootstrap classes to the fields and remove the help_text. 
            We also set the size and box-shadow for the fields and the onfocus and onfocusout events.'''
            
        super(ChangeUserPassForm, self).__init__(*args, **kwargs)
        
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
        
        self.fields['old_password'].widget.attrs['size'] = '30'
        self.fields['new_password1'].widget.attrs['size'] = '30'
        self.fields['new_password2'].widget.attrs['size'] = '30'
        
        self.fields['old_password'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        self.fields['new_password1'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        self.fields['new_password2'].widget.attrs['style'] = 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        
        self.fields['old_password'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['old_password'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['new_password1'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['new_password1'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
        self.fields['new_password2'].widget.attrs['onfocus'] = 'this.style.borderColor="#019cbb";'
        self.fields['new_password2'].widget.attrs['onfocusout'] = 'this.style.borderColor="";'
    
class UserPicForm(forms.ModelForm):
    '''The user profile picture form using the ImageField from the forms module. 
        We use the FileInput widget to style the field.'''  
        
    user_pic = forms.ImageField(label='Profile Picture', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
         model = ExtraUserInformations
         fields = ['user_pic']
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    