from pony import orm

from app.config import Config

db = orm.Database()

def init_database_connection():
  # orm.sql_debug(Config.debug_mode)
  db.bind(provider='postgres', user=Config.db_user, password=Config.db_pass, host=Config.db_host, database=Config.db_name)
  db.generate_mapping(create_tables=True, check_tables=True)
