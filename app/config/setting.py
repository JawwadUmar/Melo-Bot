import os

from dotenv import load_dotenv

load_dotenv()

#ENVRIONMENT VARIABLES
EMAIL = os.getenv("INSTAHYRE_EMAIL")
PASSWORD = os.getenv("INSTAHYRE_PASSWORD")
JOBLINK = os.getenv("INSTAHYRE_JOB_LINK")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SKILL_MATCH_THRESHOLD = int(os.getenv("SKILL_MATCH_THRESHOLD", "2"))

def _env_bool(name, default="false"):
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "y", "on"}

if not EMAIL or not PASSWORD or not JOBLINK:
    raise ValueError("Credentials missing in .env")

PROJECT_ROOT = os.path.abspath( os.path.join(os.path.dirname(__file__), "../../") )

DATA_DIRECTORY = os.path.join( PROJECT_ROOT, "data" )

#PATH WHERE SESSION DATA IS SAVED [DON'T COMMIT THIS PATH !!!]
USER_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY, "session")

OUTPUT_FILE = os.path.join(DATA_DIRECTORY, "job_application.md")



