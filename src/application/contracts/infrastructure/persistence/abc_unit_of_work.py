from abc import ABCMeta, abstractmethod

from src.application.contracts.infrastructure.persistence.abc_notification_repository import (
    ABCNotificationRepository,
)


class ABCUnitOfWork(metaclass=ABCMeta):
    @property
    @abstractmethod
    def notification_repository(self) -> ABCNotificationRepository: ...
