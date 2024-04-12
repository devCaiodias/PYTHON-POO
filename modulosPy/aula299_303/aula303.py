# Enviando E-mails SMTP com Python
import os
import pathlib
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

# Caminho file HTML
caminho_file_HTML = 'C:\\Users\\caiod\\pythonPOO\\modulosPy\\aula299_303\\aula303.html'

# Dados do meu remetente
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configuração SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(caminho_file_HTML, 'r', encoding='utf-8') as file:
    texto_file = file.read()
    templete = Template(texto_file)
    texto_email = templete.substitute(nome='Caio')


# Transformar nossas mensagem em MIMEMUltipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do E-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')