# -*- encoding: UTF-8 -*-

from enum import IntEnum


class LogType(IntEnum):
    CVN_STATUS = 0
    AUTH_ERROR = 1

LOG_TYPE = (
    (LogType.CVN_STATUS, 'CVN_STATUS'),
    (LogType.AUTH_ERROR, 'AUTH_ERROR'),
)

BASE_URL_FLATPAGES = '/investigacion/faq/'
