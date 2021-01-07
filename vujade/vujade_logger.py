"""
Dveloper: vujadeyoon
E-mail: sjyoon1671@gmail.com
Github: https://github.com/vujadeyoon/vujade

Title: vujade_logger.py
Description: A module for logger
"""


import sys
import logging
import logging.handlers
from colorlog import ColoredFormatter


class vujade_logger:
    def __init__(self, _path_log, _mode='a', _fmt='[%(asctime)s] [%(levelname)s (%(process)s)]: %(message)s', _level=logging.DEBUG):
        self.path_log = _path_log
        self.mode = _mode
        self.fmt = _fmt
        self.level = _level
        self.log_colors = {
                'DEBUG': 'cyan',
                'INFO': 'white,bold',
                'INFOV': 'cyan,bold',
                'WARNING': 'yellow',
                'ERROR': 'red,bold',
                'CRITICAL': 'red,bg_white',
            }

    def get_logger(self):
        self.logger = logging.getLogger(name=__name__)
        self.logger.setLevel(level=self.level)
        self.logger_warnings = logging.getLogger("py.warnings")
        self._set_handler()

        return self.logger

    def _set_handler(self):
        logging.captureWarnings(True)

        if self.fmt is not None:
            formatter_file = logging.Formatter(fmt=self.fmt)
            formatter_stream = ColoredFormatter(fmt='%(log_color)s' + self.fmt, log_colors=self.log_colors)

        fileHandler = logging.FileHandler(filename=self.path_log, mode=self.mode)
        streamHandler = logging.StreamHandler()

        if self.fmt is not None:
            fileHandler.setFormatter(fmt=formatter_file)
            streamHandler.setFormatter(fmt=formatter_stream)

        self.logger.addHandler(hdlr=fileHandler)
        self.logger.addHandler(hdlr=streamHandler)
        self.logger_warnings.addHandler(hdlr=fileHandler)
        self.logger_warnings.addHandler(hdlr=streamHandler)


class vujade_print2logger:
    def __init__(self, _path_log, _mode='a'):
        self.path_log = _path_log
        self.mode = _mode
        self._run()

    def info(self, _str):
        print(_str)

    def close(self):
        sys.stdout = self.stdout_ori
        self.fp_log.close()

    def _run(self):
        self.stdout_ori = sys.stdout
        self.fp_log = open(self.path_log, self.mode)
        sys.stdout = self.fp_log
