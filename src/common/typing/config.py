from typing import TypedDict


class Config(TypedDict):
    resend_api_key: str
    infobig_key: str
    mongo_db_connection_string: str
    db_name: str


class TestMessage(TypedDict):
    title: str
