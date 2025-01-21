from uuid import UUID

from fastapi import APIRouter, Depends, WebSocket
from rmediator.decorators.request_handler import Annotated
from rmediator.mediator import Mediator

from src.application.features.notification.dtos import (
    NotificationDto,
    SendNotificationDto,
    UpdateNotificationDto,
)
from src.application.features.notification.requests.commands import (
    SendNotificationCommand,
    UpdateNotificationCommand,
)
from src.application.features.notification.requests.queries import (
    GetNotificationQuery,
    GetNotificationsQuery,
)
from src.common.logging_helpers import get_logger
from src.webapi.common.helpers import GenericResponse, rest_endpoint
from src.webapi.dependency_setup import mediator

LOG = get_logger()
router = APIRouter(prefix="/notifcations", tags=["Notification Feature"])


@router.post("")
async def send_notification(
    request: SendNotificationDto,
    mediator: Annotated[Mediator, Depends(mediator)],
):
    return await mediator.send(SendNotificationCommand(dto=request))


@router.get("/{notification_id}", response_model=GenericResponse[NotificationDto])
@rest_endpoint
async def get_notification_by_id(
    notification_id: UUID,
    mediator: Annotated[Mediator, Depends(mediator)],
):
    return await mediator.send(GetNotificationQuery(notification_id=notification_id))


@router.patch("/{notification_id}", response_model=GenericResponse[NotificationDto])
@rest_endpoint
async def update_notification(
    notification_id: UUID,
    request: UpdateNotificationDto,
    mediator: Annotated[Mediator, Depends(mediator)],
):
    return await mediator.send(
        UpdateNotificationCommand(notification_id=notification_id, dto=request)
    )


@router.get("/users/{user_id}", response_model=GenericResponse[list[NotificationDto]])
@rest_endpoint
async def get_notifications_for_user(
    user_id: UUID,
    mediator: Annotated[Mediator, Depends(mediator)],
):
    return await mediator.send(GetNotificationsQuery(user_id=user_id))


@router.websocket("/{user_id}")
async def websocket(user_id: UUID, ws: WebSocket) -> None:
    await ws.accept()

    while True:
        data = await ws.receive_text()
        await ws.send_text(f"Message text was: {data}")
