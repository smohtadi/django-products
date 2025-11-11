def is_integer(s) -> bool:
    try:
        int(s)
    except ValueError:
        return False
    return True