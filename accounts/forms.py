from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={"placeholder": "First Name"}
        ))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={"placeholder": "Last Name"}
        ))
    
    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        # Add your own processing here.
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # You must return the original result.
        return user