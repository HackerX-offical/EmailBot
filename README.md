# EmailBot

A Python script designed to simulate sending multiple job offer emails from various tech giants (Google, Microsoft, Amazon, Apple, Meta, NVIDIA, OpenAI, X) to a specific target email address.

## ⚠️ Disclaimer

**This tool is for educational and testing purposes only.** Do not use this to spam, harass, or deceive others. The author is not responsible for any misuse of this tool.

## Features

- **Multiple Senders:** Configurable list of sender email accounts.
- **Customized Content:** Pre-defined HTML templates for job offers from major tech companies.
- **Automated Sending:** Iterates through the list of senders and sends the corresponding email to the target address.
- **Spam Avoidance:** Includes a slight delay between emails to help avoid triggering spam filters.

## Prerequisites

- Python 3.x
- Gmail accounts for sending emails.
- **App Passwords:** You must generate App Passwords for each sender Gmail account. Standard passwords will not work if 2-Step Verification is enabled (which is required for App Passwords).

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/HackerX-offical/EmailBot.git
    cd EmailBot
    ```

2.  **Configure the script:**
    Open `app.py` and update the following variables:

    - `TARGET_EMAIL`: The email address that will receive the simulated offers.
    - `SENDERS`: A list of tuples containing the sender email and their corresponding App Password.
      ```python
      SENDERS = [
          ("your_email1@gmail.com", "your_app_password_1"),
          ("your_email2@gmail.com", "your_app_password_2"),
          # ... add more senders
      ]
      ```
    - `EMAILS`: (Optional) You can modify the `subject` and `html` content in the `EMAILS` dictionary to customize the messages.

## Usage

Run the script using Python:

```bash
python app.py
```

The script will iterate through the configured senders and print the status of each email sent.

## Security Note

- **Never commit your real passwords or App Passwords to GitHub.**
- Use environment variables or a separate configuration file (listed in `.gitignore`) if you plan to share your code or make it public.

## License

This project is open source.
