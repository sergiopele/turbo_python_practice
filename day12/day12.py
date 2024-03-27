# in python block of code is identified within def (functions) only
# on other hand if, else, for, while -> is not separate block and all var caounts as global

# to refer to global var we need to use <global> keyword

my_var = 1

def print_var():
        global my_var
        my_var += 1
        print(my_var)

print_var()