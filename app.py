import time
import datetime
import os
import logging

# Configure logging format and level
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

while True:
    now = datetime.datetime.now()
    userid = os.getuid()
    logging.info("application running as uid: %s", userid)
    time.sleep(30)
