# Quiz 43
## SQL code
```.py
CREATE TABLE if not exists Movies(
    id INTEGER PRIMARY KEY,
    film_name TEXT,
    year_of_prod INTEGER NOT NULL,
    producer VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    budget INTEGER NOT NULL,
    category VARCHAR(255) NOT NULL
);

INSERT into Movies (film_name, year_of_prod, director, producer, budget, category) VALUES ('The Wedding Ringer', 2015, 'Jeremy Garelick', 'Will Packer', 23000000, 'Rom-com');
INSERT into Movies (film_name, year_of_prod, director, producer, budget, category) VALUES ('Rush Hour', 1998, ' Brett Ratner', 'Jonathan Glickman', 350000000, 'Action-comedy');

DELETE from Movies where id = 2;
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_043_result.png)

**Fig.1** Evidence for Quiz 43
