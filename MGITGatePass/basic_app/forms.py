from django import forms
from django.contrib.auth.models import User
from basic_app.models import StudentProfileInfo,GatepassRequests

def isroll(rl):
    if('A' in rl and '26' in rl and len(rl)==10):
        return True
    return False
    

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','email','password')
   
class StudentProfileInfoForm(forms.ModelForm):
    class Meta():
        model = StudentProfileInfo
        fields = ('roll','profile_pic','branch','typeof')
    def clean_roll(self):
         rolls = self.cleaned_data.get('roll')
        
         if not isroll(rolls):
             raise forms.ValidationError("Enter a valid roll, make sure A is capitol")
         return rolls         
