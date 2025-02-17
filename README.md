# Number-Translator

A versatile Python program to convert numbers into their word representations and vice versa. Perfect for educational purposes, data processing, or any application requiring number-to-text conversion.

## Introduction

The Number-Translator is a Python program that allows users to:

- Convert numeric values (e.g., 123) into their word representations (e.g., "one hundred twenty-three").
- Convert word representations of numbers (e.g., "two million") into their numeric equivalents (e.g., 2000000).

This tool is designed to handle large numbers (up to billions) and is case-insensitive. It also includes robust error handling to ensure accurate conversions.

## Features

### 1. Bidirectional Conversion:

- Convert numbers to words (e.g., 34500 → "thirty-four thousand five hundred").
- Convert words to numbers (e.g., "one million two hundred" → 1000200).

### 2. Large Number Support:

- Handles numbers up to billions (e.g., 1,000,000,000).

### 3. Error Handling:

- Detects invalid inputs (e.g., misspelled words or non-numeric strings).

### 4. User-Friendly Interface:

- Interactive menu for easy navigation.

### 5. Case-Insensitive:

- Accepts input in any case (e.g., "ONE HUNDRED" or "one hundred").

## Installation

### Clone the Repository:

1. Open your terminal or command prompt.
2. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/mncedisiHlonzi/Number-Translator-Python.git
   ```

3. Navigate to the project directory:

    ```bash
    cd Number-Translator-Python
    ```

### Run the Program:

1. Ensure you have Python 3.8 or higher installed. You can check your Python version by running:

    ```bash
    python --version
    ```

2. Run the program using the following command:

    ```bash
    python main.py
    ```

## Usage

### Choose an Option:

### 1. The program will display a menu:

    Choose an option:
    1. Convert string number to integer
    2. Convert integer to string number
    3. Exit

### 2. Follow the Prompts:

- For Option 1: Enter a number in words (e.g., "one hundred twenty-three").
- For Option 2: Enter a numeric value (e.g., 123).

### 3. View the Result:

- The program will display the converted value.

### 4. Exit:

- Choose Option 3 to exit the program.

## Examples

    Choose an option:
    1. Convert string number to integer
    2. Convert integer to string number
    3. Exit
    Enter your choice (1, 2, or 3): 1
    Enter a number in words: thirty seven million four hundred and sixty one thousand nine hundred and twenty five
    The numeric value is: 37461925

    Choose an option:
    1. Convert string number to integer
    2. Convert integer to string number
    3. Exit
    Enter your choice (1, 2, or 3): 2
    Enter a number: 5674832
    The number in words is: five million six hundred seventy four thousand eight hundred thirty two

    Choose an option:
    1. Convert string number to integer
    2. Convert integer to string number
    3. Exit
    Enter your choice (1, 2, or 3): 3
    Exiting the program. Goodbye!
