import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fetch_articles import fetch_articles  # Import function from fetch_articles.py
import Credentials


def send_email(subject, articles, sender_email, app_password, receiver_email):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Format email body
    email_body = f"{subject}\n\n"
    for article in articles:
        title = article.get('title', 'No Title')
        body = article.get('body', 'No Body')
        url = article.get('url')
        email_body += f"Title: {title}\n\n"
        email_body += f"{body}\n"
        email_body += f"{url}\n\n"

    # Add body to email
    msg.attach(MIMEText(email_body, 'plain'))

    # Send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")


if __name__ == "__main__":
    api_key = Credentials.api_key
    sender_email = Credentials.sender_email
    app_password = Credentials.app_password
    receiver_email = Credentials.receiver_email


    # Fetch articles
    articles = fetch_articles(api_key)
    email_subject = "Latest Articles Related to Australia"

    # Send email
    send_email(email_subject, articles, sender_email, app_password, receiver_email)
