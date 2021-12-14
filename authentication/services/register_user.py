from authentication import models as authentication_models


def register_user(*, name: str, email: str, password: str):
    user = authentication_models.User(name=name, email=email,)
    if password is not None:
        user.set_password(password)
    user.save()
    return user
