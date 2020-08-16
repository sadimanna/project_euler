def swap(s, i, j):
    q = list(s)
    q[i], q[j] = q[j], q[i]
    return ''.join(q)


# finds next lexicographic string if exist otherwise returns -1
def next_lexicographical(s):
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            m = s[i + 1]
            swap_pos = i + 1

            for j in range(i + 1, len(s)):
                if m > s[j] > s[i]:
                    m = s[j]
                    swap_pos = j

            if swap_pos != -1:
                s = swap(s, i, swap_pos)
                s = s[:i + 1] + ''.join(sorted(s[i + 1:]))
                return s

    return -1


# helper function
def permute_lexicographically(s):
    s = ''.join(sorted(s))
    permutes = []
    count = 0
    target = 999999
    while True:
        #permutes.append(s)
        s = next_lexicographical(s)
        if s == -1:
            break
        else:
        	count+=1
        	if count==target:
        		return s
    return -1

if __name__ == '__main__':
	digits = '0123456789'
	
	all_permute = permute_lexicographically(digits)
	print(all_permute)