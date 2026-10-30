from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class CadastroForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label='E-mail'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email