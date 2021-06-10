ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase

while True:
    print("BINARY-DECIMAL CONVERTER")
    print("1. Convert Binary to Decimal")
    print("2. Convert Decimal to Binary")
    print("3. Exit Program\n")

    while True:
        try:
            user_input = int(input("Select an option (1-3 only): "))
        except ValueError:
            print("Invalid selection!\n")
            continue
        if user_input > 3 or user_input < 1:
            print("Invalid selection!\n")
            continue
        else:
            break

    def bin_check(bin):
        for number in bin:
            if number != "1" and number != "0":
                print("Invalid Binary Input! \n")
                return False
                break
        return True

    def deci_check(deci):
        for number in deci:
            if number == "." or number == "-" or number == ascii_letters:
                print("Invalid Decimal Input! \n")
                return False
                break
        return True


    def bin_to_deci(input_bin):
        decimal = 0
        counter = 0
        binary = int(input_bin)
        while (binary != 0):
            decimal_1 = binary % 10
            decimal = decimal + decimal_1 * pow(2, counter)
            binary = binary // 10
            counter += 1
        print("The decimal equivalent of " + input_bin + " is " + str(decimal) + "\n")


    def deci_to_bin(input_decimal):
        binary = ""
        while int(input_decimal) != 0:
            remainder = int(input_decimal) % 2
            input_decimal = int(input_decimal) // 2
            binary = str(remainder) + binary
        print("The binary representation is " + str(binary) + "\n")


    if user_input == 1:
        input_bin = str(input("Enter binary number: "))
        while (bin_check(input_bin) == False):
            input_bin = str(input("Enter binary number: "))
        bin_to_deci(input_bin)

    if user_input == 2:
        input_deci = input("Enter decimal number: ")
        while (deci_check(input_deci) == False):
            input_deci = input("Enter decimal number: ")
        deci_to_bin(input_deci)


    if user_input == 3:
        break
print("\nGoodbye!")