def configure_plugin_decorator(func):
    def wrapper(*args):
        return func(**dict(args))

    return wrapper
