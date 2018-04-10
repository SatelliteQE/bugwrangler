'''Collection of Bugzilla queries.'''


def qe_test_coverage(config, product, flags, start, end):
    """Fetch automation coverage from Bugzilla."""
    query = config.bugzilla.build_query(
        product='Red Hat Satellite 6',
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
        query['f{0}'.format(query_fields)] = 'flagtypes.name'
        query['v{0}'.format(query_fields)] = flag
        query['o{0}'.format(query_fields)] = 'substring'

    query["include_fields"] = [
        'id',
        'summary',
        'component',
        'status',
        'resolution',
        'flags',
        'weburl',
        'cf_pm_score',
        ]
    if config.verbose:
        print(query)

    return config.bugzilla.query(query)
