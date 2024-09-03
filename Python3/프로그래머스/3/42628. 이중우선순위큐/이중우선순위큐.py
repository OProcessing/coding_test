def solution(operations) :
    answer = []
    for oper in operations :
        each = oper.split(' ')

        if each[0] == 'I' :
            each[1] = int(each[1])
            answer.append(each[1])
            answer.sort()

        elif len(answer) > 0 and each[0] == 'D' :
            if each[1] == '1' :
                answer = answer[:-1]
            else :
                answer = answer[1:]

    if len(answer) == 0 :
        return [0,0]
    else :
        answer.sort()
        return [answer[-1], answer[0]]