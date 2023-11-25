# Patchwork - automated patch tracking system
# Copyright (C) 2023 lichaoran <pkwarcraft@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later

import logging

from django.core.management import base

from patchwork.parser import getinfo

logger = logging.getLogger(__name__)


class Command(base.BaseCommand):
    help = 'get project series info from series id.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--id',
            help='series id to get info',
        )

    def handle(self, *args, **options):
        try:
            getinfo(options['id'])
        except Exception as e:
            logger.warning(f'get info failed: {e}')