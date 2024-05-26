import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(file_path, recipient_email):
    sender_email = "gerbylev.oleg@gmail.com"
    sender_password = "jybd gmjy pjzu louw"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Файл .docx"

    attachment = open(file_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % file_path)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Укажите SMTP-сервер и порт
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

