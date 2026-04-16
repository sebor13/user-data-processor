def validate_name(name):
    if len(name) < 2 or not name.isalpha():
        return False
    return True


def validate_age(age):
    try:
        age = int(age)
        if age < 0 or age > 120:
            return False, None
        return True, age
    except ValueError:
        return False, None


def process_users(data):
    valid_users = []
    invalid_users = []
    underage_users = []
    adult_users = []
    seen = []

    stats = {
        "total": 0,
        "valid": 0,
        "invalid": 0,
        "underage": 0,
        "adult": 0
    }

    for user in data:
        user = user.strip()
        stats["total"] += 1

        if not user:
            invalid_users.append(user)
            stats["invalid"] += 1
            continue

        if ":" not in user:
            invalid_users.append(user)
            stats["invalid"] += 1
            continue

        name, age = user.split(":")
        name = name.capitalize()

        is_valid = True

        if not validate_name(name):
            is_valid = False

        is_valid_age, age = validate_age(age)

        if not is_valid_age:
            is_valid = False

        if is_valid:
            key = (name, age)

            if key in seen:
                invalid_users.append(user)
                stats["invalid"] += 1
            else:
                valid_users.append(f"{name} ({age})")
                seen.append(key)
                stats["valid"] += 1

                if age < 18:
                    underage_users.append(f"{name} ({age})")
                    stats["underage"] += 1
                else:
                    adult_users.append(f"{name} ({age})")
                    stats["adult"] += 1
        else:
            invalid_users.append(user)
            stats["invalid"] += 1

    return valid_users, invalid_users, underage_users, adult_users, stats