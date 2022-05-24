# apple_price = 2

# # Assign 5 to the count variable
# count = 5

# # Assign the result of apple_price * the count variable to the total_price variable
# total_price = apple_price*count

# # By using the count variable, print 'You will buy .. apples'

# print("you can buy"+str(count)+"apple")

# # By using the total_price variable, print 'The total price is .. dollars'
# b = count*2
# b = str(b)
# print(f"The total price is{b} dollars")
apple_price = 2
# Assign 10 to the money variable
money = 10

input_count = input('How many apples do you want?: ')
count = int(input_count)
total_price = apple_price * count

print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')

# Add control flow based on the comparison of money and total_price
if count <= 5:
    money_left = money-total_price
    print("You have bought" + input_count + "apples")
    print("you have" + money_left + " dollars left")
elif count > 5:
    print("you do not have that huch money")
    print("you can buy only 5 apple with your money")
else:
    print("by bhaiya ")
