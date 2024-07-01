from django import forms

class LoginForms(forms.Form):
   
    nome_login = forms.CharField(
        label= 'Login',
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite seu Usuario'
            }
        )
    )
    senha = forms.CharField(
        label= 'senha',
        required= True,
        max_length=70,
        widget= forms.PasswordInput(
           
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    
    nome_cadastro = forms.CharField(
        label= 'Nome do cadastro',
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex: Matheus Rodrigues'
            }
        )
    )
    email = forms.EmailField(
        label= 'Emaill',
        required= True,
        max_length= 100,
        widget= forms.EmailInput({
            'class': 'form-control',
            'placeholder': 'Ex: matheusrsr@gmail.com'
            }
        )
    )
    senha = forms.CharField(
        label= 'senha',
        required= True,
        max_length=70,
        widget= forms.PasswordInput(
           
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )
    confirmar_senha = forms.CharField(
        label= 'confirmar senha',
        required= True,
        max_length=70,
        widget= forms.PasswordInput(
           
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )