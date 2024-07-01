def solution(operations):
    queue_list = []
    for i in range(len(operations)) :
        queue = operations[i].split(' ')
        if queue[0] == 'I' : queue_list.append(int(queue[1]))
        elif queue[0] == 'D' : 
            if queue_list :
                if queue[1] == '1' :
                        queue_list.remove(max(queue_list))
                elif queue[1] == '-1' :
                        queue_list.remove(min(queue_list))
                        
                     
    if queue_list :
        result = [max(queue_list), min(queue_list)]
    else : result = [0, 0]
    
    return result