from ed_domain_model.entities.notification import Notification

from src.application.contracts.infrastructure.persistence.abc_notification_repository import (
    ABCNotificationRepository,
)
from src.infrastructure.persistence.db_client import DbClient
from src.infrastructure.persistence.helpers import repository_class
from src.infrastructure.persistence.repositories.generic_repository import (
    MongoGenericRepository,
)


@repository_class
class NotificationRepository(
    MongoGenericRepository[Notification], ABCNotificationRepository
):
    def __init__(self, db_client: DbClient) -> None:
        super().__init__(db_client, "notification")
