def greetings(name_list, job_dict):
    name = " ".join(name_list)
    print(f"Hello, {name}! It's nice to have a {job_dict.get('title')} {job_dict.get('occupation')} around.")





greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.