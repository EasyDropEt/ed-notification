from rmediator.mediator import Mediator

from src.application.features.notification.handlers.commands import (
    SendNotificationCommandHandler,
    UpdateNotificationCommandHandler,
)
from src.application.features.notification.handlers.queries import (
    GetNotificationQueryHandler,
    GetNotificationsQueryHandler,
)
from src.application.features.notification.requests.commands import (
    SendNotificationCommand,
    UpdateNotificationCommand,
)
from src.application.features.notification.requests.queries import (
    GetNotificationQuery,
    GetNotificationsQuery,
)
from src.common.generic_helpers import get_config
from src.infrastructure.email.email_sender import EmailSender
from src.infrastructure.persistence.db_client import DbClient
from src.infrastructure.persistence.unit_of_work import UnitOfWork
from src.infrastructure.sms.sms_sender import SmsSender


def mediator() -> Mediator:
    # Dependencies
    config = get_config()
    db_client = DbClient(config["mongo_db_connection_string"], config["db_name"])
    uow = UnitOfWork(db_client)
    email_sender = EmailSender(config["resend_api_key"])
    sms_sender = SmsSender(config["infobig_key"])

    # Setup
    mediator = Mediator()

    requests_and_handlers = [
        (
            SendNotificationCommand,
            SendNotificationCommandHandler(uow, email_sender, sms_sender),
        ),
        (
            UpdateNotificationCommand,
            UpdateNotificationCommandHandler(uow, email_sender, sms_sender),
        ),
        (GetNotificationQuery, GetNotificationQueryHandler(uow)),
        (GetNotificationsQuery, GetNotificationsQueryHandler(uow)),
    ]

    for request, handler in requests_and_handlers:
        mediator.register_handler(request, handler)

    db_client.start()
    return mediator
