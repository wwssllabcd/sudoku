
def print_result(res):
    for i in range(9):
        start = i*9
        end = start+9
        print(res[start:end])

def init_array():
    x = 0
    # result = [
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    #     x, x, x, x, x, x, x, x, x,
    # ]
    # result = [
    # 2, 4, x, x, x, x, 5, 9, 1,
    # x, x, 3, 1, x, x, 6, 7, x,
    # x, x, x, x, 8, 9, x, x, x,

    # x, x, 5, 4, x, x, x, x, 6,
    # x, 6, x, x, 3, x, x, 1, x,
    # 8, x, x, x, x, 5, 2, x, x,

    # x, x, x, 9, 5, x, x, x, x,
    # x, 7, 1, x, x, 2, 3, x, x,
    # x, 9, 6, x, x, x, x, 8, 2]
    result = [
        x, 8, 3, x, x, x, 7, 5, x,
        4, x, x, 6, x, 1, x, x, 2,
        6, x, x, x, x, x, x, x, 9,
        x, 6, x, 4, x, 9, x, 7, x,
        x, x, x, x, x, x, x, x, x,
        x, 2, x, 1, x, 7, x, 4, x,
        2, x, x, x, x, x, x, x, 5,
        3, x, x, 2, x, 6, x, x, 4,
        x, 9, 8, x, x, x, 2, 6, x,
    ]
    return result

def init_guess():
    data = []
    for x in range(81):
        data.append([1,2,3,4,5,6,7,8,9])
    return data

def execute_rule_1(idx, data, guess):
    startIdx = int((idx/9))
    startIdx = startIdx*9
    for i in range(9):
        try:
            target = startIdx+i
            guess[target].remove(data)
        except ValueError:
            pass  # do nothing!
    guess[idx] = []
    return guess

def execute_rule_2(idx, data, guess):
    offset = int((idx%9))
    for i in range(9):
        target = i*9 + offset
        try:
            tmplist = guess[target]
            if tmplist is not []:
                tmplist.remove(data)

        except ValueError:
            pass  # do nothing!
    guess[idx] = []
    return guess

def get_idx(idx):
    result = [
        0, 0, 0, 3, 3, 3, 6, 6, 6,
        0, 0, 0, 3, 3, 3, 6, 6, 6,
        0, 0, 0, 3, 3, 3, 6, 6, 6,
        27, 27, 27, 30, 30, 30, 33, 33, 33,
        27, 27, 27, 30, 30, 30, 33, 33, 33,
        27, 27, 27, 30, 30, 30, 33, 33, 33,
        54, 54, 54, 57, 57, 57, 60, 60, 60,
        54, 54, 54, 57, 57, 57, 60, 60, 60,
        54, 54, 54, 57, 57, 57, 60, 60, 60
    ]
    return result[idx]
   

def execute_rule_3(idx, data, guess):
    base = get_idx(idx)
    for i in range(3):
        target = int(base) + i*9
        for j in range(3):
            try:
                guess[target+j].remove(data)
            except ValueError:
                pass  # do nothing!
    return guess

def execute_rule(result, guess):
    for i in range(81):
        if result[i] != 0:
            guess = execute_rule_1(i, result[i], guess)
            guess = execute_rule_2(i, result[i], guess)
            guess = execute_rule_3(i, result[i], guess)
    return result, guess

def has_new_ans(guess):
    for i in range(81):
        if guess[i] != []:
            if len(guess[i]) == 1:
                return i
    return 0xFF


guess = init_guess()
result = init_array()
print_result(result)
print("")
print_result(guess)


while(1):
    result, guess = execute_rule(result, guess)
    newAns = has_new_ans(guess)
    if newAns == 0xFF:
        break;
    result[newAns] = int(guess[newAns][0])


print("")
print_result(guess)
print("")
print_result(result)




    