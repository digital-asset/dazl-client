# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import CancelledError, sleep
from datetime import datetime, timedelta
from typing import Awaitable, Callable, TypeVar

from grpc import RpcError, StatusCode

T = TypeVar("T")

DEFAULT_TIMEOUT = timedelta(minutes=1)


def is_retryable_exception(ex: Exception) -> bool:
    if not isinstance(ex, RpcError):
        return False

    # TODO: Expand on these categories as documented here:
    #  https://docs.daml.com/app-dev/grpc/error-codes.html
    status = ex.code()
    if status == StatusCode.UNAVAILABLE:
        return True
    elif status == StatusCode.FAILED_PRECONDITION and ex.details().startswith(
        "PARTY_ALLOCATION_WITHOUT_CONNECTED_DOMAIN"
    ):
        return True

    return False


async def retry(
    fn: Callable[[], Awaitable[T]],
    *,
    retry_safe_ex: Callable[[Exception], bool] = is_retryable_exception,
    timeout: timedelta = DEFAULT_TIMEOUT
) -> T:
    a, b = 0, 1
    start = datetime.utcnow()
    while True:
        try:
            return await fn()
        except CancelledError:
            raise
        except Exception as ex:
            if (datetime.utcnow() - start) <= timeout and retry_safe_ex(ex):
                # retry in increasing intervals according to the Fibonacci sequence;
                # exponential backoff generally makes us wait too long
                a, b = b, a + b
                await sleep(a)
            else:
                raise
