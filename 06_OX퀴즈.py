
# 자신의 풀이 #

result = []

def solution(quiz):
    for i in range(len(quiz)):
        if eval(quiz[i].split(" = ")[0]) == int(quiz[i].split(" = ")[1]):
            result.extend("O")
        else:
            result.extend("X")
    return result

# 타인의 풀이 #

def valid(equation): # 다른 함수를 def 해서 list comprehension 안에 if else 형태로 조건을 주는게 임팩트 있었음. 가독성이 좋음 # 
    equation = equation.replace('=', '==') 
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]    