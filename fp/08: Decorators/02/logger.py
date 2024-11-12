def args_logger(*args, **kwargs):
    if args:
        args_lst = [f"{i + 1}. {x}" for i, x in enumerate(args)]
        args_str = "\n".join(args_lst)
        print(args_str)

    if kwargs:
        kwargs_lst = [f"* {key}: {val}" for key, val in kwargs.items()]
        kwargs_str = "\n".join(kwargs_lst)
        print(kwargs_str)
