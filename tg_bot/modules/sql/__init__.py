from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI, KInit, log

client_encoding="postgresql-83028-0.cloudclusters.net"
echo=KInit.DEBUG

def start() -> scoped_session:
    engine = create_engine('postgresql://%s@%s/%s' % (DB_URI, client_encoding, echo))
    log.info("[PostgreSQL] Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
try:
    SESSION: scoped_session = start()
except Exception as e:
    log.exception(f'[PostgreSQL] Failed to connect due to {e}')
    exit()
   
log.info("[PostgreSQL] Connection successful, session started.")
