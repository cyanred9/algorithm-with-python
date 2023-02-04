
def solution(common):
    if (common[1] - common[0]) == (common[2] - common[1]):
        answer = int(common[len(common)-1] + (common[1] - common[0]))
    else:
        answer = int(common[len(common)-1] * common[1] / common[0])
    return answer



# 다른 사람 풀이
# list의 행을 슬라이스해서 꺼내 쓴게 fancy함
# 마지막 리스트 요소 불러올때 -1을 쓰면 되는데... 아직 익숙하지가 않다

# def solution(common):
#     answer = 0
#     a,b,c = common[:3]
#     if (b-a) == (c-b):
#         return common[-1]+(b-a)
#     else:
#         return common[-1] * (b//a)
#     return answer
