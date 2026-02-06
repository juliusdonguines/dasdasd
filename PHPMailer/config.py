# config.py
# Configuration file for database and system constants

DB_CONFIG = {
    "host": "127.0.0.1",        # or public IP / domain
    "user": "root",             # your MySQL username
    "password": "",             # your MySQL password
    "database": "capstone"      # your database name
}

# Optional: Flask or API settings (for deployment)
APP_CONFIG = {
    "host": "0.0.0.0",
    "port": 5000,
    "debug": False
}
