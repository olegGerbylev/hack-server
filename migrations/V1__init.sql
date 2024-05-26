CREATE TABLE users (
    token TEXT PRIMARY KEY,
    email TEXT NOT NULL unique,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    family_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    sex TEXT NOT NULL,
    dob TEXT NOT NULL,
    company TEXT NOT NULL,
    company_tin TEXT NOT NULL,
    passport_series TEXT NOT NULL,
    passport_id TEXT NOT NULL,
    issued_by TEXT NOT NULL,
    date_issue TEXT NOT NULL,
    department_code TEXT NOT NULL,
    location TEXT NOT NULL,
    ppd BOOLEAN NOT NULL DEFAULT TRUE
);
