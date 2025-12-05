# Author: Oshan Mendis
# Date: 2025-12-06
# Description: Temperature converter program

class TemperatureConverter:
    def __init__(self, input):
        self.input = input

    def is_valid_input(self):
        # First character of input (C or F)
        prefix = self.input[0]
        # Rest of the characters in input leaving first character
        number_part = self.input[1:]

        # Making sure input length is at least 2 chars
        # Making sure input prefix is within 'F' or 'C'
        # Making sure number part is a numeric value
        if len(self.input) >= 2 and (prefix == 'F' or prefix == 'C') and number_part.replace('.', '', 1).isdigit():
            return True
        else:
            return False

    def convert(self):
        # First character of input (C or F)
        prefix = self.input[0]
        # Rest of the characters in input leaving first character
        number_part = self.input[1:]

        temp_value = float(number_part)

        # Fahrenheit → Celsius
        if prefix == 'F':
            celsius = (temp_value - 32) * 5 / 9
            print(f"F{temp_value:.0f} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius")

        # Celsius → Fahrenheit
        elif prefix == 'C':
            fahrenheit = (temp_value * 9 / 5) + 32
            print(f"C{temp_value:.0f} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit")


if __name__ == "__main__":
    user_input = input("Enter temperature (e.g., F51 or C11): ").strip()

    temp_converter = TemperatureConverter(user_input)
    if temp_converter.is_valid_input():
        temp_converter.convert()
    else:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")

