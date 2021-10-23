from django.core.exceptions import PermissionDenied


def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wrapper(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return func(request, *args, **kwargs)
            else:
                raise PermissionDenied

        return wrapper

    return decorator
