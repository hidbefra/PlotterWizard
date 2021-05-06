def warning():
    print("empty function pointer called")

class part_count():
    count = 0
    add_function_pointer = warning

    def __init__(self, add_function):
        part_count.add_function_pointer = add_function
        pass

    @staticmethod
    def add_part():
        part_count.add_function_pointer()
        pass


         # hier wird eine verknüpfte funktion des Main window aufgerufen welche status_text.text ausliest