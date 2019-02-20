
import numpy as np

sample = 100000

a = False
b = False
c = False
d = False
count_of_a_positive = 0
count_of_b_negative = 0
count_of_d_positive = 0
count_of_d_positive_and_a_negative = 0
count_of_e_positive_and_b_negative = 0
count_of_d_positive_and_e_negative = 0
count_of_a_positive_d_positive_and_e_negative = 0
count_of_b_positive_e_negative_a_positive = 0


def prob_a():
    global count_of_a_positive
    global a
    prob = np.random.randint(100)
    if prob < 20:
        count_of_a_positive += 1
        a = True
    else:
        a = False


def prob_b():
    global count_of_b_negative
    global b
    prob = np.random.randint(100)
    if a:
        if prob < 80:
            b = True
        else:
            b = False
            count_of_b_negative += 1
    else:
        if prob < 20:
            b = True
        else:
            b = False
            count_of_b_negative += 1


def prob_c():
    prob = np.random.randint(100)
    global c
    if a:
        if prob < 20:
            c = True
        else:
            c = False
    else:
        if prob < 5:
            c = True
        else:
            c = False


def prob_d():
    global count_of_d_positive
    global count_of_d_positive_and_a_negative
    global d
    prob = np.random.randint(100)
    if (not b) and (not c):
        if prob < 5:
            count_of_d_positive += 1
            if not a:
                count_of_d_positive_and_a_negative += 1
            d = True
        else:
            d = False
    else:
        if prob < 80:
            count_of_d_positive += 1
            if not a:
                count_of_d_positive_and_a_negative += 1
            d = True
        else:
            d = False


def prob_e():
    global count_of_e_positive_and_b_negative
    global count_of_d_positive_and_e_negative
    global count_of_a_positive_d_positive_and_e_negative
    global count_of_b_positive_e_negative_a_positive
    prob = np.random.randint(100)
    if c:
        if prob < 80:
            if not b:
                count_of_e_positive_and_b_negative += 1
            return True
        else:
            if d:
                count_of_d_positive_and_e_negative += 1
                if a:
                    count_of_a_positive_d_positive_and_e_negative += 1
            if b and a:
                count_of_b_positive_e_negative_a_positive += 1
            return False
    else:
        if prob < 60:
            if not b:
                count_of_e_positive_and_b_negative += 1
            return True
        else:
            if d:
                count_of_d_positive_and_e_negative += 1
                if a:
                    count_of_a_positive_d_positive_and_e_negative += 1
            if b and a:
                count_of_b_positive_e_negative_a_positive += 1
            return False


def prob_d_positive():
    count = sample
    while count > 0:
        prob_a()
        prob_b()
        prob_c()
        prob_d()
        count -= 1
    print(count_of_d_positive / sample)


def prob_d_positive_and_a_negative():
    count =  sample
    while count > 0:
        prob_a()
        prob_b()
        prob_c()
        prob_d()
        count -= 1
    print(count_of_d_positive_and_a_negative / sample)


def prob_e_positive_given_b_negative():
    count = sample
    while count > 0:
        prob_a()
        prob_b()
        prob_c()
        prob_e()
        count -= 1
    print((count_of_e_positive_and_b_negative / sample) / (count_of_b_negative / sample))


def prob_a_positive_given_d_positive_and_e_negative():
    count = sample
    while count > 0:
        prob_a()
        prob_b()
        prob_c()
        prob_d()
        prob_e()
        count -= 1
    print((count_of_a_positive_d_positive_and_e_negative / sample) / (count_of_d_positive_and_e_negative / sample))


def prob_b_positive_and_e_negative_given_a_positive():
    count = sample
    while count > 0:
        prob_a()
        prob_b()
        prob_c()
        prob_e()
        count -= 1
    print((count_of_b_positive_e_negative_a_positive / sample) / (count_of_a_positive / sample))


'''You need to run only one task at the same time to get the true result because if you run all tasks at the same time,
the global variables will change at each task, so you will get the wrong results.'''

#prob_d_positive()
#prob_d_positive_and_a_negative()
prob_e_positive_given_b_negative()
#prob_a_positive_given_d_positive_and_e_negative()
#prob_b_positive_and_e_negative_given_a_positive()

