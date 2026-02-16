def calculate_average_age(users):
    """
    Calculate the average age of users with valid age values.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries containing 'age' keys.

    Returns
    -------
    float
        The average age of users with valid integer age values.
        Returns 0.0 if no valid ages are found or an error occurs.

    Examples
    --------
    >>> users = [{'age': 30}, {'age': 25}, {'age': 35}]
    >>> calculate_average_age(users)
    30.0
    """
    try:
        valid_ages = [user.get("age") for user in users if isinstance(user.get("age"), int)]
        return sum(valid_ages) / len(valid_ages) if valid_ages else 0.0
    except ZeroDivisionError:
        print("Error: No valid ages found in the user list.")
        return 0.0
    except Exception as e:
        print(f"Error calculating average age: {e}")
        return 0.0


def get_active_user_emails(users):
    """
    Retrieve email addresses of active users.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries containing 'is_active' and 'email' keys.

    Returns
    -------
    list of str
        Email addresses of users where is_active is True and email exists.
        Returns empty list if any error occurs.

    Examples
    --------
    >>> users = [
    ...     {'is_active': True, 'email': 'alice@example.com'},
    ...     {'is_active': False, 'email': 'bob@example.com'}
    ... ]
    >>> get_active_user_emails(users)
    ['alice@example.com']
    """
    try:
        return [
            user.get("email")
            for user in users
            if user.get("is_active") and user.get("email")
        ]
    except KeyError as e:
        print(f"Error: Missing required key {e} in user dictionary.")
        return []
    except Exception as e:
        print(f"Error retrieving active user emails: {e}")
        return []


if __name__ == "__main__":
    users = [
        {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
        {"name": "bob", "age": 25, "is_active": False},
        {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
        {"name": "david", "age": "unknown", "is_active": False}
    ]

    average_age = calculate_average_age(users)
    print(f"average user age: {average_age:.2f}")

    active_user_emails = get_active_user_emails(users)
    print(f"active user emails: {active_user_emails}")