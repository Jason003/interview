def strict_increasing_digit(N):
    digits = list(map(int, list(str(N))))
    mark = len(digits) - 1
    while mark > 0:
        if digits[mark - 1] >= digits[mark]:
            break
        mark -= 1
    if mark == -1:
        return N
    
