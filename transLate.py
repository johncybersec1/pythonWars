def correct_polish_letters(st): 
    polishChar = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    translation_table = str.maketrans(polishChar)
    return st.translate(translation_table)