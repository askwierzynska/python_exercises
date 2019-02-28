import datetime


def print_header():
    print('...........................')
    print('           bday')
    print('...........................')
    print('')


def get_birthday():
    print('When were you born?')
    year = int(input('Year? [yyyy] '))
    month = int(input('Month? [mm] '))
    day = int(input('Day? [dd] '))
    special_day = datetime.date(year, month, day)
    return special_day


def calc_date(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dif = this_year - target_date
    return dif.days


def resume(days):
    if days < 0:
        print('Your birthday was {0} days ago.'.format(-days))

    elif days > 0:
        print('Your birthday is coming in {0} days!'.format(days))

    else:
        print('Today is your birthday! Happy birthday!')


def main():
    print_header()
    bday = get_birthday()
    today = datetime.date.today()
    difference = calc_date(bday, today)
    resume(difference)


main()


