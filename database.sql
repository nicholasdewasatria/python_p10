CREATE DATABASE crud_sia;

CREATE TABLE students (
    npm VARCHAR(20) PRIMARY KEY,  -- NPM sebagai primary key
    name VARCHAR(100) NOT NULL,    -- Nama mahasiswa
    program VARCHAR(100) NOT NULL, -- Program studi
    faculty VARCHAR(100) NOT NULL -- Fakultas
);