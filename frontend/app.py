"""Flask app which stores visit count in redis
"""
import time
import logging
import redis
from flask import Flask
import watchtower

APP = Flask(__name__)
CACHE = redis.Redis(host='redis-master', port=6379)

# setup cloudwatch logger
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(watchtower.CloudWatchLogHandler()) # fetch from env AWS configuration

def get_hit_count():
    """writes data to redis
    """
    retries = 5
    while True:
        try:
            return CACHE.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@APP.route('/')
def hit():
    """Entry point for the app
    """
    count = get_hit_count()
    LOGGER.info("website visited!")
    return 'I have been hit %i times since deployment.\n' % int(count)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", debug=True)
