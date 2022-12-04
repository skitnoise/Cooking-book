from pathlib import Path
import os
import shutil
print("Recipe Book 0.1")
exit_program = False
recipe_counter = 0
base = Path.home()
directory_path = Path(base, 'Desktop/Python/Day_6/Recipes')
print(f"Welcome! The recipes are located in {directory_path} ")


def exit_recipe_manager():
    print("Farewell!")
    exit()


def validate_letter_or_number():
    user_input = ''
    is_valid = False
    alphabet_and_numbers = " "
    while not is_valid:
        user_input = input("Choice: ")
        if user_input not in alphabet_and_numbers:
            is_valid = True
        else:
            print("You haven't chosen a correct letter or number")
    return user_input


def validate_number():
    user_input = ''
    is_valid = False
    number_list = "123456"

    while not is_valid:
        user_input = input("Please choose a number from 1 to 6\nChoice: ")

        if user_input in number_list and len(user_input) == 1:
            is_valid = True
        else:
            print("You haven't chosen a correct number ")

    return user_input


def recipe_category():
    category_list_file = os.listdir(directory_path)
    print(category_list_file)


def recipe_list(selected_choice):
    recipe_list_file = os.listdir(directory_path/selected_choice)
    print(recipe_list_file)


def list_categories():
    list_all_categories = os.listdir(directory_path)
    list_all_categories = ", ".join(list_all_categories)
    print(list_all_categories)


def counting_recipes():
    file_count = sum([len(files) for r, d, files in os.walk('/Day_6/Recipes')])
    file_count = str(file_count)
    return file_count


print("You have " + counting_recipes() + " recipes")


def menu():
    print("Choose an option: \n [1] - read recipe \n [2] - create recipe \n "
          "[3] - create category \n [4] - delete recipe \n [5] - delete category \n [6] - end program")
    user_menu_input = validate_number()
    return user_menu_input


def menu_choice(user_menu_input):
    user_menu_input = int(user_menu_input)
    if user_menu_input == 1:
        choose_category(user_menu_input)
    elif user_menu_input == 2:
        choose_category(user_menu_input)
    elif user_menu_input == 3:
        create_category()
    elif user_menu_input == 4:
        choose_category(user_menu_input)
    elif user_menu_input == 5:
        delete_category()
    elif user_menu_input == 6:
        exit_recipe_manager()


def choose_category(user_input):
    print("Which category do you choose?")
    list_categories()
    category_input = validate_letter_or_number()
    if user_input == 1:
        read_recipe(category_input)
    elif user_input == 2:
        create_recipe(category_input)
    elif user_input == 4:
        delete_recipe(category_input)
    return category_input


def create_category():
    print("Type the name of the new directory")
    new_dir = validate_letter_or_number()
    path = directory_path/new_dir
    is_exist = os.path.exists(path)
    if is_exist is True:
        print("The directory already exists")
        create_category()
    else:
        os.mkdir(directory_path/new_dir)


def delete_recipe(category_input):
    print("Which recipe do you want to delete?")
    list_recipes_in_folder = os.listdir(directory_path/category_input)
    string_recipes_in_folder = ", ".join(list_recipes_in_folder)
    print(string_recipes_in_folder)
    delete_recipe_choice = validate_letter_or_number()
    path = Path(directory_path/category_input/delete_recipe_choice)
    if path.is_file():
        os.unlink(path)
    else:
        print(f'The file {delete_recipe_choice} does not exist')
        delete_recipe(category_input)


def delete_category():
    print("Which category do you want to delete?")
    recipe_category()
    delete_dir = validate_letter_or_number()
    path = directory_path / delete_dir
    is_exist = os.path.exists(path)
    if is_exist is False:
        print("The directory doesn't exist")
        delete_category()
    else:
        shutil.rmtree(directory_path / delete_dir)


def create_recipe(category_input):
    print("Enter the name of the recipe")
    user_recipe_name = validate_letter_or_number()
    user_recipe_name_extension = user_recipe_name + ".txt"
    user_recipe = Path(directory_path/category_input/user_recipe_name_extension)
    user_recipe.touch(exist_ok=True)
    user_recipe_file = open(user_recipe)
    write_recipe_content(user_recipe)
    return user_recipe_file


def write_recipe_content(user_recipe):
    print("Write the content of the recipe")
    user_content_input = validate_letter_or_number()
    recipe_content = open(user_recipe, 'a')
    recipe_content.write(user_content_input)
    recipe_content.close()


def read_recipe(category_input):
    print("Which recipe do you want to read?")
    list_recipes_in_folder = os.listdir(directory_path/category_input)
    string_recipes_in_folder = ", ".join(list_recipes_in_folder)
    print(string_recipes_in_folder)
    recipe_read_choice = validate_letter_or_number()
    check_file_existence(category_input, recipe_read_choice)
    return recipe_read_choice


def check_file_existence(category_input, recipe_read_choice):
    path = Path(directory_path/category_input/recipe_read_choice)
    path_to_file = recipe_read_choice
    if path.is_file():
        open_recipe_path = Path(directory_path/category_input/recipe_read_choice)
        open_recipe = open(open_recipe_path)
        print(open_recipe.read())
        input("Press Enter to return to menu... ")
    else:
        print(f'The file {path_to_file} does not exist')
        read_recipe(category_input)


menu_choice(menu())

while not exit_program:
    menu_choice(menu())
