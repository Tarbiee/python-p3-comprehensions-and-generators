# !/usr/bin/env python3
# evens = list()
# def return_evens(num_list):
#     for n in num_list:
#         if n % 2 == 0:
#             evens.append(n)
#     return evens
# return_evens([0, 1, 3, 5, 7, 8, 9])


def return_evens(num_list):
    evens =[n for n in num_list if n%2 ==0]  
    if not evens:
        return[]
    else:
        return evens
return_evens([0, 1, 3, 5, 7, 8, 9])

    

def make_exclamation(sentence_list):
    sentence = [n + "!" for n in sentence_list ]
    return sentence