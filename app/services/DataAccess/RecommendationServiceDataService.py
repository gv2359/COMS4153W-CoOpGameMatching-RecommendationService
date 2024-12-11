
from framework.services.data_access.MySQLDataService import MySQLDataService


class RecommendationDataService(MySQLDataService):

    def __init__(self, context):
        super().__init__(context)

    def initialize(self, database_name):
        """
        Creates the database and tables if they do not exist.
        """
        # Connect to MySQL server (without specifying a database)
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                # Create the database if it doesn't exist
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        # Ensure connection to the specific database for table creation
        self.context["database"] = database_name  # Update context with database name

        # Create tables in the specified database
        with self._get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"USE {database_name}")

                # Create the `game_info` table if it doesn't exist
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS game_info (
                        gameId CHAR(36) PRIMARY KEY,  -- Remove default UUID generation here
                        image VARCHAR(255),
                        title VARCHAR(255),
                        description TEXT,
                        genre TEXT
                    )
                """)
                connection.commit()

    def get_recommendations(self, game_id: str, num_recoms: int):

        database = self.context["database"]

        # Build the SQL query with optional filters
        base_query = f"SELECT * FROM {database}.game_info ORDER BY RAND()"

        base_query += " LIMIT %s"
        params = [num_recoms]

        # Execute the query and return the results
        return self.execute_query(base_query, params)
