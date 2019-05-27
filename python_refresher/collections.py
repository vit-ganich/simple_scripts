list_grades = [1, 2, 3, 4]
tuple_grades = (1, 2, 3, 4)  # immutable
set_grades = {1, 2, 3, 4, 4, 4}  # unique and unordered

list_grades.append(5)

tuple_one = (10,)  # need to place comma at the end
first_set = {1, 2, 3, 4, 5}
second_set = {2, 4, 6, 8}

# Get common values for two sets
print(first_set.intersection(second_set))  # {2, 4}
print(first_set.union(second_set))  # {1, 2, 3, 4, 5, 6, 8}
print({1, 2, 3, 4}.difference({1, 2, 4}))  # {3}


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def who_do_you_know() -> list:
    people = input("Enter your friends (comma-separated): ")
    # We need to remove spaces and normalize names
    people_stripped = [item.strip().lower() for item in people.split(",")]
    return people_stripped


def ask_user():
    person = input("Enter a person you know: ").lower().strip()
    if person in who_do_you_know():
        print(f"You know {person}")
    else:
        print("You don't know him / her")


#ask_user()


def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)