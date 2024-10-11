import logging
from pythonjsonlogger import jsonlogger

import threading

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter('%(timestamp)s %(levelname)s %(message)s ', timestamp=True)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


def __generate_random_logs_daemon():
    import random
    import time
    while True:
        time.sleep(random.randint(1, 5))
        random_number = random.randint(1, 3)

        if random_number == 1:
            logger.info("This is an info message")
        elif random_number == 2:
            logger.warning("This is a warning message")
        else:
            logger.error("This is an fun message")


def start_random_logs():
    threading.Thread(target=__generate_random_logs_daemon).start()
