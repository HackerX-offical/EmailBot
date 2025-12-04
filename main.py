import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import random
import requests
import base64

# Constants for timing
RUN_DURATION = 10 * 60  # 10 minutes in seconds
PAUSE_DURATION = 30 * 60  # 30 minutes in seconds
EMAIL_DELAY = 3  # Seconds between emails

# Your target email
TARGET_EMAIL = "your_target_email@gmail.com"

# Single sender account
SENDER_EMAIL = "your_sender_email@gmail.com"
SENDER_PASSWORD = "your_sender_password"

def get_base64_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_data = base64.b64encode(response.content).decode('utf-8')
            return f"data:image/png;base64,{image_data}"
    except Exception as e:
        print(f"Error fetching image: {e}")
    return None

# Company logos (direct image URLs)
COMPANY_LOGOS = {
    "Google": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
    "Microsoft": "https://img.icons8.com/color/96/000000/microsoft.png",
    "Amazon": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg",
    "Apple": "https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png",
    "Meta": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Meta_Platforms_Inc._logo.svg",
    "NVIDIA": "https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/01-nvidia-logo-vert-500x200-2c50-d@2x.png",
    "OpenAI": "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg",
    "X": "https://upload.wikimedia.org/wikipedia/commons/5/57/X_logo_2023_%28white%29.png"
}

# Email subjects and HTML contents keyed by company
EMAILS = {
    "Google": {
        "subject": "Congratulations! You've Been Selected for the Software Developer Position at Google",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="Google Logo" style="height: 60px;">
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
    "Microsoft": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at Microsoft",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="Microsoft Logo" style="height: 60px;">
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
    "Amazon": {
        "subject": "Congratulations! You've Been Selected for the Software Development Engineer Position at Amazon",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="Amazon Logo" style="height: 60px;">
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
    "Apple": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at Apple",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="Apple Logo" style="height: 60px;">
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
    "Meta": {
        "subject": "Congratulations! You've Been Selected for the Software Developer Position at Meta",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="Meta Logo" style="height: 60px;">
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
    "NVIDIA": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at NVIDIA",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="NVIDIA Logo" style="height: 60px;">
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
    "OpenAI": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at OpenAI",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="OpenAI Logo" style="height: 60px;">
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
    "X": {
        "subject": "Congratulations! You've Been Selected for the Software Engineer Position at X",
        "html": """
        <html><body>
        <div style="font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
        <div style="text-align: center; margin-bottom: 30px;">
            <img src="{logo}" alt="X Logo" style="height: 60px;">
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
    max_retries = 3
    retry_count = 0
    server = None
    
    while retry_count < max_retries:
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['From'] = sender_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(html_content, 'html'))

            # Create new connection for each attempt
            server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
            server.set_debuglevel(0)  # Disable debug output
            server.ehlo()
            server.starttls()
            server.ehlo()
            
            # Login with explicit error handling
            try:
                server.login(sender_email, sender_password)
            except smtplib.SMTPAuthenticationError:
                print("Authentication failed. Please check your credentials.")
                return False
            except Exception as e:
                print(f"Login error: {e}")
                return False
            
            # Send email
            try:
                server.sendmail(sender_email, to_email, msg.as_string())
            except Exception as e:
                print(f"Send error: {e}")
                return False
            
            server.quit()
            return True
            
        except smtplib.SMTPServerDisconnected:
            retry_count += 1
            if server:
                try:
                    server.quit()
                except:
                    pass
            
            if retry_count < max_retries:
                print(f"Connection lost. Retry {retry_count}/{max_retries}...")
                time.sleep(10)  # Wait 10 seconds before retry
            else:
                print("Failed to send email after multiple attempts")
                return False
                
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

def main():
    print("Loading company logos...")
    encoded_logos = {}
    for company, logo_url in COMPANY_LOGOS.items():
        print(f"Loading {company} logo...")
        encoded_logo = get_base64_image(logo_url)
        if encoded_logo:
            encoded_logos[company] = encoded_logo
            print(f"✓ {company} logo loaded")
        else:
            print(f"✗ Failed to load {company} logo")
    
    print("\nStarting email cycle...")
    email_count = 0
    
    while True:
        start_time = time.time()
        print(f"\nStarting {RUN_DURATION//60} minute sending cycle...")
        
        # Run for RUN_DURATION
        while time.time() - start_time < RUN_DURATION:
            company = random.choice(list(EMAILS.keys()))
            email_data = EMAILS[company]
            
            print(f"\nSending email from {company}...")
            html_content = email_data['html'].format(logo=encoded_logos.get(company, ''))
            
            if send_email(SENDER_EMAIL, SENDER_PASSWORD, TARGET_EMAIL, email_data['subject'], html_content):
                email_count += 1
                print(f"✓ Email sent successfully ({email_count} total)")
            else:
                print("✗ Failed to send email")
            
            time.sleep(EMAIL_DELAY)
        
        # Pause for PAUSE_DURATION
        print(f"\nPausing for {PAUSE_DURATION//60} minutes...")
        time.sleep(PAUSE_DURATION)

if __name__ == "__main__":
    main()
