""" This module contains the Profiler class, which is used to profile the execution time of a function.

    Example usage:

    from data_analysis.profiler import Profiler

    @Profiler
    def function_to_profile():
        # Do something
        return None

    function_to_profile()

    """

import time
from memory_profiler import profile

class Profiler:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.start_time = time.time()
        result = self.func(*args, **kwargs)
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        print(f"Execution time: {self.execution_time} seconds")
        return result

    @profile
    def profile_memory(self, *args, **kwargs):
        return self.func(*args, **kwargs)
