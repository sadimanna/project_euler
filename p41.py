from math import factorial, sqrt
 
def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

def prime_lex(s):
    seq = list(s)
    # there are going to be n! permutations where n = len(seq)
    for _ in range(factorial(len(seq))):
        # print permutation
        #print(''.join(seq))
        if isprime(int(''.join(seq))):
            #print('Prime : '+''.join(seq))
            return ''.join(seq)
 
        # find p such that seq[p:] is the largest sequence with elements in
        # descending lexicographic order
        p = len(seq) - 1
        while p > 0 and seq[p - 1] < seq[p]:
            p -= 1
 
        # reverse seq[p:]
        seq[p:] = reversed(seq[p:])
        #print(seq)
 
        if p > 0:
            # find q such that seq[q] is the smallest element in seq[p:] such that
            # seq[q] > seq[p - 1]
            q = p
            while seq[p - 1] < seq[q]:
                q += 1
 
            # swap seq[p - 1] and seq[q]
            seq[p - 1], seq[q] = seq[q], seq[p - 1]
            #print(seq)
    return ''

if __name__ == '__main__':
    output = ''
    s = '987654321'
    while output=='':
        output = prime_lex(s)
        if output=='':
            s = s[1:]

    print(output)
 
    
        