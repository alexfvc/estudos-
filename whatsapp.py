from twilio.rest import Client
import os

# as credenciais são recuperadas das variáveis de ambiente TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
client = Client()

# esse é o numero de teste da sandbox da Twilio
from_whatsapp_number='whatsapp:+5561981557486'
# substitua esse número com o seu próprio número do Whatsapp
to_whatsapp_number='whatsapp:+5561981557486'

client.messages.create(body='oi',
                      from_=from_whatsapp_number,
                      to=to_whatsapp_number)