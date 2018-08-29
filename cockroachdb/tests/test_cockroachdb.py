# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.cockroachdb import CockroachdbCheck


def test_check(aggregator, instance):
    check = CockroachdbCheck('cockroachdb', {}, {}, [instance])
    check.check(instance)
    raise Exception('{}'.format(len(aggregator._metrics)))

    aggregator.assert_all_metrics_covered()
