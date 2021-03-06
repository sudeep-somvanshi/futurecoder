import sys

import sentry_sdk
import snoop
from dryenv import DryEnv, populate_globals
from littleutils import setup_quick_console_logging
from sentry_sdk.integrations.django import DjangoIntegration

setup_quick_console_logging()


class Root(DryEnv):
    DEBUG = True

    SEPARATE_WORKER_PROCESS = False
    MASTER_URL = "http://localhost:5000/"

    SAVE_CODE_ENTRIES = True

    SENTRY_DSN = ""
    SECRET_KEY = 'kt1+4_u=ga%3v3@fy0@7c(&lq%)6tt=c+f-(ihd32@t$)i6gjm'
    GITHUB_TOKEN = ""


class MONITOR(DryEnv):
    ACTIVE = False
    THRESHOLD = 90
    MIN_PROCESSES = 1
    NUM_MEASUREMENTS = 3
    SLEEP_TIME = 5


snoop.install(enabled=Root.DEBUG, out=sys.__stderr__, columns=['thread'])

sentry_sdk.init(
    dsn=Root.SENTRY_DSN,
    integrations=[DjangoIntegration()],
    send_default_pii=True
)

populate_globals()
