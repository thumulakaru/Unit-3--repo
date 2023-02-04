# Quiz 38
## Code
```.py
from matplotlib import pyplot as plt, pyplot
import random
from Lessons.composition_travelling_salesman import City, Coordinate,country

city_name = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose"]

capital = City("Washington DC", Coordinate(38.8951, -77.0367))
us = country("United States", capital)

for name in city_name:
    city = City(name, Coordinate(random.randint(0,100), random.randint(0,100)))
    us.new_city(city)


x = []
y = []
label = []
for city in us.get_cities():
    x.append(city.location.x)
    y.append(city.location.y)
    label.append(city.name)
plt.scatter(x, y, s=100)
for i, label in enumerate(label):
    plt.annotate(label, (x[i], y[i]))
plt.xlabel("Distance(km)")
plt.ylabel("Distance(km)")
plt.show()
```

## Evidence
![](https://github.com/thumulakaru/Unit-3--repo/blob/main/Quizzes/Quiz_038_result.png)

**Fig.1** Results after running the code
