import os
from psycopg import connect, sql
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL: conn = connect(DATABASE_URL)
else: conn = None  # Mock or in-memory DB setup
