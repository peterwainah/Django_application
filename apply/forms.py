from django import forms
from apply.models import UserProfileInfo, ScholarshipApplication, SchoolInformation
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

class ScholarshipApplicationForm(forms.ModelForm):
    class Meta:
        model = ScholarshipApplication
        fields = '__all__'

    def clean(self): 
  
        # data from the form is fetched using super function 
        super(ScholarshipApplicationForm, self).clean() 
          
        # extract the username and text field from the data 
        name = self.cleaned_data.get('name')
  
        # conditions to be met for the username length 
        if len(name) < 5: 
            self._errors['name'] = self.error_class([ 
                'Minimum 5 characters required']) 
    
        # return any errors if found 
        return self.cleaned_data 

class SchoolInformationForm(forms.ModelForm):
    class Meta:
        model = SchoolInformation
        fields = '__all__'

    def clean(self): 
  
        # data from the form is fetched using super function 
        super(SchoolInformationForm, self).clean() 
          
        # extract the username and text field from the data 
        name = self.cleaned_data.get('name')
  
        # conditions to be met for the username length 
        if len(name) < 5: 
            self._errors['name'] = self.error_class([ 
                'Minimum 5 characters required']) 
    
        # return any errors if found 
        return self.cleaned_data 