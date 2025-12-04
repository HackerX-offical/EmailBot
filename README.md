# EmailBot

A Python script designed to simulate sending multiple job offer emails from various tech giants (Google, Microsoft, Amazon, Apple, Meta, NVIDIA, OpenAI, X) to a specific target email address.

## ⚠️ Disclaimer

**This tool is for educational and testing purposes only.** Do not use this to spam, harass, or deceive others. The author is not responsible for any misuse of this tool.

## Scripts

This repository contains two scripts with different behaviors:

### 1. `app.py` (Multi-Sender Mode)

- **Purpose:** Sends one email from _each_ configured sender in the `SENDERS` list.
- **Behavior:** Iterates through the list of sender accounts and sends the specific company email associated with that sender index/key.
- **Best for:** Testing multiple sender accounts or sending a specific set of emails once.

### 2. `main.py` (Continuous Loop Mode)

- **Purpose:** Continuously sends random job offer emails from a _single_ sender account.
- **Behavior:**
  - Runs in cycles: Sends emails for a set duration (default 10 mins), then pauses (default 30 mins).
  - Randomly selects a tech company for each email.
  - Fetches and embeds company logos as Base64 images.
  - Includes retry logic and connection handling.
- **Best for:** Long-running stress testing or continuous simulation.

## Prerequisites

- Python 3.x
- `requests` library (for `main.py`)
- Gmail accounts for sending emails.
- **App Passwords:** You must generate App Passwords for each sender Gmail account. Standard passwords will not work if 2-Step Verification is enabled.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/HackerX-offical/EmailBot.git
    cd EmailBot
    ```

2.  **Install dependencies (for `main.py`):**

    ```bash
    pip install requests
    ```

3.  **Configure the scripts:**

    **For `app.py`:**
    Open `app.py` and update:

    - `TARGET_EMAIL`: The recipient email.
    - `SENDERS`: List of `(email, app_password)` tuples.

    **For `main.py`:**
    Open `main.py` and update:

    - `TARGET_EMAIL`: The recipient email.
    - `SENDER_EMAIL`: Your single sender Gmail address.
    - `SENDER_PASSWORD`: Your sender App Password.
    - _Optional:_ Adjust `RUN_DURATION`, `PAUSE_DURATION`, and `EMAIL_DELAY` at the top of the file.

## Usage

**To run the multi-sender script:**

```bash
python app.py
```

**To run the continuous loop script:**

```bash
python main.py
```

## Security Note

- **Never commit your real passwords or App Passwords to GitHub.**
- Use environment variables or a separate configuration file (listed in `.gitignore`) if you plan to share your code or make it public.

## License

This project is open source.
