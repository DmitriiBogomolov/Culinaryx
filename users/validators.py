from django.core.exceptions import ValidationError
import re


def validate_username(value, message="Имя пользователя должно состоять \
                        из латинских букв, цифр или знака подчеркивания."):

    reg = "[a-zA-Z_][0-9a-zA-Z_]*$"
    if re.match(reg, value) is None:
        raise ValidationError(
            message,
            code='message_is_wrong',
        )


def validate_name(value, message="Введите имя полностью."):

    reg = "[a-zA-Zа-яА-Я]+\s+[0-9a-zA-Zа-яА-Я_\s]*$"
    if re.match(reg, value) is None:
        raise ValidationError(
            message,
            code='name_is_wrong',
        )
