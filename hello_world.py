"""query to produce which city was hottest in July 2013"""
SELECT * FROM weather WHERE average_high = (SELECT MAX(average_high) FROM weather);
"""first two cities which were coldest in January"""
SELECT * FROM weather WHERE cold_month = 'January' ORDER BY average_high LIMIT 2;
"""hottest in July and not coldest in January"""
SELECT city FROM weather WHERE cold_month != 'January' AND warm_month = 'July';


#Lesson 3.3
#Write a SQL statement which finds the mean of the average high temperatures for all of the cities within a state.
SELECT AVG(average_high) FROM weather INNER JOIN cities ON name = city WHERE state = 'CA';
#Result 69.5

