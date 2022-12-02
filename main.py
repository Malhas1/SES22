

def count_digits(line:str) -> int:
        digits =
        ['0', '1', '2','3', '4', '5', '6', '7', '8', '9' ]
        total = 0
        for s in line:
            if s in digits:
                    total += 1
        return total

s = input()
print(count_digits(s))
