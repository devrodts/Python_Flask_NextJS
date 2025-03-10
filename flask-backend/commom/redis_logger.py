import logging
import redis


class RedisHandler(logging.Handler):
    def __init__(self, host='redis', port=6379, db=0, key='logs'):
        super().__init__()
        self.redis_client = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        self.key = key

    def emit(self, record):
        try:
            log_entry = self.format(record)
            self.redis_client.rpush(self.key, log_entry)
        except Exception:
            self.handleError(record)

def setup_redis_logging(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    redis_handler = RedisHandler(host='redis', port=6379, db=0, key='logs')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    redis_handler.setFormatter(formatter)
    logger.addHandler(redis_handler)
    return logger
