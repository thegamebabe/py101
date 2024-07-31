def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) > 4 or len(dot_separated_words) < 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        # if not is_an_ip_number(word):
        #     return false

    return True
    
    
print(is_dot_separated_ip_address("10.4.5"))