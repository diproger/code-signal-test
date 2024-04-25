import time
import psutil
from rest_framework.response import Response
from rest_framework import status


class ExecutionTimeLimitMixin:
    def dispatch(self, request, *args, **kwargs):
        # Execution time as needed
        timeout = 4
        start_time = time.time()

        response = super().dispatch(request, *args, **kwargs)

        elapsed_time = time.time() - start_time

        if elapsed_time > timeout:
            return Response({'error': 'Execution time limit exceeded'}, status=status.HTTP_400_BAD_REQUEST)

        return response


class MemoryUsageLimitMixin:
    def dispatch(self, request, *args, **kwargs):
        max_memory_usage = 1024 * 1024 * 1024
        current_memory_usage = psutil.virtual_memory().used
        if current_memory_usage > max_memory_usage:
            return Response({'error': 'Memory limit exceeded'}, status=status.HTTP_400_BAD_REQUEST)
        return super().dispatch(request, *args, **kwargs)
