def required_method(methods: list = []):
    def decorator(view):
        def wrapper(request, *args, **kwargs):
            if request['method'] in methods:
                return view(request, *args, **kwargs)
            else:
                return 'method not allow'
        return wrapper
    return decorator


@required_method(['POST'])
def get_user(request, *args, **kwargs):
    return 'request success'


print(get_user({'method': 'POST'}))
print(get_user({'method': 'GET'}))
