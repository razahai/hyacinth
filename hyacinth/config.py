import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev").encode("utf-8")

DATABASE_URI = os.getenv("DATABASE_URI", "hyacinth.db")

RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY", "6LfvVmEqAAAAAKAZFnnr26IHuXOaeVVDRnjDO1Fj")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY", "6LfvVmEqAAAAAFMOGAft_1ov8pRVFpBl29Ti9OJg")

UPLOAD_PATH = "jobs"
ALLOWED_FILE_TYPES = ["jpg", "jpeg", "png", "pdf", "docx", "doc", "odt", "webp"]
MAX_FILE_SIZE = 64 * 1024 * 1024 # 64 MB
MAX_PAGES_PER_JOB = 10
PRINT_JOB_RATE_LIMIT = 5 

REQUEST_FORM = "https://forms.gle/eUXYWj34nxLmn8Xb7"