name = input("What is your name? ")

num_chars = len(name)

#if name.endswith("!"):
if name[num_chars - 1] == '!':
    print(f"HELLO {name.upper()}, WHY ARE WE YELLING?")
else:
    print(f"Hello {name}.")