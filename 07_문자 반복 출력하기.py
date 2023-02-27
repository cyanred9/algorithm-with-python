def solution(my_string, n):
    result = ''
    for i in range(len(my_string)):
        result += my_string[i] * n 
    return result

# 타인의 풀이 #

def solution(my_string, n):
    return ''.join(i*n for i in my_string) # join 안에서 한번에 for문으로 처리할 수 있었구나...
