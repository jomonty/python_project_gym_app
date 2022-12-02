DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS plans;
DROP TABLE IF EXISTS class_schedules;
DROP TABLE IF EXISTS class_images;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS instructors;

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN,
    capacity INT
);

CREATE TABLE class_images (
    id SERIAL PRIMARY KEY,
    class_id INT NOT NULL REFERENCES classes(id),
    class_image_path VARCHAR(255)
);

CREATE TABLE class_schedules (
    id SERIAL PRIMARY KEY,
    class_id INT NOT NULL REFERENCES classes(id),
    instructor_id INT NOT NULL REFERENCES instructors(id),
    date VARCHAR(255),
    start_time VARCHAR(255),
    duration_mins INT
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    address VARCHAR(255)
);

CREATE TABLE plans (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    member_id INT NOT NULL REFERENCES members(id),
    plan_id INT NOT NULL REFERENCES plans(id),
    active BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT NOT NULL REFERENCES members(id),
    class_schedule_id INT NOT NULL REFERENCES class_schedules(id)
);