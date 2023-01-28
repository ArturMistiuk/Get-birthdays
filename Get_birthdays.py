from datetime import datetime, timedelta
from collections import defaultdict


CURRENT_YEAR = datetime.now().year       # Current year constant


def get_birthdays_per_week(users):
    birthdays_this_week = defaultdict(list)  # Dictionary that creates days of birthdays as keys and names into values
    for user in users:  # Iterate over each person from users
        difference = (user['birthday'] - datetime.now()).days + 1  # Count how many days left to birthday from today
        if 7 >= difference >= 0:  # If birthday will be this week or Saturday/Sunday
            if user['birthday'].weekday() == 5 and (difference + 2) <= 7:  # If birthday on Saturday
                user['birthday'] += timedelta(days=2)  # Add 2 days to birthday
            elif user['birthday'].weekday() == 6 and (difference + 1) <= 7:  # If birthday on Sunday
                user['birthday'] += timedelta(days=1)  # Add 1 day to birthday
            elif user['birthday'].weekday() == 5 or user['birthday'].weekday() == 6:  # If birthday on Saturday/Sunday
                continue                                             # and Monday on the next week - skip this birthday
            birthdays_this_week[user['birthday'].strftime('%A')].append(user['name'])  # Add name and day to dictionary
    birthdays_this_week = dict(birthdays_this_week)                # Convert defaultdict to dict
    for birthday, person in birthdays_this_week.items():        # Iterate over each birthday this week
        print(f'{birthday}: {", ".join(person)}')             # Output day and name of people who has birthday


def main():

    # Function call example
    # people = [                           # Dictionary with information about colleagues
    #        {'name': 'Bill', 'birthday': datetime(year=CURRENT_YEAR, month=1, day=29)},
    #        {'name': 'Artur', 'birthday': datetime(year=CURRENT_YEAR, month=1, day=29)},
    #        {'name': 'Katya', 'birthday': datetime(year=CURRENT_YEAR, month=2, day=3)},
    #        ]
    #get_birthdays_per_week(people)


if __name__ == '__main__':
    main()
