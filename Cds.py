def words_to_number(word):
    # Dictionary to map words to numbers
    word_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000,
        'billion': 1000000000
    }

    # Split the input into words
    words = word.lower().replace('-', ' ').replace(' and ', ' ').split()

    # Initialize variables
    number = 0
    current = 0

    for w in words:
        if w in word_to_num:
            if w == 'hundred':
                current *= word_to_num[w]
            elif w == 'thousand' or w == 'million' or w == 'billion':
                current *= word_to_num[w]
                number += current
                current = 0
            else:
                current += word_to_num[w]
        else:
            return None  # Invalid input

    number += current
    return number

def number_to_words(number):
    # Dictionary to map numbers to words
    num_to_word = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        1000000: 'million',
        1000000000: 'billion'
    }

    if number == 0:
        return num_to_word[0]

    def convert_chunk(chunk):
        if chunk == 0:
            return ""
        words = []
        if chunk >= 100:
            hundred = chunk // 100
            words.append(num_to_word[hundred])
            words.append(num_to_word[100])
            chunk %= 100
        if chunk >= 20:
            tens = chunk // 10 * 10
            words.append(num_to_word[tens])
            chunk %= 10
        if chunk > 0 and chunk < 20:
            words.append(num_to_word[chunk])
        return ' '.join(words)

    words = []
    if number >= 1000000000:
        billion = number // 1000000000
        words.append(convert_chunk(billion))
        words.append(num_to_word[1000000000])
        number %= 1000000000
    if number >= 1000000:
        million = number // 1000000
        words.append(convert_chunk(million))
        words.append(num_to_word[1000000])
        number %= 1000000
    if number >= 1000:
        thousand = number // 1000
        words.append(convert_chunk(thousand))
        words.append(num_to_word[1000])
        number %= 1000
    if number > 0:
        words.append(convert_chunk(number))

    return ' '.join(words)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Convert string number to integer")
        print("2. Convert integer to string number")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            user_input = input("Enter a number in words: ")
            if user_input.replace(' ', '').replace('-', '').isalpha():
                result = words_to_number(user_input)
                if result is not None:
                    print(f"The numeric value is: {result}")
                else:
                    print("Invalid input: Not a valid number word.")
            else:
                print("Invalid input: Please enter a string (e.g., 'one hundred twenty-three').")

        elif choice == '2':
            user_input = input("Enter a number: ")
            if user_input.isdigit():
                result = number_to_words(int(user_input))
                print(f"The number in words is: {result}")
            else:
                print("Invalid input: Please enter a valid integer (e.g., 123).")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()