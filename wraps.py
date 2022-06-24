from functools import wraps


def required_b_not_zero(func):
    @wraps(func)
    def check_b_is_zero(a: int, b: int):
        if b == 0:
            return 'cannot div'
        else:
            return func(a, b)

    return check_b_is_zero


@required_b_not_zero
def div(a: int, b: int):
    return a/b


print(div(1, 1))
print(div(1, 0))
