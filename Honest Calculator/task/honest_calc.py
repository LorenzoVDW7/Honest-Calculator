# write your code here
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
running = True
memory = 0.0
operators = ["+", "-", "/", "*"]
result = -1
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(par):
    output = False
    if -10 < par < 10 and float.is_integer(par):
        output = True
    elif not -10 < par < 10 and float.is_integer(par):
        output = False
    return output


def check(v1, v2, oper):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1 and oper == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
    else:
        return


while running:
    endThree = False
    calc = input(f"{msg_0}\n")

    x, operation, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError as VE:
        x = None
        y = None

    if not isinstance(x, (float, int)) and not isinstance(y, (float, int)):
        print(msg_1)
    elif operation not in operators:
        print(msg_2)

    if x is not None and y is not None:
        check(x, y, operation)
        if operation == "/" and y == 0:
            print(msg_3)
            running = True
        else:
            if operation == "+":
                result = x + y
                print(result)

            elif operation == "-":
                result = x - y
                print(result)

            elif operation == "*":
                result = x * y
                print(result)

            elif operation == "/" and y != 0:
                result = x / y
                print(result)

            while not endThree:
                print(msg_4)
                answer_msg4 = input()

                if answer_msg4 == "y":
                    if is_one_digit(result):
                        message = {10: msg_10, 11: msg_11, 12: msg_12}
                        msg_index = 10
                        msg_max = False
                        while not msg_max:
                            answer_msg10 = input(message[msg_index])
                            if answer_msg10 == "y":
                                if msg_index < 12:
                                    msg_index += 1
                                elif not msg_index < 12:
                                    msg_max = True
                                    memory = result
                            elif answer_msg10 == "n":
                                msg_max = True
                            else:
                                msg_max = False
                        endThree = True
                    elif not is_one_digit(result):
                        memory = result
                        endThree = True
                elif answer_msg4 != "y":
                    if answer_msg4 == "n":
                        endThree = True
                    elif answer_msg4 != "n":
                        endThree = False

            print(msg_5)
            answer_msg5 = input()

            if answer_msg5 == "n":
                running = False
