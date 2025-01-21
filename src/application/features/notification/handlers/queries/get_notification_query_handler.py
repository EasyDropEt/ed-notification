from rmediator.decorators import request_handler
from rmediator.types import RequestHandler

from src.application.common.responses.base_response import BaseResponse
from src.application.contracts.infrastructure.persistence.abc_unit_of_work import (
    ABCUnitOfWork,
)
from src.application.features.notification.dtos.notification_dto import NotificationDto
from src.application.features.notification.requests.queries import GetNotificationQuery
from src.common.logging_helpers import get_logger

LOG = get_logger()


@request_handler(GetNotificationQuery, BaseResponse[NotificationDto])
class GetNotificationQueryHandler(RequestHandler):
    def __init__(self, uow: ABCUnitOfWork):
        self._uow = uow

    async def handle(
        self, request: GetNotificationQuery
    ) -> BaseResponse[NotificationDto]:
        notification = self._uow.notification_repository.get(id=request.notification_id)

        return BaseResponse[NotificationDto].success(
            "Notification fetched successfully",
            NotificationDto(**notification),  # type: ignore
        )
