from ed_notification.common.generic_helpers import get_config
from ed_notification.common.logging_helpers import get_logger
from ed_notification.webapi.api import API

LOG = get_logger()


class Package:
    def __init__(self) -> None:
        self._config = get_config()
        self._api = API(
            title="ED Notification Service",
            description="Notification service for the ED project",
            version="1.0.0",
        )

    def start(self) -> None:
        self._api.start()

    def stop(self) -> None:
        self._api.stop()


if __name__ == "__main__":
    main = Package()

    main.start()
