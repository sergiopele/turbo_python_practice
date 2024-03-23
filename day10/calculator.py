from art import logo
import os
first_num_prompt = "What's the first number?: "
second_num_prompt = "What's the second number?: "
error_msg = "Please enter a numeric value\n"
operator_prompt = "Pick an operation: "
operation_list = ["+", "-", "*", "/"]
operator_error_msg = "Please enter a valid operation '+', '-', '*' or '-'\n"
division_zero = "Error: division by zero"
def determin_number_datatype(number):
        convert_int = int(number)
        convert_float = float(number)

        if type(number) == int:
                return convert_int
        elif type(number) == float:
                return convert_float
        elif not "." in number:
                return int(number)
        else:
                return float(number)
        
def first_number():
        """Function accepts first user's input"""
        number_1 = input(first_num_prompt)
        while not number_1.isdigit():
                number_1 =input(error_msg + " " + first_num_prompt)
        return determin_number_datatype(number_1)

def second_number() -> float:
        """Function accepts second user's input"""
        number_2 = input(second_num_prompt)
        while not number_2.isdigit():
                number_2 =input(error_msg + " " + second_num_prompt)
        return determin_number_datatype(number_2)

def operator() -> str:
        """Function define numeric operation"""
        operator = input(operator_prompt)
        while not operator in operation_list:
                operator = input(operator_error_msg + " " + operator_prompt)
        return operator

def result(num_1, operator:str, num_2):
        """Function agregate result"""
        result = 0
        if operator == "+":
                result = num_1 + num_2
        elif operator == "-":
                result = num_1 - num_2
        elif operator == "*":
                result =  num_1 * num_2
        else:
                if not num_2 == 0: 
                        result = num_1 / num_2
                else:
                        print(division_zero)
                        return "Error"
        print(f"{num_1} {operator} {num_2} = {result}")
        return determin_number_datatype(result)

def continue_calculation(result) -> bool:
        """Function to check if user wants to proceed calculation with previous result"""
        answer = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: \n")
        if answer.lower() == "y":
                return True
        else: 
                os.system("clear")
                return False
        
def calculator_console_app() -> int:        
        return result(output 
                      if ((type(output) == float 
                           or type(output) == int) 
                          and continue_calculation(output) == True) 
                      else first_number(), operator(), second_number())

print(logo)
output = ""
while True:
        output = calculator_console_app()

