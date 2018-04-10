"""Constants for the project."""

REJECTED = "qe_test_coverage-"
AUTOMATED = "qe_test_coverage+"

BACKLOG = "qe_test_coverage?"
BACKLOG_BUGZILLA_STATUS = [
    'NEW',
    'ASSIGNED',
    'POST',
    'MODIFIED',
    'ON_DEV',
]

BUGZILLA_URL = "https://bugzilla.redhat.com/xmlrpc.cgi"
BUGZILLA_QUERY_URL = "https://bugzilla.redhat.com/query.cgi"
BUGZILLA_STATUS = [
    'NEW',
    'ASSIGNED',
    'POST',
    'MODIFIED',
    'ON_DEV',
    'ON_QA',
    'VERIFIED',
    'RELEASE_PENDING',
    'CLOSED',
]
EXCLUDED_KEYWORDS = [
    'ABIAssurance',
    'FutureFeature',
    'HardwareEnablement',
    'Improvement',
    'ReleaseNotes',
    'SecurityTracking',
    'Task',
    'TechPreview',
    'TestOnly',
    'Tracking',
]
