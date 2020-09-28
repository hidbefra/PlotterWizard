def warning():
    print("empty function pointer called")

class status_text():
    text = ""
    update_function_pointer = warning

    def __init__(self, update_function):
        status_text.update_function_pointer = update_function

    def add_line_to_status_text(text):
        status_text.text += text +"\n"
        #print(status_text.text)
        status_text.update_function_pointer() # hier wird eine verknüpfte funktion des Main window aufgerufen welche status_text.text ausliest