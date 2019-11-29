'''
Given morse code with no break, count the number of possibilities
Follow-up: output all the possibilities
/*
reverse_translate_count('..')
> 2  (I | EE)
reverse_translate_count('')
> 0
reverse_translate_count('...-.')
> 15
reverse_translate_count('--.')
> 4  (['T,T,E', 'T,N', 'G', 'M,E']


'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
*/
'''


def reverse_translate_count(s):
    d = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..'}
    d = {j: i for i, j in d.items()}
    mem = {}
    def dfs(idx):
        if idx == len(s):
            return ['']
        if idx in mem:
            return mem[idx]
        res = []
        for length in range(min(5, len(s) - idx + 1)):
            temp = s[idx: length + idx]
            if temp in d:
                for remain in dfs(idx + length):
                    res.append(d[temp] + (',' if remain else '') + remain)
        mem[idx] = res
        return res
    return dfs(0)


print(reverse_translate_count('...-.'))
