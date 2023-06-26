from django import forms
g=[('MALE','male'),('FEMALE','female')]

class student(forms.Form):
    Name=forms.CharField(max_length=100)
    Age =forms.IntegerField()
    Email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    Address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'cols':4,'rows':3}))
    gender=forms.ChoiceField(choices=g)