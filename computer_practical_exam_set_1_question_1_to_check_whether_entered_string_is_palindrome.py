string_given_by_user = input("Enter the string to check for palindrome: ")

forward_list = []
forward_list[:0] = string_given_by_user

backward_list = []

#this for loop will add values to backward list in reverse order

for i in range(0, len(forward_list)):
               backward_list.append(forward_list[len(forward_list) - i - 1])

#this for loop will check whether string is palindrome or not

for j in range(0, len(forward_list)):

    if forward_list[j] != backward_list[j] :
        print("Entered string is not a palindrome")
        break

    if j >= len(forward_list)-1 :
        print("String is palindrome")
