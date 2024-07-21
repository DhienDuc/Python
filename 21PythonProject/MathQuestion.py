import random
import time

# initial define
number_min = 1
number_max = 25
quantity = 10
operators = ['+', '-', '*']

def question():
    # create random
    first_num = random.randint(number_min, number_max)
    sencond_num = random.randint(number_min, number_max)
    operator = random.choice(operators)
    # make string
    exp = str((first_num)) + " " + operator + " " + str(sencond_num)
    # get answer from string
    answer = eval(exp)
    # rerturn
    return exp, answer

input("Press any key to start!")
print("--------------------Start--------------------")

start_time = time.time()

for i in range(quantity):
    exp, answer = question()
    while True:
        reply = input("#Question " + str(i + 1) + " : " + exp + " = ")
        if reply == 'q':
            quit()
        if reply == str(answer):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------Finished in {} seconnds---------".format(total_time))



