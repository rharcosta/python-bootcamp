class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:  # args[0] = user
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Rubia")  # name = Rubia
new_user.is_logged_in = True
create_post(new_user)
