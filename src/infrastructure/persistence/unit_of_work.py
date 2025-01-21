from src.application.contracts.infrastructure.persistence.abc_notification_repository import (
    ABCNotificationRepository,
)
from src.application.contracts.infrastructure.persistence.abc_unit_of_work import (
    ABCUnitOfWork,
)
from src.infrastructure.persistence.mongo_db_client import DbClient
from src.infrastructure.persistence.repositories.notification_repository import (
    NotificationRepository,
)


class UnitOfWork(ABCUnitOfWork):
    def __init__(self, db_client: DbClient) -> None:
        self._notification_repository = NotificationRepository(db_client)

    @property
    def notification_repository(self) -> ABCNotificationRepository:
        return self._notification_repository
