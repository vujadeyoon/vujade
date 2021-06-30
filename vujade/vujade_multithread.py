"""
from abc import *
Dveloper: vujadeyoon
E-mail: sjyoon1671@gmail.com
Github: https://github.com/vujadeyoon/vujade

Title: vujade_multithread.py
Description: A module for multi-thread
"""


import abc


class ThreadBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _lock(self):
        pass

    @abc.abstractmethod
    def _unlock(self):
        pass
