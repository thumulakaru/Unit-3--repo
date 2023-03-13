# Quiz 45
## UML Diagram
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_045_UML_diag.jpeg)

**Fig.1** UML diagram for the database

## Question 1
Create the SQL queries to find the responsible for the fraudulent transaction.

```.sql
SELECT
  CASE
    WHEN total_deposits - total_withdrawals != balance THEN 'bad'
    ELSE 'good'
  END AS 'Status',
  total_deposits,
  total_withdrawals,
  balance,
  account_id

FROM (
  SELECT
    SUM(amount) AS total_deposits,
    account_id AS a_d_id
  FROM transactions
  WHERE transaction_type = 'deposit'
  GROUP BY account_id
),

(
  SELECT
    SUM(amount) AS total_withdrawals,
    account_id AS a_w_id
  FROM transactions
  WHERE transaction_type = 'withdraw'
  GROUP BY account_id
),

accounts
WHERE a_d_id = a_w_id
    AND a_d_id = accounts.account_id
    AND Status = "bad";;
```

![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_045_result_1.png)
**Fig.2** The answer for the above 

## Question 2
```.sql
SELECT customers.first_name, customers.last_name, accounts.account_id
FROM customers
JOIN accounts
ON customers.customer_id = accounts.customer_id
WHERE accounts.account_id IN (12, 13, 15, 17, 19);
```

![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_045_result_2.png)
