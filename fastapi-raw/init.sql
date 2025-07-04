-- Initialize the database
USE sbtest;

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_id (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert some sample data (optional)
INSERT INTO users (name) VALUES 
    ('John Doe'),
    ('Jane Smith'),
    ('Bob Johnson');

-- Grant permissions
GRANT ALL PRIVILEGES ON sbtest.* TO 'app_user'@'%';
FLUSH PRIVILEGES;