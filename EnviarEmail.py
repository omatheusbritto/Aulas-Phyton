import datetime
from time import sleep
import win32com.client as win32

# criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)

nome = str(input('Digite o seu nome: '))
sleep(1.3)
emaildestinatario = str(input('Digite o E-mail destinatário: '))
sleep(1.3)
assunto = str(input('Qual o assunto: '))
sleep(1.3)
textoprincipal = str(input('Digite o seu texto: '))
sleep(1.3)
fonecontato = str(input('Deixe o seu telefone para contato com DDD: '))
(sleep(2))
data = datetime.datetime.now()

# configurar as informações do seu e-mail
email.To = f"{emaildestinatario}"
email.Subject = f"{assunto} {data.day}/{data.month}/{data.year} "
email.HTMLBody = f"""
<p>E-mail de: {nome},</p><br><br>
<p>Informa-se que: {textoprincipal}</p> <br><br>
<p>Telefone para contato de {nome}: {fonecontato}</p>

<p>Email enviado em {data.day}/{data.month}/{data.year}</p>

<p>Email enviado atraves de Python</p>
"""

#anexo = "C://Users/theub/OneDrive/Imagens/ComboCasal.jpeg"
#email.Attachments.Add(anexo)

email.Send()
print(f"Email Enviado com sucesso para {emaildestinatario}")
sleep(5)