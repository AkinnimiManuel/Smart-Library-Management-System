

#clear screen
def clear_screen():
    #windows
    import os
    os.system("cls" if os.name == "nt" else "clear")