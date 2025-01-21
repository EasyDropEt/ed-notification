from threading import Thread

from src.common.generic_helpers import get_config
from src.common.logging_helpers import get_logger
from src.infrastructure.rabbitmq.subscriber import RabbitMQSubscriber, example_callback
from src.webapi.api import API

LOG = get_logger()


class Package:
    def __init__(self) -> None:
        self._rabbitmq_subscriber = RabbitMQSubscriber("notification")
        self._api = API()
        self._config = get_config()

        print(self._config)

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
