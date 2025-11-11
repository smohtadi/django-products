from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, ctx):
    response = exception_handler(exc, ctx)
    exc_name = exc.__class__.__name__
    message = "An unexpected error occurred"
    status_code = getattr(exc, "status_code", 500)
    errors = None

    if response is not None:
        message = exc.detail
        status_code = response.status_code
        if exc_name == "ValidationError":
            message = "Invalid parameters"
            errors = exc.detail

    problem = {
        "code": status_code,
        "message": message,
    }
    if errors is not None:
        problem["errors"] = errors
    response = Response(problem, status=status_code)
    response['Content-Type'] = "application/problem+json"
    return response
