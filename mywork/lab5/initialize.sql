CREATE DATABASE theater_db;
USE theater_db;

CREATE TABLE productions (
    production_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    opening_date DATE
);

CREATE TABLE cast_members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(255) NOT NULL,
    role_type VARCHAR(100),
    production_id INT,
    FOREIGN KEY (production_id) REFERENCES productions(production_id)
);

INSERT INTO productions (title, genre, opening_date) VALUES 
('Hamilton', 'Musical', '2026-01-15'),
('Dear Evan Hansen', 'Musical', '2026-02-10'),
('Wicked', 'Musical', '2025-11-20'),
('Hadestown', 'Folk Opera', '2026-03-05'),
('The Lion King', 'Musical', '2025-09-12'),
('Les Misérables', 'Epic Musical', '2025-12-01'),
('The Phantom of the Opera', 'Musical', '2026-01-20'),
('Waitress', 'Musical', '2026-04-10'),
('Six', 'Pop Musical', '2025-10-30'),
('Moulin Rouge!', 'Jukebox Musical', '2026-05-15');

INSERT INTO cast_members (full_name, role_type, production_id) VALUES 
('Alexander Hamilton', 'Lead', 1),
('Evan Hansen', 'Lead', 2),
('Elphaba', 'Lead', 3),
('Orpheus', 'Lead', 4),
('Simba', 'Lead', 5),
('Jean Valjean', 'Lead', 6),
('The Phantom', 'Lead', 7),
('Jenna Hunterson', 'Lead', 8),
('Anne Boleyn', 'Lead', 9),
('Satine', 'Lead', 10);