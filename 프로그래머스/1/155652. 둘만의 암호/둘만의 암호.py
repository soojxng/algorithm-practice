def solution(s, skip, index):
    answer = ''
    alphabet = [chr(x) for x in range(ord('a'), ord('z')+1) if chr(x) not in skip]
    alphabet_map = {char: idx for idx, char in enumerate(alphabet)}
    
    for i in s:
        answer += alphabet[(alphabet_map[i] + index) % len(alphabet)]
    return answer