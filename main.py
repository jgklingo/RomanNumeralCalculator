import sys

conversion_dictionary = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def main():
    help_string = "Syntax: [-d(--toDecimal) | -r(--toRoman)] <number_to_convert>"
    if len(sys.argv) < 3:
        print(help_string)
    elif sys.argv[1] == "-d" or sys.argv[1] == "--toDecimal":
        print(roman_to_decimal(sys.argv[2]))
    elif sys.argv[1] == "-r" or sys.argv[1] == "--toRoman":
        print(decimal_to_roman(int(sys.argv[2])))
    else:
        print("Option not recognized." + help_string)


def decimal_to_roman(decimal: int) -> str:
    roman_numerals = ""
    while decimal > 0:
        for symbol in conversion_dictionary.keys().__reversed__():
            if conversion_dictionary[symbol] <= decimal:
                roman_numerals += symbol
                decimal -= conversion_dictionary[symbol]
                break

        last_4 = roman_numerals[-4:]
        last_5 = roman_numerals[-5:]
        if last_4 == "IIII":
            roman_numerals = roman_numerals[:-4]
            roman_numerals += "IV"
        elif last_5 == "VIIII":
            roman_numerals = roman_numerals[:-5]
            roman_numerals += "IX"
        elif last_4 == "XXXX":
            roman_numerals = roman_numerals[:-4]
            roman_numerals += "XL"
        elif last_5 == "LXXXX":
            roman_numerals = roman_numerals[:-5]
            roman_numerals += "XC"
        elif last_4 == "CCCC":
            roman_numerals = roman_numerals[:-4]
            roman_numerals += "CD"
        elif last_5 == "DCCCC":
            roman_numerals = roman_numerals[:-5]
            roman_numerals += "CM"
        last_3 = roman_numerals[-3:]
        if last_3 == "VIV":
            roman_numerals = roman_numerals[:-3]
            roman_numerals += "IX"
        elif last_3 == "LXL":
            roman_numerals = roman_numerals[:-3]
            roman_numerals += "XC"
        elif last_3 == "DCD":
            roman_numerals = roman_numerals[:-3]
            roman_numerals += "CM"
    return roman_numerals


def roman_to_decimal(roman_numeral: str) -> int:
    symbol_2_value = 0
    total = 0
    while len(roman_numeral) > 0:
        symbol_1_value = conversion_dictionary[roman_numeral[0]]
        if len(roman_numeral) > 1:
            symbol_2_value = conversion_dictionary[roman_numeral[1]]
        if symbol_1_value < symbol_2_value:
            total += symbol_2_value - symbol_1_value
            roman_numeral = roman_numeral[2:]
        else:
            total += symbol_1_value
            roman_numeral = roman_numeral[1:]
    return total


if __name__ == '__main__':
    main()
