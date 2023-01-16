from pynput import keyboard as kb
items_list = []
def save_input():
    with open("D:\\log.txt", "w") as f: #location to save the specified file.
        for item in items_list:
            k = str(item).replace("'" , " ")
            f.write(str(item))
def onPress(button):
    # try:
    #     print("You pressed {0}".format(button.char))
    #     items_list.append(button)
    # except AttributeError:
    #     print("You pressed special button {0}".format(button))
    if button == kb.Key.enter:
        #stop the listener
        raise kb.Listener.StopException
    items_list.append(button)
    print(items_list)
def onRelease(button):
    pass
with kb.Listener(on_press = onPress) as listener:
    listener.join()

#To save the input to a local file
save_input()