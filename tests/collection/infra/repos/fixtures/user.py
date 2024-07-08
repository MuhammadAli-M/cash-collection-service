from domains.collection.infra.repos.user import User


def create_user():
    return User.objects.create_user(
        first_name="M",
        last_name="A",
        email="ma@g.com",
        password="12345"
    )
