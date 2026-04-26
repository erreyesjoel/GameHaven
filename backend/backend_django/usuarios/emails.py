from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse

def send_internal_email(request, user):
    # Generar token y uid
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    
    # Construir la URL completa
    relative_url = reverse('definir_contrasena', kwargs={'uidb64': uid, 'token': token})
    token_url = request.build_absolute_uri(relative_url)

    # Renderizar tu template HTML
    html_message = render_to_string("emails/set_password_email.html", {
        "user": user,
        "token_url": token_url,
    })

    # Enviar correo
    send_mail(
        subject="Definir contraseña interna",
        message=f"Hola {user.email}, haz clic en el siguiente enlace para definir tu contraseña: {token_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
        fail_silently=False,
    )
