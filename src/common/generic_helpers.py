import os
from uuid import UUID, uuid4

from dotenv import load_dotenv

from src.common.typing.config import Config


def get_new_id() -> UUID:
    return uuid4()


def get_config() -> Config:
    load_dotenv()

    return {
        "resend_api_key": os.getenv("RESEND_KEY") or "",
        "mongo_db_connection_string": os.getenv("MONGO_DB_KEY") or "",
        "db_name": os.getenv("DB_NAME") or "",
        "infobig_key": os.getenv("INFOBIG_KEY") or "",
    }
