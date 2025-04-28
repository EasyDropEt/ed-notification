from threading import Thread

from ed_domain.queues.ed_notification.notification_model import \
    NotificationModel
from ed_infrastructure.queues.rabbitmq.subscriber import RabbitMQSubscriber

from ed_notification.common.generic_helpers import get_config
from ed_notification.common.logging_helpers import get_logger
from ed_notification.webapi.api import API

LOG = get_logger()


class Package:
    def __init__(self) -> None:
        self._config = get_config()
        self._api = API()
        self._rabbitmq_subscriber = RabbitMQSubscriber[NotificationModel](
            self._config["rabbitmq"]["url"],
            self._config["rabbitmq"]["queue"],
        )

    def start_subscriber(self) -> None:
        self._rabbitmq_subscriber.start()

    def start_api(self) -> None:
        self._api.start()

    def stop(self) -> None:
        self._api.stop()
        self._rabbitmq_subscriber.stop()


if __name__ == "__main__":
    main = Package()

    subscriber_thread = Thread(target=main.start_subscriber, daemon=False)

    subscriber_thread.start()
    main.start_api()
