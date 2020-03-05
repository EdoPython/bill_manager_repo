from django import forms
from .models import Bill
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmation = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['autofocus'] = True
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['confirmation'].widget.attrs['class'] = 'form-control'
        self.fields['confirmation'].widget.attrs['placeholder'] = 'Confirm password'

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        # username = cleaned_data.get('username')
        confirmation = cleaned_data.get('confirmation')

        if password != confirmation:
            raise forms.ValidationError('Password and confirmation are not equals')


class BillForm(forms.ModelForm):
    emisor = forms.CharField()
    importe = forms.DecimalField(max_digits=13, decimal_places=2)
    fechahora = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])
    metodo = forms.Select(choices=('Cash', 'Credit card', 'Transfer', 'Paypal', 'Check', 'Other'))
    descripcion = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.fields['emisor'].widget.attrs['class'] = 'form-control'
        self.fields['emisor'].widget.attrs['autofocus'] = True
        self.fields['importe'].widget.attrs['class'] = 'form-control'
        self.fields['fechahora'].widget.attrs['class'] = 'form-control datetimepicker-input'
        self.fields['fechahora'].widget.attrs['data-target'] = '#datetimepicker1'
        self.fields['metodo'].widget.attrs['class'] = 'form-control'
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Bill
        fields = ('emisor', 'importe', 'fechahora', 'metodo', 'descripcion')
