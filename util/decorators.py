def ignore_own_message(func):
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)
    return wrapped
