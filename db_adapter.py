import psycopg2
from psycopg2 import Error

class DB():
    def query(query_str):
        try:
            connection = psycopg2.connect(user="cyohbduykqvubk",
                                          password="308cf370dd772d05166588f522fe3f314660db44aa8d303fab7a2a6c562198f7",
                                          host="ec2-54-75-224-168.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="d4qg2ovmhrrvsg")
            connection.autocommit = True
            cursor = connection.cursor()
            print(query_str)
            cursor.execute(query_str)
            result = cursor.fetchall()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
        return result