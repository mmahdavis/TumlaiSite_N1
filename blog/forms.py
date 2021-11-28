from django import forms


class CommentForm(forms.Form):
    name=forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs={'class':'form-control text','placeholder':'نام'})
    )
    email=forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control text email','placeholder':'ایمیل'})
    )
    title=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control text','placeholder':'موضوع'})
    )
    message=forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control textarea','placeholder':'پیام شما'})
    )