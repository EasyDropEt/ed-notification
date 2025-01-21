from datetime import UTC, datetime

from ed_domain_model.entities.notification import NotificationType
from rmediator.decorators import request_handler
from rmediator.types import RequestHandler

from src.application.common.responses.base_response import BaseResponse
from src.application.contracts.infrastructure.email.abc_email_sender import (
    ABCEmailSender,
)
from src.application.contracts.infrastructure.persistence.abc_unit_of_work import (
    ABCUnitOfWork,
)
from src.application.contracts.infrastructure.sms.abc_sms_sender import ABCSmsSender
from src.application.features.notification.dtos import (
    NotificationDto,
    SendNotificationDto,
)
from src.application.features.notification.requests.commands.send_notification_command import (
    SendNotificationCommand,
)
from src.common.generic_helpers import get_new_id
from src.common.logging_helpers import get_logger

LOG = get_logger()


@request_handler(SendNotificationCommand, BaseResponse[NotificationDto])
class SendNotificationCommandHandler(RequestHandler):
    def __init__(
        self,
        uow: ABCUnitOfWork,
        email_sender: ABCEmailSender,
        sms_sender: ABCSmsSender,
    ):
        self._uow = uow
        self._email_sender = email_sender
        self._sms_sender = sms_sender

    async def handle(
        self, request: SendNotificationCommand
    ) -> BaseResponse[NotificationDto]:
        dto: SendNotificationDto = request.dto
        created = self._uow.notification_repository.create(
            {
                "id": get_new_id(),
                "user_id": dto["user_id"],
                "message": dto["message"],
                "read_status": False,
                "created_datetime": datetime.now(UTC),
                "notification_type": dto["notification_type"],
            }
        )

        return BaseResponse[NotificationDto].success(
            "Notification sent",
            NotificationDto(**created),  # type: ignore
        )
