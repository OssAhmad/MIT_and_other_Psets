# Problem Set 4A
# Name: Oss Ahmad 
# Collaborators: No One 
# Time Spent: 2:00

def main():
    _input = input("Enter a string: ")
    print('Input:', _input)
    #print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) # this is just a test line, but I didn't delete it for some reason :/ 
    print('Output:', get_permutations(_input))

def find_permutations(S, L):
    l = []
    for e in L:
        i = 0
        while i <= len(e):
            l.append(e[:i] + S + e[i:])
            i = i + 1
    return(l)

def del_replicas(L):
    ll = []
    for e in L:
        if e not in ll:
            ll.append(e)
    return ll

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    l = []
    if len(sequence) == 1:
        return list(sequence)
    else: 
        l =  find_permutations(sequence[0], get_permutations(sequence[1:]))
    
    l = del_replicas(l)
    
    return(l)

if __name__ == '__main__':
#   #EXAMPLE
    main()
#      You can put example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n) 
#    Also the algortithm is far from refined and will take forever to give an answer for strings that have more than 10 charaters in them. 
