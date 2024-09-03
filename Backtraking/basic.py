# Generating all possible binary strings of length n

def generate_binary_string(n):
    res = []
    def backtrack(cur_st):
        if  len(cur_st) == n:
            res.append(cur_st)
            return
        backtrack(cur_st+'0')
        backtrack(cur_st+'1')
    backtrack('')
    return res
print(generate_binary_string(2))

