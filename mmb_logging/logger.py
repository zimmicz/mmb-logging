#!/usr/bin/env python3

import logging
import logging.handlers
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

def create_logger(config:dict):
    """Create logger.

    :param config with log_file, sentry_dsn
    """
    log_file = config['log_file']

    if hasattr(config, 'SENTRY_DSN'):
        sentry_sdk.init(
            dsn=config['SENTRY_DSN'],
            integrations=[FlaskIntegration()]
        )

    if (not os.path.exists(os.path.dirname(log_file))):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        open(log_file, 'a').close()

    rfh = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024 * 1024)
    rfh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rfh.setFormatter(formatter)

    return rfh

