from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from idiomatic.models import Estudiante

def is_student_registered(function):
    def wrap(request, *args, **kwargs):
        if "estudiante" in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect("create_student")

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
