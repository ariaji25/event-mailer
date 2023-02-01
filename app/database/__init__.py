from pony import orm

from app.config import Config

db = orm.Database()

def init_database_connection():
  # orm.sql_debug(Config.debug_mode)
  db.bind('sqlite', '../../db.sql')
  db.generate_mapping(create_tables=True, check_tables=True)
