def replace_exclamation(st):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    long = len(st)
    str_lst = list(st)
    for i in range(long):
        if str_lst[i] in vowel:
            str_lst[i] = '!'
    new_str = ''.join(str_lst)
    return new_str
