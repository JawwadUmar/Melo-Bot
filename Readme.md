# Melo — Instahyre Job Application Assistant

<div align="center">
  <img src="data/melo.jpg" alt="melo" width="250">
</div>

**Melo** is an automation tool that helps you apply to matching jobs on [Instahyre](https://www.instahyre.com/) based on your configured skills and match threshold.

Instead of manually going through job opportunities one by one, Melo can automate the repetitive parts of the process so you can **sit back and relax** while it handles the applications.

> ⚠️ **Disclaimer:** Use automation responsibly and make sure your use complies with Instahyre's terms of service and applicable policies. Never use credentials belonging to someone else.

---

## ✨ Features

* 🔐 Login to your Instahyre account
* 🔎 Find matching job opportunities
* 🎯 Filter jobs using a configurable skill-match threshold
* 📄 Automate the job application workflow
* ⚙️ Configure credentials and settings through a `.env` file
* 🌐 Browser automation using Chromium

---

## 📋 Requirements

Before getting started, make sure you have:

* Python 3.x
* `pip`
* Chromium/Chrome browser support
* An Instahyre account
* The project source code

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/JawwadUmar/Melo-Bot.git

```

### 2. Create a virtual environment

It is recommended to use a virtual environment so that the project's dependencies don't interfere with your system Python installation.

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Melo uses environment variables for account credentials and configuration.

A `sample.env` file is included in the project as a template.

Create a new `.env` file at the **project root**:

```bash
cp sample.env .env
```

Then open `.env` and fill in your actual values.

Example:

```env
INSTAHYRE_EMAIL="your-email@example.com"
INSTAHYRE_PASSWORD="your-password"
INSTAHYRE_JOB_LINK="https://www.instahyre.com/candidate/opportunities/?matching=true"
PHONE_NUMBER="your-phone-number"
SKILL_MATCH_THRESHOLD="2"
```

### Environment variables

| Variable                | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| `INSTAHYRE_EMAIL`       | Email address associated with your Instahyre account |
| `INSTAHYRE_PASSWORD`    | Instahyre account password                           |
| `INSTAHYRE_JOB_LINK`    | Instahyre job opportunities URL                      |
| `PHONE_NUMBER`          | Phone number used during the application process     |
| `SKILL_MATCH_THRESHOLD` | Minimum skill-match threshold for considering a job  |

### 🔒 Keep your credentials private

**Never commit `.env` to Git.**

Make sure your `.gitignore` contains:

```gitignore
.env
venv/
__pycache__/
*.pyc
data/session/
```

If credentials have already been exposed publicly, **change the password immediately** and replace the exposed credentials in your local `.env`.

---

## ▶️ Running Melo

Once the environment is configured, activate your virtual environment and run:

```bash
python main.py
```

Melo will start the configured automation workflow.

A typical setup looks like:

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python main.py
```

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

---

## 🎯 Skill Match Threshold

The `SKILL_MATCH_THRESHOLD` variable controls how closely a job should match your configured skills before Melo considers it.

For example:

```env
SKILL_MATCH_THRESHOLD="2"
```

Adjust this value according to how strict you want the matching process to be.

A lower threshold may result in more opportunities being considered, while a higher threshold can make the filtering more selective.


---


## 🔐 Security Recommendations

Because Melo works with an account that can submit job applications, treat its credentials as sensitive.

* Never hard-code credentials into Python source files.
* Never commit `.env` to Git.
* Use a dedicated account if appropriate.
* Rotate your password if it is accidentally exposed.
* Review applications before relying on fully automated submissions.
* Respect Instahyre's terms and application limits.

---

## 🤝 Contributing

Contributions, improvements, and bug fixes are welcome.

A typical workflow is:

```bash
git checkout -b feature/my-feature
```

Make your changes, test them locally, and open a pull request.

---

## 📄 License

```text
MIT License
```

---

## ❤️ Melo

**Configure it once. Start it. Let Melo handle the repetitive work.**

```bash
python main.py
```

**Sit back and relax. 🚀**
