def get_todos(filepath='todos.txt'):
    # Context manager short, sagely and fast way to work with file "with" automatically close file
    with open(filepath, 'r') as file_local:
        # The readlines() method returns a list containing each line in the file as a list item.
        todos_local = file_local.readlines()
    return todos_local


# In this function we do not need return method because this does one action and we do not need any value for output.
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
