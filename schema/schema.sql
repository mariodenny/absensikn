-- =========================================================
-- DATABASE
-- =========================================================
CREATE DATABASE IF NOT EXISTS absensi_kn
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE absensi_kn;

-- =========================================================
-- MASTER TABLES
-- =========================================================

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE roles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(20) NOT NULL UNIQUE COMMENT 'ADMIN, SA, TEACHER',
  description VARCHAR(255)
) ENGINE=InnoDB;

CREATE TABLE terms (
  id INT AUTO_INCREMENT PRIMARY KEY,
  term_code VARCHAR(5) NOT NULL COMMENT 'A, A+, B, B+, C, C+, D, D+',
  term_label VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE modules (
  id INT AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(20) NOT NULL UNIQUE COMMENT 'LK, JK8, JK12',
  name VARCHAR(100) NOT NULL,
  description TEXT
) ENGINE=InnoDB;

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  birth_date DATE,
  level VARCHAR(10) COMMENT 'LK / JK',
  status VARCHAR(20) COMMENT 'trial, active, completed, cancel'
) ENGINE=InnoDB;

-- =========================================================
-- CORE TABLES (HARUS DULUAN)
-- =========================================================

CREATE TABLE classes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  term_id INT NOT NULL,
  module_id INT NOT NULL,
  teacher_id INT NOT NULL,
  name VARCHAR(100) NOT NULL,
  max_sessions INT DEFAULT 20 COMMENT 'Default 20 per SOP',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_classes_term
    FOREIGN KEY (term_id) REFERENCES terms(id),
  CONSTRAINT fk_classes_module
    FOREIGN KEY (module_id) REFERENCES modules(id),
  CONSTRAINT fk_classes_teacher
    FOREIGN KEY (teacher_id) REFERENCES users(id)
) ENGINE=InnoDB;

CREATE TABLE class_sessions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  class_id INT NOT NULL,
  session_number INT NOT NULL COMMENT '1 - max_sessions',
  session_date DATE,
  topic VARCHAR(150),
  is_final_project BOOLEAN DEFAULT FALSE,
  CONSTRAINT fk_class_sessions_class
    FOREIGN KEY (class_id) REFERENCES classes(id)
    ON DELETE CASCADE,
  CONSTRAINT uq_class_session_number
    UNIQUE (class_id, session_number)
) ENGINE=InnoDB;

-- =========================================================
-- RELATION / PIVOT TABLES
-- =========================================================

CREATE TABLE user_roles (
  user_id INT NOT NULL,
  role_id INT NOT NULL,
  PRIMARY KEY (user_id, role_id),
  CONSTRAINT fk_user_roles_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE,
  CONSTRAINT fk_user_roles_role
    FOREIGN KEY (role_id) REFERENCES roles(id)
    ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE class_students (
  class_id INT NOT NULL,
  student_id INT NOT NULL,
  PRIMARY KEY (class_id, student_id),
  CONSTRAINT fk_class_students_class
    FOREIGN KEY (class_id) REFERENCES classes(id)
    ON DELETE CASCADE,
  CONSTRAINT fk_class_students_student
    FOREIGN KEY (student_id) REFERENCES students(id)
    ON DELETE CASCADE
) ENGINE=InnoDB;

-- =========================================================
-- ATTENDANCE
-- =========================================================

CREATE TABLE attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  class_session_id INT NOT NULL,
  student_id INT NOT NULL,
  status VARCHAR(20) NOT NULL COMMENT 'present, absent, consul',
  note TEXT,
  CONSTRAINT fk_attendance_session
    FOREIGN KEY (class_session_id) REFERENCES class_sessions(id)
    ON DELETE CASCADE,
  CONSTRAINT fk_attendance_student
    FOREIGN KEY (student_id) REFERENCES students(id)
    ON DELETE CASCADE,
  CONSTRAINT uq_attendance_unique
    UNIQUE (class_session_id, student_id)
) ENGINE=InnoDB;

-- =========================================================
-- END
-- =========================================================
