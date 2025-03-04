import functools
import hashlib
import inspect
import sys
from collections.abc import Callable
from datetime import timedelta
from pathlib import Path
from typing import TypeVar, cast

import diskcache

F = TypeVar("F", bound=Callable)  # Generic type for any function


def key_func(func: Callable, ignore_self: bool, *args, **kwargs) -> str:
    """Generate a cache key based on the function and its arguments."""
    file_of_func = inspect.getsourcefile(func)
    if file_of_func is None:
        raise ValueError(f"Cannot get source file for {func.__name__}")

    hash_for_func_file = hashlib.sha256(Path(file_of_func).read_bytes()).hexdigest()

    args_str = []
    if ignore_self:
        args_str.append("<ignore-self>")
        args_str.extend(map(str, args[1:]))
    else:
        args_str.extend(map(str, args))

    args_str.extend(f"{k}={v}" for k, v in kwargs.items())

    return f"{func.__name__}({', '.join(args_str)}) @ {hash_for_func_file}"


def memoize(
    cache: diskcache.Cache, expire=timedelta(), ignore_self=False
) -> Callable[[F], F]:
    """
    Universal caching decorator for sync & async functions.

    Notes:
    - The function's cache key includes a hash of the file where it is defined.
    - This prevents stale caches after code updates.
    - Async generators are **not supported** because caching them would require
      collecting all values first.
    """

    def decorator(func: F) -> F:
        if inspect.isasyncgenfunction(func):
            sys.exit(
                "Caching async generators does not make sense. "
                "The caching function would need to collect all items before returning "
                "them, which would defeat the purpose of using an async generator."
            )

        def log_cache_hit(cache_key: str) -> None:
            print(f"📦 Using cached result for {cache_key}")

        def log_cache_miss(cache_key: str) -> None:
            print(f"✅ Cached result for {cache_key}")

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            cache_key = key_func(func, ignore_self, *args, **kwargs)

            cached = cache.get(cache_key)
            if cached is not None:
                log_cache_hit(cache_key)
                return cached
            else:
                result = await func(*args, **kwargs)  # Run async function
                cache.set(cache_key, result, expire=expire.total_seconds())
                log_cache_miss(cache_key)
                return result

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            cache_key = key_func(func, ignore_self, *args, **kwargs)

            cached = cache.get(cache_key)
            if cached is not None:
                log_cache_hit(cache_key)
                return cached
            else:
                result = func(*args, **kwargs)  # Run sync function
                cache.set(cache_key, result, expire=expire.total_seconds())
                log_cache_miss(cache_key)
                return result

        # Note: casting ensures correct return type for Pyright
        if inspect.iscoroutinefunction(func):
            return cast(F, async_wrapper)
        else:
            return cast(F, sync_wrapper)

    return decorator
