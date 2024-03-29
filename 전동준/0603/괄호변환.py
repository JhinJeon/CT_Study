#재귀 함수 구현(해설 코드 참고)

def balanced_index(p):  #'('와 ')'가 짝이 맞는지 확인
    count = 0   #왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
def check_proper(p):    #'균형'인지 확인(True/False)
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index+1] #완성된 괄호
    v = p[index+1:] #완성되지 않은 괄호(개수만 맞는 괄호)
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

a = input()
solution(a)