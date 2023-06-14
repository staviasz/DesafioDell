import sqlite3

try:
    sqlite3.connect(":memory:")
    print("O módulo sqlite3 está instalado.")
except ImportError:
    print("O módulo sqlite3 não está instalado.")
