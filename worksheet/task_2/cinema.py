"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Returns film title, screen, and price for a specific customer.
    Based on the DB schema:
    - films (title)
    - screenings (screen)
    - tickets (price, customer_id, screening_id)
    """
    cursor = conn.cursor()


    query = """
        SELECT films.title, screenings.screen, tickets.price
        FROM tickets
        JOIN screenings ON tickets.screening_id = screenings.screening_id
        JOIN films ON screenings.film_id = films.film_id
        WHERE tickets.customer_id = ?
        ORDER BY films.title ASC
    """

    cursor.execute(query, (customer_id,))
    results = cursor.fetchall()
    cursor.close()
    
    return results


def screening_sales(conn):
    """
    Write a function that returns the number of tickets sold for each screening.

    The function should return a list of tuples containing (in order):
    - the screening ID
    - the film title
    - the number of tickets sold

    All screenings should be included, even if no tickets were sold for that screening.

    Results should be ordered by the number of tickets sold, from highest to lowest.

    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    cursor = conn.cursor()
    query = """
        SELECT s.id, f.title, COUNT(t.id) AS tickets_sold
        FROM screenings s
        JOIN films f ON s.film_id = f.id
        LEFT JOIN tickets t ON s.id = t.screening_id
        GROUP BY s.id, f.title
        ORDER BY tickets_sold DESC
    """
    cursor.execute(query)
    return cursor.fetchall()


def top_customers_by_spend(conn, limit):
    """
    Write a function that returns the customers who have spent the most money on tickets.

    The function should return a list of tuples containing (in order):
    - the customer name
    - the total amount spent on tickets


    Only customers who have purchased at least one ticket should be included.

    Results should be ordered by total amount spent, from highest to lowest, and limited to a specified number of rows (passed in by the argument `limit`)
    
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    cursor = conn.cursor()
    query = """
        SELECT c.name, SUM(t.price) AS total_spent
        FROM customers c
        JOIN tickets t ON c.id = t.customer_id
        GROUP BY c.id, c.name
        ORDER BY total_spent DESC
        LIMIT ?
    """
    cursor.execute(query, (limit,))
    return cursor.fetchall()