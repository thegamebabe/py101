def short_long_short(str1, str2):
    longer = str1 if len(str1) > len(str2) else str2
    shorter = str1 if len(str1) < len(str2) else str2
    return shorter + longer + shorter
    
    

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")