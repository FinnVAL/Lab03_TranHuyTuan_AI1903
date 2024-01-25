def is_hex(string):
    try:
        int(string, 16)
        return True
    except:
        return False

def hex_to_decimal():
    hex_string = input("Enter a hexadecimal string: ")

    if is_hex(hex_string):
        decimal_value = int(hex_string, 16)
        print(f"The corresponding base-10 value is: {decimal_value}")
    else:
        print("Error: Invalid hexadecimal string")

hex_to_decimal()