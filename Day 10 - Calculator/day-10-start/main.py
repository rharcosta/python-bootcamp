#functions with output
def format_name(first_name, last_name):
    """Docstring: Take a first and last name and format it to return the title case version of the name."""
    return f"{first_name.title()} {last_name.title()}"

#print(format_name("RUBIA", "costa"))
print(format_name(input("What is your first name? "), input("What is your last name? ")))