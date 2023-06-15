

def hello(str):
    return 'How can I help you?', True


def add(str):
    text = str.split()
    if len(text) < 2:
        return 'Error. Must be: first name (surname), phone number', True
    global book
    book.update({str[:len(str)-len(text[-1])]: text[-1]})

    return 'Added ' + str, True


def change(str):
    text = str.split()
    if len(text) < 2:
        return 'Error. Must be: first name (surname), phone number', True
    global book
    t = book.get(str[:-len(text[-1])])
    if t:
        book.update({str[:len(str)-len(text[-1])]: text[-1]})
    else:
        return f'Error. {str[:-len(text[-1])]} not found. Repeat, please', True

    return 'Changed ' + str, True


def phone(str):
    text = str.split()
    global book
    t = book.get(str+' ')
    if not t:
        return f'Error. {str} not found. Repeat, please', True

    return str + ' :' + t, True

def show_all(str):
    global book
    str = ''
    for k, v in book.items():
        str = str + k +': ' + v + '\n'

    return str, True

def good_bye(str):
    return str, False

def close(str):
    return str, False

def exit(str):
    return str, False
    
book = {}
def func_distrib(input_C, commands):

    answer = ('Input error. Repeat, please',True)
    for com in commands:
        if com == input_C.lower()[:len(com)]:
            if len(com) == len(input_C):
                test = com.replace(' ', '_') + '()'
                answer = eval(com.replace(' ', '_') + '("")')
            else:
                input_mod = input_C[len(com):].strip()
                answer = eval(com.replace(' ', '_') + '(input_mod)')
    return answer




def main():
    commands = ('hello','add','change','phone','show all','good bye','close','exit')
    l = True
    while l:
        text = input(' Go -->')
        f = func_distrib(text, commands)
        l = f[1]
        print(f[0])



if __name__ == '__main__':

    main()

