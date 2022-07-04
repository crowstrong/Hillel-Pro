"""
    source of def object_memory(count):
    https://habr.com/ru/post/193890/

    source of LFUCache:
    https://www.geeksforgeeks.org/cachetools-module-in-python/
    https://github.com/rfyiambest/pylfu/blob/master/pylfu/pylfu.py

"""
import functools
# import sys
# import tracemalloc
import psutil
import os
# from cachetools import cached, LFUCache
from collections import OrderedDict

import requests


# def object_memory(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Function: {func.__name__}, use: {sys.getsizeof(result)} bytes')
#         return result
#
#     return wrapper

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def object_memory(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))

        return result

    return wrapper


@object_memory
def lfu_cache_decorator(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            cache_key = (*args, tuple(kwargs.items()))
            if cache_key in wrapper._cache:
                wrapper._cache[cache_key]['freq'] += 1
                return wrapper._cache[cache_key]['value']
            result = f(*args, **kwargs)
            if len(wrapper._cache) >= max_limit:
                min_freq = min(wrapper._cache.values(), key=lambda x: x['freq'])['freq']
                for k, v in wrapper._cache.items():
                    if v['freq'] == min_freq:
                        del wrapper._cache[k]
                        break
            wrapper._cache[cache_key] = {'value': result, 'freq': 1}

            return result

        wrapper._cache = OrderedDict()

        return wrapper

    return internal


@object_memory
# @cached(LFUCache(maxsize=2))
@lfu_cache_decorator(max_limit=2)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    if first_n:
        return res.content[:first_n]
    else:
        return res.content


if __name__ == '__main__':
    fetch_url('https://www.google.com')
    fetch_url('https://www.google.com')
    fetch_url('https://www.google.com')
    fetch_url('https://www.google.com')
    fetch_url('https://www.youtube.com')
    fetch_url('https://ithillel.ua')
