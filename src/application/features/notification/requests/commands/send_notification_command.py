from dataclasses import dataclass

from rmediator.decorators import request
from rmediator.types import Request

from src.application.common.responses.base_response import BaseResponse
from src.application.features.notification.dtos import (
    NotificationDto,
    SendNotificationDto,
)


@request(BaseResponse[NotificationDto])
@dataclass
class SendNotificationCommand(Request):
    dto: SendNotificationDto
