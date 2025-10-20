from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django  import  forms



class UserCreation(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(widget=forms.PasswordInput,label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput,label='Повторение пароля')
    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name','password1','password2',]
        labels= {   'username':'Имя пользователя',
                    'email':'Почта',
                    'first_name':'Имя',
                    'last_name':'Фамилия',}


    def email_check(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.get(email=email):
            raise forms.ValidationError('Пользователь с такой почтой уже существует')
        return email




class UserLogin(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput({'class':'form-input'}))


    class Meta:
        model = get_user_model()
        fields = ['username','password']
        labels = {'username':'Имя пользователя',
                  'password':'Пароль',}