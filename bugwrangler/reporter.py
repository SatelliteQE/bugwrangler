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
])

fields_to_export = (
    'id',
    'pm_score',
    'summary',
    'status',
    'resolution',
    'flags',
    )


def print_table(bugs):
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
    print(export_to_txt(bug_table, export_fields=fields_to_export))
