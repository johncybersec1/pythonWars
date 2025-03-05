def sort_my_string(s):
    s1 = s[::2] # Items at even indexes
    s2 = s[1::2] # Items at odd indexes
    return f"{s1} {s2}"
    
