import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conn_str = "sqlite:///" + os.path.join(BASE_DIR, "database.db")