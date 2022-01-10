def GetInput(display, x):
    display['text'] = str(display['text']) + str(x)
    if display['text'][0] == 0 or display['text'][0] == "0":
        display['text'] = display['text'][1:]

def Clr(display):
    display['text'] = 0
    num_q = list()
    op_q = list()


