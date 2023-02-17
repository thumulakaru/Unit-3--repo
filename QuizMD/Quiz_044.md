# Quiz 44
## SQL code
```.sql
SELECT count(*) from sqlite_master where type = "table";
select count(*) from INHABITANT where gender = "Male" and state = "Friendly";
select avg(gold) from INHABITANT group by villageid;
select count(*) from ITEM where item like "A%";
select count(distinct job) from INHABITANT;
select item from ITEM, INHABITANT where (INHABITANT.personid = ITEM.owner) and (INHABITANT.job = "Herbalist")
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_044_result_1.png)

**Fig.1** 1st Question answer

![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_044_result_2.png)

**Fig.2** 2nd Question answer

![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_044_result_3.png)

**Fig.3** 3rd Question answer

![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_044_result_4.png)

**Fig.4** 4th Question answer

![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_044_result_5.png)

**Fig.5** 5th Question answer

![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_044_result_6.png)

**Fig.6** 6th Question answer
