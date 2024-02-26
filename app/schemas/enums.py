import enum


class UserTypeEnum(enum.Enum):
    """
    UserType for the application users
    """

    admin = "admin"
    mentor = "mentor"
    trainee = "trainee"
