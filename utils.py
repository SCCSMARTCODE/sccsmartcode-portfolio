from dataclasses import dataclass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@dataclass
class FormData:
    name: str
    email: str
    subject: str
    message: str


# Send email (placeholder for email sending logic)
def send_email(form_data: FormData):
    formatted_email = contact_email_sec1_template + contact_email_sec2_template.format(
        sender_name=form_data.name,
        sender_email=form_data.email,
        contact_subject=form_data.subject,
        contact_message=form_data.message
    )

    # Email configuration
    sender_email = receiver_email = "sccsmart247@gmail.com"
    email_subject = f"New Contact Message: {form_data.subject}"

    # Create a multipart message and set headers
    msg = MIMEMultipart("alternative")
    msg["Subject"] = email_subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Attach the HTML content to the email
    msg.attach(MIMEText(formatted_email, "html"))

    # Gmail SMTP configuration
    smtp_server = "smtp.gmail.com"
    port = 587  # For TLS
    password = "letd hyth zgri bmju"  # Replace with your Gmail App Password

    try:
        # Connect to the Gmail SMTP server and send email
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)



contact_email_sec1_template = """
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>New Contact Message - {contact_subject}</title>
            <style type="text/css">
              /* Basic Reset */
              body, p, h1, h2, a { margin: 0; padding: 0; }
              body {
                background-color: #f9f9f9;
                font-family: Arial, sans-serif;
                color: #333333;
                line-height: 1.5;
              }
              .container {
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                border: 1px solid #dddddd;
                padding: 20px;
              }
              .header {
                background-color: #0f172a;
                color: #ffffff;
                text-align: center;
                padding: 20px;
              }
              .header h1 {
                font-size: 24px;
              }
              .content {
                padding: 20px;
                font-size: 16px;
              }
              .content p {
                margin-bottom: 10px;
              }
              .footer {
                font-size: 12px;
                color: #777777;
                text-align: center;
                padding: 10px;
                border-top: 1px solid #dddddd;
                margin-top: 20px;
              }
            </style>
          </head>

          """
contact_email_sec2_template = """
          <body>
            <div class="container">
              <div class="header">
                <h1>New Contact Message Received</h1>
              </div>
              <div class="content">
                <p><strong>Name:</strong> {sender_name}</p>
                <p><strong>Email:</strong> {sender_email}</p>
                <p><strong>Subject:</strong> {contact_subject}</p>
                <p><strong>Message:</strong></p>
                <p>{contact_message}</p>
              </div>
              <div class="footer">
                <p>This message was sent from your portfolio website contact form.</p>
              </div>
            </div>
          </body>
        </html>
        """
