# Quiz 34
## Code
```.py
def to_roman(num:int)->str:
    out = ""
    if num > 100:
        raise ValueError("Input must be less than or equal to 100")

    # Convert the input number to roman number
    if num == 100:
        out = "C"
        num = 0

    if num >= 90:
        out += "XC"
        num -= 90

    if num >= 50:
        out += "L"
        num -= 50

    if num >= 40:
        out += "XL"
        num -= 40

    if num >= 10:
        out += "X" * (num // 10)
        num %= 10

    if num >= 9:
        out += "IX"
        num -= 9

    if num >= 5:
        out += "V"
        num -= 5

    if num >= 4:
        out += "IV"
        num -= 4

    if num >= 1:
        out += "I" * num

    return out


print(to_roman(99))
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_034_result.png)

**Fig.1** Results of the test file
