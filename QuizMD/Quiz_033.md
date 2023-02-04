# Quiz 33
## Code
```.py
def mystery(list1:list, list2: list) -> list:
    output = []
    for l1_element in list1:
        for l2_element in list2:
            if l1_element == l2_element:
                output.append(l1_element)
    return output
```
## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_033_result.png)

**Fig.1** Test results
