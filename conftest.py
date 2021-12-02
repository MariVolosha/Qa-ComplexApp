"""Conftest"""
import logging


def pytest_runtest_setup(item):
    # item.cls.logger = logging.getLogger(".".join((item.module.__name__, item.cls.__name__, item.name)))
    item.cls.logger = logging.getLogger(item.name)
