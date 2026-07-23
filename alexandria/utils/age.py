from datetime import date


def age_in_days(birthday):

    return (date.today() - birthday).days


def age_in_months(birthday):

    days = age_in_days(birthday)

    return days // 30


def age_text(birthday):

    months = age_in_months(birthday)

    if months < 24:

        return f"{months} months"

    years = months // 12

    remaining = months % 12

    if remaining == 0:

        return f"{years} years"

    return f"{years} years {remaining} months"