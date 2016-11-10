def _func2():
    try:
        with open('/non_existing_path') as f:
            f.read()
    except IOError:
        other_func()


def other_func():
    raise raise_func()


def raise_func():
    raise RuntimeError('asd')
