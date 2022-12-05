DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    class_date VARCHAR(20),
    class_time VARCHAR(20),
    capacity INT,
    is_active BOOLEAN
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    is_premium BOOLEAN,
    is_active BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    class_id INT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
    member_id INT NOT NULL REFERENCES members(id) ON DELETE CASCADE
)