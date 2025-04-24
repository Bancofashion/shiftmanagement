from database import engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fix_indexes():
    try:
        with engine.connect() as connection:
            # Drop the problematic index if it exists
            connection.execute("DROP INDEX IF EXISTS ix_facturen_year_client ON facturen")
            
            # Create a new index using a different syntax
            connection.execute("""
                CREATE INDEX ix_facturen_year_client 
                ON facturen (LEFT(factuurnummer, 7))
            """)
            logger.info("Successfully created index on facturen table")
    except Exception as e:
        logger.error(f"Error fixing indexes: {str(e)}")

if __name__ == "__main__":
    fix_indexes() 