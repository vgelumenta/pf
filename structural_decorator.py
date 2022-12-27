def decorator_text_uppercase(func):
    def wrapper():
        function = func()
        text_uppercase = function.upper()
        return text_uppercase
    return wrapper

def text():
    return 'anisah fanny'
decorated_result = decorator_text_uppercase(text)
print(decorated_result())