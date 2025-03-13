# SQL

- Query - question or statement
- Not case sensitive - column names

## Exercise 1 — Tasks

1. Find the title of each film
   ```SQL
   SELECT title FROM movies;
   ```
2. Find the director of each film

   ```SQL
   SELECT director FROM movies;
   ```

3. Find the title and director of each film

   ```SQL
   SELECT title, director FROM movies;
   ```

4. Find the title and year of each film

   ```SQL
   SELECT title, year FROM movies;
   ```

5. Find all the information about each film

   ```SQL
   SELECT * FROM movies;
   ```

   ![alt text](image-1.png)

## Exercise 2 — Tasks

1. Find the movie with a row id of 6
   ```sql
    SELECT *
    FROM movies
    where id = 6;
   ```
2. Find the movies released in the years between 2000 and 2010

   ```sql
   SELECT *
   FROM movies
   where year between 2000 and 2010;
   ```

- Select all data from movies where the year matches condition
- Alternate way:
  ```sql
  SELECT *
  FROM movies
  WHERE year >= 2000 and year <=2010
  ```

1. Find the movies not released in the years between 2000 and 2010

   ```sql
    SELECT *
    FROM movies
    where year not between 2000 and 2010;
   ```

2. Find the first 5 Pixar movies and their release year

   ```sql
    SELECT *
    FROM movies
    where id in (1,2,3,4,5);
   ```

   - Alternate way

   ```sql
       Select title, year
       FROM movies
       LIMIT 5;
   ```

![alt text](image-2.png)

## Exercise 3 — Tasks

1. Find all the Toy Story movies

   ```sql
    SELECT *
    FROM movies
    WHERE title like "Toy Story%";
   ```

2. Find all the movies directed by John Lasseter

   ```sql
    SELECT *
    FROM movies
    WHERE director = "John Lasseter";
   ```

   - Can use `LIKE`

3. Find all the movies (and director) not directed by John Lasseter

   ```sql
    SELECT *
    FROM movies
    WHERE director != "John Lasseter";
   ```

   - Can use `NOT LIKE`
   -

4. Find all the WALL-\* movies

   - Answer 1

   ```sql
    SELECT *
    FROM movies
    WHERE title like "WALL-%";
   ```

   - Answer 2

   ```sql
   SELECT *
   FROM movies
   WHERE title like "WALL-_";
   ```

   ![alt text](image-3.png)

# Exercise 4 — Tasks

1. List all directors of Pixar movies (alphabetically), without duplicates

   ```sql
    SELECT DISTINCT director
    FROM movies
    ORDER BY director;
   ```

2. List the last four Pixar movies released (ordered from most recent to least)

   ```sql
    SELECT *
    FROM movies
    ORDER BY year DESC
    LIMIT 4;
   ```

3. List the first five Pixar movies sorted alphabetically

   ```sql
    SELECT *
    FROM movies
    ORDER BY title
    LIMIT 5;
   ```

4. List the next five Pixar movies sorted alphabetically

   ```sql
    SELECT *
    FROM movies
    ORDER BY title
    LIMIT 5 OFFSET 5;
   ```

   ![alt text](image-4.png)

## Review 1 — Tasks

1. List all the Canadian cities and their populations

   ```sql
    SELECT *
    FROM north_american_cities
    WHERE country = "Canada";
   ```

2. Order all the cities in the United States by their latitude from north to south

   ```sql
    SELECT *
    FROM north_american_cities
    WHERE country = "United States"
    ORDER BY latitude DESC;
   ```

3. List all the cities west of Chicago, ordered from west to east

   ```sql
    SELECT * FROM north_american_cities
    WHERE longitude < -87.629798
    ORDER BY longitude;
   ```

   - not recommended to hard code -87.629798 (longitude)
   - Recommended Answer (Sub-Query)

     ```sql
     SELECT *
     FROM north_american_cities
     Where longitude < (
     SELECT longitude
     FROM north_american_cities
     Where city = "Chicago"
     )
     Order By longitude;
     ```

   ```

   ```

4. List the two largest cities in Mexico (by population)

   ```sql
    SELECT * FROM north_american_cities
    WHERE country = "Mexico"
    ORDER BY population DESC
    LIMIT 2;
   ```

5. List the third and fourth largest cities (by population) in the United States and their population

   ```SQL
    SELECT * FROM north_american_cities
    WHERE country = "United States"
    ORDER BY population DESC
    LIMIT 2 OFFSET 2;
   ```

![alt text](image-5.png)
