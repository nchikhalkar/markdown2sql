# markdown2sql
Converts Markdown Tables into SQL Create and Insert Statements

This is a Flask application which converts Markdown Tables into SQL DML syntax. You can copy the Markdown and Paste it in the Application UI, it will provide SQL code to create the table and insert data into it.

sample input:

![image](https://github.com/nchikhalkar/markdown2sql/assets/98278612/e270c67c-ff7c-4ade-aac0-b280f3216a7d)

COPY THE BELOW TEXT to use as sample input

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+



Output:


Create Table SQL:
CREATE TABLE your_table_name (
    name STRING,
    population STRING,
    area STRING
);
Insert Statements:
        
            INSERT INTO your_table_name (name, population, area) VALUES ("Afghanistan", "25500100", "652230");
        
            INSERT INTO your_table_name (name, population, area) VALUES ("Algeria", "37100000", "2381741");



-------------------------------------------

## USE CASE:
Leetcode Problems can be solved on any database using this application, we can copy the markdown and create a table in our environment and can use that for practise or tests.


-------------------------------------------

## Application Screenshots:


![image](https://github.com/nchikhalkar/markdown2sql/assets/98278612/9453ff60-f5bb-4353-b299-924edf849f49)


![image](https://github.com/nchikhalkar/markdown2sql/assets/98278612/a175b363-e267-4fea-b1a5-f39284741831)

