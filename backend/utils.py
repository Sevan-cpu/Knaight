import time
import torch
import functools
import psutil

def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        return (result, exec_time)
    return wrapper


def memory_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ram_info = psutil.virtual_memory()
        peak_mem_consumption = ram_info.used / 1024 / 1024 / 1024
        result, exec_time = func(*args, **kwargs)
        return round(peak_mem_consumption,2), round(exec_time,2), result
    return wrapper


@memory_decorator
@time_decorator
def generate_output(prompt, llm):
    outputs = llm(prompt)
    return outputs