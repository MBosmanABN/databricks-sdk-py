from datetime import timedelta

import pytest

from databricks.sdk.errors import NotFound, ResourceDoesNotExist
from databricks.sdk.retries import retried


def test_match_retry_condition_on_no_qualifier():
    with pytest.raises(SyntaxError):

        @retried()
        def foo():
            return 1


def test_match_retry_condition_on_conflict():
    with pytest.raises(SyntaxError):

        @retried(on=[IOError], is_retryable=lambda _: 'always')
        def foo():
            return 1


def test_match_retry_always():
    with pytest.raises(StopIteration):

        @retried(is_retryable=lambda _: 'always', timeout=timedelta(seconds=1))
        def foo():
            raise StopIteration()

        foo()


def test_match_on_errors():
    with pytest.raises(KeyError):

        @retried(on=[KeyError, AttributeError], timeout=timedelta(seconds=0.5))
        def foo():
            raise KeyError(1)

        foo()


def test_match_on_subclass():
    calls = []
    with pytest.raises(NotFound):

        @retried(on=[NotFound], timeout=timedelta(seconds=3))
        def foo():
            calls.append(1)
            raise ResourceDoesNotExist(...)

        foo()
    assert len(calls) > 1


def test_propagates_outside_exception():
    with pytest.raises(KeyError):

        @retried(on=[AttributeError], timeout=timedelta(seconds=0.5))
        def foo():
            raise KeyError(1)

        foo()
