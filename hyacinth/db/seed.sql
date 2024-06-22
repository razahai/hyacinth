DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS jobs;

CREATE TABLE users (
    id TEXT UNIQUE NOT NULL PRIMARY KEY, 
    delivery_address TEXT NOT NULL
);

CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    file_name TEXT NOT NULL,
    job_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    job_status TEXT NOT NULL CHECK (job_status IN ('delivered', 'in_progress', 'pending')),
    FOREIGN KEY (user_id) REFERENCES users (id)
);