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
    cursor = conn.cursor()
    query = """
        SELECT s.screening_id, f.title, COUNT(t.ticket_id) AS tickets_sold
        FROM screenings s
        JOIN films f ON s.film_id = f.film_id
        LEFT JOIN tickets t ON s.screening_id = t.screening_id
        GROUP BY s.screening_id, f.title
        ORDER BY tickets_sold DESC
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def top_customers_by_spend(conn, limit):
    cursor = conn.cursor()
    query = """
        SELECT c.customer_name, SUM(t.price) AS total_spent
        FROM customers c
        JOIN tickets t ON c.customer_id = t.customer_id
        GROUP BY c.customer_id, c.customer_name
        ORDER BY total_spent DESC
        LIMIT ?
    """
    cursor.execute(query, (limit,))
    results = cursor.fetchall()
    cursor.close()
    return results