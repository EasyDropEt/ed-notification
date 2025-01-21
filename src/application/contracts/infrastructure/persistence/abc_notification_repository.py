from abc import ABCMeta

from ed_domain_model.entities.notification import Notification

from src.application.contracts.infrastructure.persistence.abc_generic_repository import (
    ABCGenericRepository,
)


class ABCNotificationRepository(
    ABCGenericRepository[Notification],
    metaclass=ABCMeta,
): ...
