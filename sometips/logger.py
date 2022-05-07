import logging


class Logger(object):
    def __init__(self, name=None):
        self.logger = logging.getLogger(name)
        self.msg_format = r'%(asctime)s.%(msecs)d %(levelname)s %(process)d-%(thread)d: %(message)s (%(filename)s:%(lineno)d)'
        self.date_format = '%Y-%m-%d %H:%M:%S'
        self.formatter = logging.Formatter(self.msg_format, self.date_format)
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)
        self.logger.setLevel(logging.INFO)

    def log(self, msg, level):
        self.logger.log(level, msg)

    def debug(self, msg):
        self.log(msg, logging.DEBUG)

    def info(self, msg):
        self.log(msg, logging.INFO)

    def warning(self, msg):
        self.log(msg, logging.WARNING)

    def warning_or_error(self, msg, error_condition=False):
        if not error_condition:
            self.warning(msg)
        else:
            self.error(msg)

    def error(self, msg):
        self.log(msg, logging.ERROR)

    def critical(self, msg):
        self.log(msg, logging.CRITICAL)

    def set_level(self, level):
        self.logger.setLevel(level)
