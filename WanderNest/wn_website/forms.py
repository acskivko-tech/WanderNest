from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django  import  forms



class UserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Имя пользователя',
            'email': 'Почта',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def email_check(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с такой почтой уже существует')
        return email

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.help_text = ''




class UserLoginFrom(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput({'class':'form-input'}))


    class Meta:
        model = get_user_model()
        fields = ['username','password']
        labels = {'username':'Имя пользователя',
                  'password':'Пароль',}




class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(disabled=True)
    password = forms.CharField(widget=forms.PasswordInput,disabled=True)

    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name']



