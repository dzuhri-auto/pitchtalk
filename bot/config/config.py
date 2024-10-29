import json
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    LICENSE_KEY = os.getenv("LICENSE_KEY")

    USE_RANDOM_DELAY_IN_RUN = os.getenv("USE_RANDOM_DELAY_IN_RUN", "True")
    RANDOM_DELAY_IN_RUN = json.loads(os.getenv("RANDOM_DELAY_IN_RUN", "[3, 15]"))

    REF_ID = os.getenv("REF_ID")

    USE_PROXY_FROM_FILE = os.getenv("USE_PROXY_FROM_FILE", "False")

settings = Settings()
