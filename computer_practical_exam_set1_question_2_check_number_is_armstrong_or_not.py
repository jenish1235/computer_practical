number_to_check = int(input("Enter the number to check for armstrong: "))
initial_number = number_to_check
sum_of_cubes = 0

for i in range(len(str(number_to_check))) :
    unit_digit = number_to_check % 10
    sum_of_cubes = sum_of_cubes + (unit_digit * unit_digit * unit_digit)
    number_to_check = int(number_to_check / 10)

if sum_of_cubes == initial_number:
    print(" given number is armstrong  number")
else:
    print("given number is not armstrong number")
               
