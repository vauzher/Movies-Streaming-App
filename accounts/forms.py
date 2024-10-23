from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from .models import Profile

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            try:
                user_profile = self.instance.profile
            except Profile.DoesNotExist:
                user_profile = None

            if user_profile:
                self.fields['profile_picture'].initial = user_profile.profile_photo

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password and new_password != confirm_password:
            raise forms.ValidationError("The new passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            if self.cleaned_data.get('profile_picture'):
                profile.profile_photo = self.cleaned_data['profile_picture']
            profile.save()
        return user
