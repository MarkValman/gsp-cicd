def a_is_consistent(li):
    if( (li[0].count('a') == li[1].count('a')) and (li[1].count('a') == li[2].count('a'))):
        return True
    else:
        return False

def permute(s):
    result = [[s]]
    for i in range(1, len(s)):
        first = [s[:i]]
        rest = s[i:]
        for p in permute(rest):
            result.append(first + p)
    return result

def solution(S):
    all_possible_combinations = permute(S)
    
    combinations_only_with_length_of_3 = []
    for p in all_possible_combinations:
        if(len(p) == 3):
            combinations_only_with_length_of_3.append(p)
    counter = 0
    print(combinations_only_with_length_of_3)
    for combination in combinations_only_with_length_of_3:
        if(a_is_consistent(combination)):
            counter += 1
    return counter

# print(solution('abaab'))