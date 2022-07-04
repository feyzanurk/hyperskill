operations = ["+", "-", "*", "/"]
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
messages = ["Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]
global memory 
memory = 0


def second_flow(result):
    print(msg_4)
    global memory
    answer = input()
    if answer == "y":
        if is_one_digit(result):
            sub_function(result)
        else:
            memory = result
            third_flow()
    elif answer == "n":
        third_flow()
    #else:
    #    second_flow(result)  


def third_flow():
    global memory
    print(msg_5)
    answer = input()
    if answer == "y":
        first_flow()
    elif answer != "n":
        third_flow()
        

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 in ["*", "+", "-"]):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)
    

def is_one_digit(v):
    global memory
    if 10 > v > -10 and v.is_integer():
        return True
    else:
        return False
        


def sub_function(result):
    global memory
    msg_index = 10
    real_index = 0
    while True:
        new_message = messages[real_index]
        print(new_message)
        answer = input()
        if answer == "y":
            if msg_index < 12:
                msg_index += 1
                real_index += 1
                continue
            else:
                memory = result
                third_flow()
        elif answer == "n":
            third_flow()
        else:
            continue
                
        
        
def first_flow():
    global memory
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == "M":
       x = memory
    if y == "M":
       y = memory
    try:
        x = float(x)
        y = float(y)
    except Exception:
        print(msg_1)
        first_flow()
    if oper not in operations:
        print(msg_2)
        first_flow()
    if oper in operations:
        check(x, y, oper)
        if oper == operations[0]:
            result = x + y
            print(result)
            second_flow(result)
        elif oper == operations[1]:
            result = x - y
            print(result)
            second_flow(result)
        elif oper == operations[2]:
            result = x * y
            print(result)
            second_flow(result)
        elif oper == operations[3]:
            try:
                result = x / y
                print(result)
                second_flow(result)
            except ZeroDivisionError:
                print(msg_3)
                first_flow()

first_flow() 