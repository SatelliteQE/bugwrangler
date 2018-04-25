'''Collection of Bugzilla queries.'''
from bugwrangler.constants import QUERY_FIELDS


def needs_info(config, product, requestee):
    '''Fetch Bigzilla issues waiting for information from requestee.'''
    query = config.bugzilla.build_query(
        product=product,
    )

    query['f1'] = 'requestees.login_name'
    query['o1'] = 'equals'
    query['v1'] = requestee
    query['query_format'] = 'advanced'

    query["include_fields"] = QUERY_FIELDS

    if config.verbose:
        print(query)

    return config.bugzilla.query(query)


def qe_test_coverage(config, product, flags, start, end):
    '''Fetch automation coverage from Bugzilla.'''
    query = config.bugzilla.build_query(
        product=product,
    )

    # Do we care about date range?
    if start:
        query['chfieldfrom'] = start
    if end:
        query['chfieldto'] = end

    # Filtering for either of the following 2 flags
    query['f1'] = 'OP'
    query['j1'] = 'OR'

    # Filtering excludes the following component
    query['f2'] = 'CP'

    # Filtering
    query['f3'] = 'component'
    query['v3'] = 'Doc'
    query['o3'] = 'casesubstring'
    query['n3'] = '1'

    query['f4'] = 'external_bugzilla.description'
    query['v4'] = 'Red Hat Customer Portal'
    query['o4'] = 'substring'

    # Total number of fields used so far
    query_fields = 4
    for flag in flags:
        # Filtering for coverage flag
        query_fields += 1
        query[f'f{query_fields}'] = 'flagtypes.name'
        query[f'v{query_fields}'] = flag
        query[f'o{query_fields}'] = 'substring'

    query["include_fields"] = QUERY_FIELDS

    if config.verbose:
        print(query)

    return config.bugzilla.query(query)
