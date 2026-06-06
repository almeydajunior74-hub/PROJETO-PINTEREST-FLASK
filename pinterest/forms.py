#criando os formularios de login e de perfil
from flask_wtf import FlaskForm   #estrutura da class
from wtforms import StringField,PasswordField,SubmitField,FileField #campo_texto/ campo_senha/#campo_botão_form,arquivos
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError 
#validar campos emai/equalto_if_senha==senha/tamanho_de senha(caract...)/mensagem de erro
from pinterest.models import Usuario



class FormLogin(FlaskForm):
    email = StringField("E-mail",validators=[DataRequired(),Email()])
    senha = PasswordField("Senha",validators=[DataRequired()])
    botao_confirmacao = SubmitField("Login")



class FormCriarConta(FlaskForm):
    email = StringField("E-mail",validators=[DataRequired(),Email()])
    username = StringField("Nome de usuario",[DataRequired()])
    senha = PasswordField("Senha",validators=[DataRequired(),Length(6,20)])
    confirmar_senha = PasswordField("Confirmar Senha",validators=[DataRequired(),EqualTo("senha")])
    botao_confirmacao=SubmitField("Criar Conta")
 


    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()

        if usuario:
            return ValidationError("Erro... Esse e-mail já foi cadastrado")




class FormFoto(FlaskForm):
    foto = FileField("foto",validators=[DataRequired()])
    botao_confirmar = SubmitField("Enviar foto")