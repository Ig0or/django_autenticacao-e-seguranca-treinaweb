from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.password_validation import password_changed

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome=None, pais_origem=None, password=None):
        if not email:
            raise ValueError('O usuário precisa de um email.')
        usuario = self.model(
            nome = nome,
            pais_origem = pais_origem,
            email = self.normalize_email(email)
         )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, nome, pais_origem, email, password):
        usuario = self.create_user(nome=nome, email=email, pais_origem=pais_origem)
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        return usuario
