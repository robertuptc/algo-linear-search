array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    for x in range(0, len(array_to_search_through), 1):
        if value_to_find == array_to_search_through[x]:
            return x
            
    


def linear_search_global(value_to_find, array_to_search_through):
    answer = []
    for x in range(0, len(array_to_search_through), 1):
        if value_to_find == array_to_search_through[x]:
            answer.append(x)
    return answer
    





