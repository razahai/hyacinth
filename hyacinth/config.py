import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev").encode("utf-8")