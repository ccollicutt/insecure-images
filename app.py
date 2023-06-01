import datetime
import os
import logging
import time
from flask import Flask
import threading
import sys
import logging.handlers

app = Flask(__name__)


@app.route("/")
def log_uid():
    now = datetime.datetime.now()
    userid = os.getuid()
    logging.info("application running as uid: %s", userid)
    return "Logged UID: {}".format(userid)


def thread_log(interval):
    while True:
        now = datetime.datetime.now()
        log_entry = "<{}> {}: application running as uid: {}".format(
            logging.handlers.SysLogHandler.LOG_USER,
            now.isoformat(),
            os.getuid(),
        )
        sys.stdout.write(log_entry + "\n")
        sys.stdout.flush()
        time.sleep(interval * 60)


def main():
    logging.basicConfig(level=logging.INFO)
    root_logger = logging.getLogger()
    root_logger.addHandler(logging.handlers.SysLogHandler())

    # Start the log thread
    log_thread = threading.Thread(target=thread_log, args=(1,))
    log_thread.daemon = True
    log_thread.start()

    app.run()


if __name__ == "__main__":
    main()
