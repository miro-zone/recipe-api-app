"""
Django command to wait for the database to be available.
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""
    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        max_tries = 10
        while db_up is False:
            max_tries -= 1
            try:
                if max_tries < 0 :
                    raise TimeoutError("Fail to connect with database.")
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, watiting 1 second...')
                time.sleep(1)
            except RuntimeError as e:
                self.stdout.write(e)

        self.stdout.write(self.style.SUCCESS("Database Avaialble!"))
