BugWrangler
===========

Introduction
------------

**BugWrangler** is a small tool I built to perform some queries against [Red Hat](http://redhat.com)'s [Bugzilla](https://bugzilla.redhat.com), though it could also be used against other Bugzilla installations, and provide me with reports and metrics. Right now it can output queries to standard output.

Installation
------------

Installation is still manual:

1. Clone the `bugwrangler` repository to your computer.
2. Install it by running `pip install -r requirements.txt`

Usage
-----

    bugwrangler --help
    Usage: bugwrangler [OPTIONS] COMMAND [ARGS]...

    CLI object.

    Options:
    --help  Show this message and exit.

    Commands:
    coverage  Display Bugzilla issue automation status.

    bugwrangler coverage --help
    Usage: bugwrangler coverage [OPTIONS]

    Display Bugzilla issue automation status.

    Options:
    --product TEXT    Product name  [required]
    -f, --flags TEXT  Which Bugzilla flag to use.
    --start TEXT      Start date range.
    --end TEXT        End date range.
    --report
    -v, --verbose
    --help            Show this message and exit.

Examples
--------

All **Red Hat Satellite 6** issues with `flags` *qe_test_coverage+* and *sat-6.4.0+*

    $ bugwrangler coverage --product 'Red Hat Satellite 6' -f 'qe_test_coverage+' -f'sat-6.4.0+'
    qe_test_coverage+, sat-6.4.0+ = 2

Now, generate a report for the same query

    $ bugwrangler coverage --product 'Red Hat Satellite 6' -f 'qe_test_coverage+' -f'sat-6.4.0+' --report
    qe_test_coverage+, sat-6.4.0+ = 2
    +---------+----------+---------------------------+--------+------------+----------------------------------------------------------------------------------------+
    |    id   | pm_score |          summary          | status | resolution |                                         flags                                   |
    +---------+----------+---------------------------+--------+------------+----------------------------------------------------------------------------------------+
    | 1177766 |     -269 | [RFE] Republish composite |   POST |            | needinfo?, qe_test_coverage+, sat-6.4.0+, devel_triaged+, pm_ack+, devel_ack+, qa_ack+ |
    | 1449011 |      678 | [RFE] Ansible integration |    NEW |            | needinfo?, qe_test_coverage+, sat-6.4.0+, devel_triaged+, pm_ack+, devel_ack+, qa_ack+ |
    +---------+----------+---------------------------+--------+------------+----------------------------------------------------------------------------------------+

Find all issues with a `needsinfo` on user `bart@example.com`

    $ bugwrangler needsinfo --product 'Red Hat Satellite 6' -r bart@example.com
    bart@example.com
    https://bugzilla.redhat.com/show_bug.cgi?id=1439344

Find all issues with a `needsinfo` for multiple users

    $ bugwrangler needsinfo --product 'Red Hat Satellite 6' -r bart@example.com -r homer@example.com
    bart@example.com
    https://bugzilla.redhat.com/show_bug.cgi?id=1439344
    homer@example.com
    https://bugzilla.redhat.com/show_bug.cgi?id=1370952
    https://bugzilla.redhat.com/show_bug.cgi?id=1181283
    https://bugzilla.redhat.com/show_bug.cgi?id=1334863

Now, generate a report for the same query

    $ bugwrangler needsinfo --product 'Red Hat Satellite 6' -r bart@example.com -r homer@example.com --report
    +---------------------+-----------------------------------------------------+-------------------------------------+
    |      requestee      |                        weburl                       |               summary               |
    +---------------------+-----------------------------------------------------+-------------------------------------+
    | bart@example.com    | https://bugzilla.redhat.com/show_bug.cgi?id=1439344 | pulp-admin throws exception on a ca |
    +---------------------+-----------------------------------------------------+-------------------------------------+

    +--------------------+-----------------------------------------------------+-------------------------------------+
    |     requestee      |                        weburl                       |               summary               |
    +--------------------+-----------------------------------------------------+-------------------------------------+
    | homer@example.com  | https://bugzilla.redhat.com/show_bug.cgi?id=1370952 | RHEL6 Satellite 6.2 upgrade error - |
    | homer@example.com  | https://bugzilla.redhat.com/show_bug.cgi?id=1181283 | error when changing fqdn and updati |
    | homer@example.com  | https://bugzilla.redhat.com/show_bug.cgi?id=1334863 | VDC guest subscriptions do not list |
    +--------------------+-----------------------------------------------------+-------------------------------------+
