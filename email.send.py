import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'sabiha'
email['to'] = "athiq@ezcloudai.com"
email['subject'] = 'greetings by sabiha'

email.set_content('I am a python developer')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('tttestertest05@gmail.com', 'Tester123')
    smtp.send_message(email)
    print("all is well")
