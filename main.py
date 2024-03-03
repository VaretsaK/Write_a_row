def save_input_from_user(file_name: str) -> None:
    """
    This function saves user's input into a specific file.
    :param file_name:
    :return:
    """
    user_input = input("Your input here: ")
    with open(file_name, "a+") as file:
        file.write(user_input + "\n")
