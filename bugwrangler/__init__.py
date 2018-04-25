"""
Fetch automation status from Bugzilla for a Red Hat product.
"""

from __future__ import print_function

from requests.exceptions import ConnectionError

import bugzilla
import click
import os
import sys

from bugwrangler.constants import (
    AUTOMATED,
    BUGZILLA_URL,
    )
from bugwrangler.queries import needs_info, qe_test_coverage
from bugwrangler.reporter import needsinfo_query_report, general_query_report


class Config(object):
    """Store Bugzilla attributes for all methods."""

    def __init__(self):
        self.user = os.environ.get('BUGZILLA_USER_NAME', None)
        self.password = os.environ.get('BUGZILLA_USER_PASSWORD', None)
        self.bugzilla = bugzilla.Bugzilla(url=BUGZILLA_URL)

        # Get a valid web session if credentials are available.
        if not self.user and not self.password:
            click.echo('Please provide valid Bugzilla credentials!')
            sys.exit(-1)

        try:
            self.session = self.bugzilla.login(
                user=self.user,
                password=self.password)
        except ConnectionError as err:
            click.echo("Could not connect to Bugzilla: {0}".format(err))
            sys.exit(-1)


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
def cli():
    """CLI object."""
    pass


@cli.command()
@click.option(
    '--product',
    required=True,
    type=str,
    help=("Product name"),
)
@click.option(
    '--flags',
    '-f',
    default=[AUTOMATED],
    help='Which Bugzilla flag to use.',
    multiple=True,
    type=str,
)
@click.option(
    '--start',
    default=None,
    help="Start date range."
)
@click.option(
    '--end',
    default='Now',
    help="End date range."
)
@click.option('--report', is_flag=True)
@click.option('--verbose', '-v', is_flag=True)
@pass_config
def coverage(config, product, flags, start, end, report, verbose):
    """Display Bugzilla issue automation status."""
    config.verbose = verbose
    bugs = qe_test_coverage(config, product, flags, start, end)
    bug_count = len(bugs)

    click.echo("{} = {}".format(
        ', '.join(flags), bug_count
        ))
    if report:
        general_query_report(bugs)


@click.group()
def cli():
    """CLI object."""
    pass


@cli.command()
@click.option(
    '--product',
    required=True,
    type=str,
    help=("Product name"),
)
@click.option(
    '--requestee',
    '-r',
    default=[AUTOMATED],
    help='Bugzilla user email.',
    multiple=True,
    type=str,
)
@click.option('--report', is_flag=True)
@click.option('--verbose', '-v', is_flag=True)
@pass_config
def needsinfo(config, product, requestee, report, verbose):
    """Display Bugzilla issues with needsinfo status."""
    config.verbose = verbose

    for contact in requestee:
        bugs = needs_info(config, product, contact)
        if report:
            needsinfo_query_report(bugs, contact)
        else:
            click.echo(f'{contact}')
            for bug in bugs:
                click.echo(f'{bug.weburl}')
