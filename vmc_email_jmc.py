import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders 
import os
email = os.getenv("BREVO_FROM_EMAIL", "mathclub@sjs.edu.bd")
password = os.getenv("BREVO_SMTP_PASSWORD")

recipents = [
    "sharanhaquesakin@gmail.com",
    "sharanhaques@gmail.com",
    "tawhidbinomar@gmail.com"
]


subject = "JMC Best"
body = "Here's your certifcate mate! "

api_key = os.getenv("BREVO_SMTP_API_KEY")
user = os.getenv("BREVO_SMTP_USER")

pdf = "pset.pdf"

server = smtplib.SMTP("smtp-relay.brevo.com", 587)
server.starttls()
if not user or not api_key:
    raise ValueError("Missing SMTP credentials. Set BREVO_SMTP_USER and BREVO_SMTP_API_KEY.")
server.login(user, api_key)

for r in recipents:

    msg = MIMEMultipart()
    msg["from"] = email
    msg["to"] = r
    msg["Subject"] = subject
    msg.attach(MIMEText(body , "plain"))

    # The attachment part

    with open(pdf, "rb") as file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f'attachment; filename="{os.path.basename(pdf)}"'
    )

    msg.attach(part)

    try:
        server.send_message(msg)
        print(f"Emailed {r}")
    
    except Exception as err:

        print(f"Failed to mail {r}: ", err) 

server.quit()   


