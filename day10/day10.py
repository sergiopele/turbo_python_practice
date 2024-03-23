def format_name(f_name:str, l_name:str) -> str:
        # docsstring
        """Take a first and last name and format it to 
        return the title case version of the name"""
        return f"{f_name} {l_name}".title()

name = input("Enter you name")
l_name = input("Enter your last name")
print(format_name(name,l_name))