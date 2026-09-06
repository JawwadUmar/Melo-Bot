import os
from dotenv import load_dotenv

load_dotenv()

#ENVRIONMENT VARIABLES
EMAIL = os.getenv("INSTAHYRE_EMAIL")
PASSWORD = os.getenv("INSTAHYRE_PASSWORD")
JOBLINK = os.getenv("INSTAHYRE_JOB_LINK")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

def _env_bool(name, default="false"):
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "y", "on"}

if not EMAIL or not PASSWORD or not JOBLINK:
    raise ValueError("Credentials missing in .env")

#PATH WHERE SESSION DATA IS SAVED [DON'T COMMIT THIS PATH !!!]
USER_DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), "../../data/session")



