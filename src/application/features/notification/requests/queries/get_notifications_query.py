from dataclasses import dataclass
from uuid import UUID

from rmediator.decorators import request
from rmediator.types import Request

from src.application.common.responses.base_response import BaseResponse
from src.application.features.notification.dtos.notification_dto import NotificationDto


@request(BaseResponse[list[NotificationDto]])
@dataclass
class GetNotificationsQuery(Request):
    user_id: UUID
