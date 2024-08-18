{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f322839f-a815-4a0d-8adf-02f04b0b1c82",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector\n",
    "\n",
    "def fetch_data(curr, query):\n",
    "    curr.execute(query)\n",
    "    return curr.fetchall()\n",
    "\n",
    "def main():\n",
    "    # Connect to the database\n",
    "    conn = mysql.connector.connect(\n",
    "        host=\"127.0.0.1\",\n",
    "        user=\"root\",\n",
    "        password=\"1234\",\n",
    "        database=\"projectp0\"\n",
    "    )\n",
    "    curr = conn.cursor()\n",
    "\n",
    "    # Define queries to fetch data\n",
    "    queries = {\n",
    "        \"Customer\": \"SELECT * FROM Customer LIMIT 5;\",\n",
    "        \"Product\": \"SELECT * FROM Product LIMIT 5;\",\n",
    "        \"Orders\": \"SELECT * FROM Orders LIMIT 5;\",\n",
    "        \"Payment\": \"SELECT * FROM Payment LIMIT 5;\"\n",
    "    }\n",
    "\n",
    "    # Fetch and display data\n",
    "    for table_name, query in queries.items():\n",
    "        data = fetch_data(curr, query)\n",
    "        print(f\"\\n{table_name} Data:\")\n",
    "        for row in data:\n",
    "            print(row)\n",
    "\n",
    "    # Close connection\n",
    "    curr.close()\n",
    "    conn.close()\n",
    "    print(\"Database connection closed.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
