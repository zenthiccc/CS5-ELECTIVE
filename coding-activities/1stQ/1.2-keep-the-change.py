# Create your solution for the "Keep the Change activity"

change = int(input("Enter amount of change in cents (0 or 99): "))
while change > 99 or change < 0:
    change = input("Change must be 0 to 99, try again: ")

if change%25 == 0 or change%25 != 0:
    cent25 = change//25
    cent25R = change%25

if cent25R%10 == 0 or cent25R%10 != 0:
    cent10 = cent25R//10
    cent10R = cent25R%10

if cent10R%5 == 0 or cent10R%5 != 0:
    cent5 = cent10R//5
    cent5R = cent10R%5

if cent5R%1 == 0:
    cent1 = cent5R//1


print("Breakdown: ")
if cent25 != 0:
    print(str(cent25) + " x 25 cents")

if cent10 != 0:
    print(str(cent10) + " x 10 cents")

if cent5 != 0:
    print(str(cent5) + " x 5 cents")

if cent1 != 0:
    print(str(cent1) + " x 1 cent")