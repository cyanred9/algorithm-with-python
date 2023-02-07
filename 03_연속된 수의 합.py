
# 코드를 홀수, 짝수로 나누고 공통적인 부분을 없애지 못해서 굉장히 중복이 많다.
# list comprehension을 쓰면 간략하게 활용 가능하니 연습해야할듯.

def solution(num, total):
    if num%2 == 0:
        answer = list(range(int(total/num-(num//2-0.5)), int(total/num+(num//2-0.5))+1))
    else:
        answer = list(range(int(total/num-num//2),int(total/num+num//2)+1))
    return answer
