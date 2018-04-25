from collections import OrderedDict
from rows import export_to_txt, fields, Table

my_fields = OrderedDict([
    ('id', fields.IntegerField),
    ('summary', fields.TextField),
    ('component', fields.TextField),
    ('status', fields.TextField),
    ('resolution', fields.TextField),
    ('flags', fields.TextField),
    ('pm_score', fields.IntegerField),
    ('weburl', fields.TextField),
    ('requestee', fields.TextField),
])

GENERAL_EXPORT_FIELDS = (
    'id',
    'pm_score',
    'summary',
    'status',
    'resolution',
    'flags',
    )

NEEDSINFO_EXPORT_FIELDS = (
    'requestee',
    'weburl',
    'summary',
    )


def general_query_report(bugs):
    '''Print general Bugzilla query to stdout.'''
    bug_table = Table(fields=my_fields)

    for bug in bugs:
        flags = ', '.join([
            '{}{}'.format(bug['name'], bug['status'])
            for bug in bugs[0].flags
            if bug['is_active']]
                )
        bug_table.append(
            {
                'id': bug.id,
                'summary': bug.summary[:25],
                'component': bug.component,
                'status': bug.status,
                'resolution': bug.resolution,
                'flags': flags,
                'pm_score': bug.cf_pm_score,
            }
        )
    print(export_to_txt(bug_table, export_fields=GENERAL_EXPORT_FIELDS))


def needsinfo_query_report(bugs, requestee):
    '''Print general Bugzilla query to stdout.'''
    bug_table = Table(fields=my_fields)

    for bug in bugs:
        bug_table.append(
            {
                'requestee': requestee,
                'weburl': bug.weburl,
                'summary': bug.summary[:35],
            }
        )
    print(export_to_txt(bug_table, export_fields=NEEDSINFO_EXPORT_FIELDS))
