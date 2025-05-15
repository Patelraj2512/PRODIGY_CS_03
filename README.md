# Password Strength Checker

A simple yet effective Python application that evaluates password strength and provides feedback for improvement.

## Overview

This Password Strength Checker analyzes passwords based on multiple security criteria and provides instant feedback on their strength. It helps users create stronger passwords by offering specific suggestions for improvement.

## Features

- **Comprehensive Strength Analysis**: Evaluates passwords based on 5 key criteria:
  - Length (minimum 8 characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Presence of numbers
  - Presence of special characters

- **Strength Rating**: Categorizes passwords as:
  - Strong 💪 (meets all criteria)
  - Moderate 👍 (meets 3-4 criteria)
  - Weak ⚠️ (meets 0-2 criteria)

- **Detailed Feedback**: Provides specific suggestions to improve password strength

- **User-Friendly Interface**: Simple command-line interface with clear visual indicators

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/password-strength-checker.git
   ```

2. Navigate to the project directory:
   ```
   cd password-strength-checker
   ```

3. No additional dependencies required - the script uses only Python standard libraries!

## Usage

Run the script using Python:

```
python task3.py
```

Follow the prompts to enter a password, and the application will provide immediate feedback on its strength.

## Example

```
=== Password Strength Checker ===
Enter a password to check: MyWeakPwd1

Password Strength: Moderate 👍
Suggestions to improve:
❌ Include at least one special character (e.g., !, @, #, etc.).
```

## Why Password Strength Matters

Strong passwords are essential for protecting your accounts from unauthorized access. A strong password:
- Is harder to guess through brute force attacks
- Provides better protection against dictionary attacks
- Reduces the risk of credential stuffing if other accounts are compromised

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Developed as part of Prodigy InfoTech Internship - Task 3