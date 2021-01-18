import re


def count_digits(password):
    return sum(character.isdigit() for character in password)


def valid_password(password):
    if len(password) >= 8 and password.isalnum() and count_digits(password) >= 2:
        return True
    return False


def get_user_info(user):
    return {
        "phone": user.telephone,
        "city": user.city,
        "information": user.information,
        "link_vk": user.vk,
        "link_facebook": user.facebook,
        "link_instagram": user.instagram
    }


def get_all_user_info(user):
    obj = user.get_info()
    obj["first_name"] = user.First_name
    obj["surname"] = user.Surname
    obj["middle name"] = user.Middle_name
    obj["email"] = user.email
    return obj
