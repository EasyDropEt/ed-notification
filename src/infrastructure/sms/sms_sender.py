import http.client
import json

from src.application.contracts.infrastructure.sms.abc_sms_sender import ABCSmsSender


class SmsSender(ABCSmsSender):
    def __init__(self, api_key: str) -> None:
        self._api_key = (
            "3b90100ee093d3b100d908b1d2aa7587-77d8fec0-0f48-4dce-b082-2e1e47c60bca"
        )

    async def send(self, recipient: str, message: str) -> None:
        conn = http.client.HTTPSConnection("kq13q8.api.infobip.com")
        payload = json.dumps(
            {
                "name": "2fa test application",
                "enabled": True,
                "configuration": {
                    "pinAttempts": 10,
                    "allowMultiplePinVerifications": True,
                    "pinTimeToLive": "15m",
                    "verifyPinLimit": "1/3s",
                    "sendPinPerApplicationLimit": "100/1d",
                    "sendPinPerPhoneNumberLimit": "10/1d",
                },
                "pinType": "NUMERIC",
                "messageText": "Your pin is {{pin}}",
                "pinLength": 4,
                "senderId": "ServiceSMS",
            }
        )
        headers = {
            "Authorization": "App 3b90100ee093d3b100d908b1d2aa7587-77d8fec0-0f48-4dce-b082-2e1e47c60bca",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        conn.request("POST", "/2fa/2/applications", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
