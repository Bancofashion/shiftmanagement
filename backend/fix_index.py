from sqlalchemy import create_engine, text
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get database connection details from environment variables
DB_USER = os.getenv("DB_USER", "planner_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "planner_password")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "planner_db")

# Create database connection
DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def fix_indexes():
    try:
        with engine.connect() as connection:
            # Drop existing index if it exists
            connection.execute(text("""
                SELECT COUNT(1) INTO @index_exists 
                FROM INFORMATION_SCHEMA.STATISTICS 
                WHERE table_schema = :db_name 
                AND table_name = 'facturen' 
                AND index_name = 'ix_facturen_year_client'
            """), {"db_name": DB_NAME})
            
            connection.execute(text("""
                SET @sql = IF(@index_exists > 0, 
                    'DROP INDEX ix_facturen_year_client ON facturen',
                    'SELECT 1')
            """))
            
            connection.execute(text("PREPARE stmt FROM @sql"))
            connection.execute(text("EXECUTE stmt"))
            connection.execute(text("DEALLOCATE PREPARE stmt"))

            # Create new index
            connection.execute(text("""
                CREATE INDEX ix_facturen_year_client ON facturen (
                    LEFT(factuurnummer, 4),
                    opdrachtgever_id
                )
            """))
            
            logger.info("Successfully created index on facturen table")
            
    except Exception as e:
        logger.error(f"Error fixing indexes: {str(e)}")
        raise

if __name__ == "__main__":
    fix_indexes() 