# Leeds Eats

You've been asked by a local food delivery company to create a management dashboard to help them monitor customer and driver data.
A database and diagram have been provided to show you the table names and relationships.

A basic menu has been written for you, which calls the functions which you need to fill in.

You will need to use a range of the SQL features you have already learned!

You should print out data in a clear and human-readible way - use linebreaks (`\n`) and tab breaks (`\t`) where needed.

## Section 1 - Summaries

1. Display the total number of customers.
2. Show the earliest and latest customer signup dates.
3. Display:
- total number of orders
- average order value
- highest and lowest order totals
4. Display the total number of drivers and their hire dates.

## Section 2 - Key Statistics

5. Orders per customer
- Customer name
- Number of orders
- Total amount spent


6. Driver workload
- Driver name
- Number of deliveries completed


7. Order delivery Lookup - search for an individual order
- search for an order by ID
- customer name
- order total
- delivery date
- driver



## Section 3 - Time-based Summaries

8. Count the number of orders per order date.
9. Count the number of deliveries per delivery date.
10. Count customer signups per month - you may need to do some python processing on this one!

## Section 4 - Performance and Rankings

11. List the top 5 customers by total spend.
12. Rank drivers by number of deliveries completed.
13. Display all orders above a value which should be inputted by the user (e.g. £100)

## Section 5 - Stretch Goals - Charts

These extension tasks draw on the **visualisation** work you did last semester - you will need to import and use matplotlib (or the visualisation library of your choice) to create some graphs.

Rather than giving you specific instructions, interpret these requests from the management team - think about what data they need, and the best way to show it (you can use charts or tables):

1. "Which days are we busiest?"
2. "I need to see whether the business is getting more orders over time"
3. "Do we have enough drivers to keep up with orders?"
4. "Are all the drivers being given the same workload?"
5. "Are there any obvious peaks or quiet periods we should look at?"
6. "Do we make most of our money from small orders, or from large orders?"

Functions have not been pre-written for these, and it's up to you how you want to tackle them.

## General Tips
h
You can always write and test your SQL in a sql file first to check that it finds the data you expect.

It's a good idea to start by constructing the joins before you worry about what data you want to get out of the table - when you have the columns you need, then move on to picking out the columns and any processing to be done on them.