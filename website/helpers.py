from django.core.mail import send_mail
from django.conf import settings






def send_forget_password_mail(email,token):
    subject = 'your forget password link'
    messages = f'Hi ,click on the linkto reset your password http://127.0.0.1:9000/website/change_password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    print("this is the email:",email)
    recipient_list = [email]
    send_mail(subject,messages,email_from,recipient_list,fail_silently=False)
    return  True