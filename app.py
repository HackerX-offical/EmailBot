import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Your target email
TARGET_EMAIL = "suryanshunab@gmail.com"

# Sender accounts (email, app_password)
SENDERS = [
    ("email1@gmail.com", "app_password_for_email1"),  # Replace with actual app password
    ("email2@gmail.com", "app_password_for_email2"),
    ("email3@gmail.com", "app_password_for_email3"),
    ("email4@gmail.com", "app_password_for_email4"),
    ("email5@gmail.com", "app_password_for_email5"),
    ("email6@gmail.com", "app_password_for_email6"),
    ("email7@gmail.com", "app_password_for_email7"),
    ("email8@gmail.com", "app_password_for_email8"),
]


# Email subjects and HTML contents keyed by sender email
EMAILS = {
    "email1@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Developer Position at Google",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" alt="Google Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Developer</strong> position at <strong>Google</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the Google family.</p>
        <br/>
        <p>Best regards,<br/>
        Anjali Mehta<br/>
        Senior Talent Acquisition Specialist<br/>
        Google LLC<br/>
        <a href="mailto:anjali.mehta@google.com">anjali.mehta@google.com</a><br/>
        +1 (650) 555-1234</p>
        </div>
        </body></html>
        """
    },
    "email2@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at Microsoft",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" alt="Microsoft Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Engineer</strong> position at <strong>Microsoft</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the Microsoft family.</p>
        <br/>
        <p>Best regards,<br/>
        Rajesh Kumar<br/>
        Senior Talent Acquisition Specialist<br/>
        Microsoft Corporation<br/>
        <a href="mailto:rajesh.kumar@microsoft.com">rajesh.kumar@microsoft.com</a><br/>
        +1 (425) 882-8080</p>
        </div>
        </body></html>
        """
    },
    "email3@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Development Engineer Position at Amazon",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg" alt="Amazon Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Development Engineer</strong> position at <strong>Amazon</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the Amazon family.</p>
        <br/>
        <p>Best regards,<br/>
        Neha Singh<br/>
        Senior Talent Acquisition Specialist<br/>
        Amazon.com, Inc.<br/>
        <a href="mailto:neha.singh@amazon.com">neha.singh@amazon.com</a><br/>
        +1 (206) 266-1000</p>
        </div>
        </body></html>
        """
    },
    "email4@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at Apple",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg" alt="Apple Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Engineer</strong> position at <strong>Apple</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the Apple family.</p>
        <br/>
        <p>Best regards,<br/>
        Sarah Johnson<br/>
        Senior Talent Acquisition Specialist<br/>
        Apple Inc.<br/>
        <a href="mailto:sarah.johnson@apple.com">sarah.johnson@apple.com</a><br/>
        +1 (408) 996-1010</p>
        </div>
        </body></html>
        """
    },
    "email5@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Developer Position at Meta",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Meta_Platforms_Inc._logo.svg" alt="Meta Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Developer</strong> position at <strong>Meta</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the Meta family.</p>
        <br/>
        <p>Best regards,<br/>
        Michael Chen<br/>
        Senior Talent Acquisition Specialist<br/>
        Meta Platforms Inc.<br/>
        <a href="mailto:michael.chen@meta.com">michael.chen@meta.com</a><br/>
        +1 (650) 543-4800</p>
        </div>
        </body></html>
        """
    },
    "email6@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at NVIDIA",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Nvidia_logo.svg" alt="NVIDIA Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Engineer</strong> position at <strong>NVIDIA</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the NVIDIA family.</p>
        <br/>
        <p>Best regards,<br/>
        David Wilson<br/>
        Senior Talent Acquisition Specialist<br/>
        NVIDIA Corporation<br/>
        <a href="mailto:david.wilson@nvidia.com">david.wilson@nvidia.com</a><br/>
        +1 (408) 486-2000</p>
        </div>
        </body></html>
        """
    },
    "email7@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at OpenAI",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" alt="OpenAI Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Engineer</strong> position at <strong>OpenAI</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the OpenAI family.</p>
        <br/>
        <p>Best regards,<br/>
        Emily Rodriguez<br/>
        Senior Talent Acquisition Specialist<br/>
        OpenAI<br/>
        <a href="mailto:emily.rodriguez@openai.com">emily.rodriguez@openai.com</a><br/>
        +1 (415) 123-4567</p>
        </div>
        </body></html>
        """
    },
    "email8@gmail.com": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at X",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/57/X_logo_2023_%28white%29.png" alt="X Logo" style="height: 60px;">
        </div>
        <p>Dear Suryanshu Nabheet,</p>
        <p>We are delighted to inform you that after a thorough evaluation of your application and interview performance, you have been shortlisted and selected for the <strong>Software Engineer</strong> position at <strong>X</strong>.</p>
        <p>Your strong technical skills, problem-solving abilities, and passion for innovation truly impressed our hiring team. We are confident that you will make valuable contributions to our engineering projects and be a great fit within our collaborative work environment.</p>
        <p><strong>Next steps:</strong><br/>
        Our Human Resources team will contact you shortly with the formal offer letter and detailed information about the onboarding process. Should you have any questions or require further assistance, please do not hesitate to reach out to us.</p>
        <p>Congratulations once again, Suryanshu! We look forward to welcoming you to the X family.</p>
        <br/>
        <p>Best regards,<br/>
        Alex Thompson<br/>
        Senior Talent Acquisition Specialist<br/>
        X Corp<br/>
        <a href="mailto:alex.thompson@x.com">alex.thompson@x.com</a><br/>
        +1 (415) 222-9670</p>
        </div>
        </body></html>
        """
    }
}

def send_email(sender_email, sender_password, to_email, subject, html_content):
    # Setup SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully from {sender_email} to {to_email}")
    except Exception as e:
        print(f"Failed to send email from {sender_email}: {e}")

def main():
    for sender_email, sender_password in SENDERS:
        if sender_email in EMAILS:
            subject = EMAILS[sender_email]['subject']
            html = EMAILS[sender_email]['html']
            send_email(sender_email, sender_password, TARGET_EMAIL, subject, html)
            time.sleep(1)  # wait 1 second between emails to avoid triggering spam filters
        else:
            print(f"No email content defined for {sender_email}")

if __name__ == "__main__":
    main()
