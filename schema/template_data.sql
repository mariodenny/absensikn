-- Users
INSERT INTO users (name, email, password, created_at) VALUES
('KN Admin', 'admin@knmedan.com', '$2a$12$ssuW0pnkF7nXzEHUncz3ue1En2/rSedSuFu6Zr.aiMDEPtZD4AZ4.', NOW()),
('KN Teacher 1', 'teacher1@knmedan.com', '$2a$12$ssuW0pnkF7nXzEHUncz3ue1En2/rSedSuFu6Zr.aiMDEPtZD4AZ4.', NOW()),
('KN Teacher 2', 'teacher2@knmedan.com', '$2a$12$ssuW0pnkF7nXzEHUncz3ue1En2/rSedSuFu6Zr.aiMDEPtZD4AZ4.', NOW()),
('KN Student Advisor', 'sa1@knmedan.com', '$2a$12$ssuW0pnkF7nXzEHUncz3ue1En2/rSedSuFu6Zr.aiMDEPtZD4AZ4.', NOW());

-- Roles
INSERT INTO roles (code, description) VALUES
('ADMIN', 'Administrator sistem'),
('TEACHER', 'Guru / pengajar'),
('SA', 'Student Advisor / admin kelas'),
('STUDENT', 'Murid / peserta kelas');

-- User Roles
INSERT INTO user_roles (user_id, role_id) VALUES
(1, 1), -- Admin KN → ADMIN
(2, 2), -- Teacher One → TEACHER
(3, 2), -- Teacher Two → TEACHER
(4, 3); -- SA One → SA
