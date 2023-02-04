# https://school.programmers.co.kr/learn/courses/30/lessons/120808#


# 내가 맞춘 정답
from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    a = Fraction(numer1,denom1) + Fraction(numer2,denom2)
    answer = [a.numerator, a.denominator]
    return answer


# 조금더 수학적인 정답
# import math 

# def solution(numer1, denom1, numer2, denom2):
#     a = (numer1 * denom2) + (numer2 * denom1) 
#     b = denom1 * denom2
#     c = math.gcd(a,b)
#     answer = [a/c,b/c]
#     return answer