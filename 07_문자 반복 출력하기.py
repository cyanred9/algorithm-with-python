def solution(my_string, n):
    result = ''
    for i in range(len(my_string)):
        result += my_string[i] * n 
    return result