CREATE TABLE TouristDestination (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX),
    location NVARCHAR(255),
    image_url NVARCHAR(500),
    best_season NVARCHAR(100),
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE TourService (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(255) NOT NULL,
    service_type NVARCHAR(100), -- Ví dụ: Nhà xe, Công ty du lịch, Tuyến tàu, Vé máy bay
    description NVARCHAR(MAX),
    price DECIMAL(18, 2),
    contact_info NVARCHAR(255),
    location NVARCHAR(255),
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE Booking (
    id INT PRIMARY KEY IDENTITY(1,1),
    tour_id INT FOREIGN KEY REFERENCES TouristDestination(id),
    service_id INT FOREIGN KEY REFERENCES TourService(id),
    customer_name NVARCHAR(255) NOT NULL,
    phone_number NVARCHAR(20) NOT NULL,
    address NVARCHAR(500) NOT NULL,
    email NVARCHAR(255),
    booking_date DATETIME DEFAULT GETDATE(),
    total_price DECIMAL(18, 2) NOT NULL,
    payment_status NVARCHAR(50), -- Ví dụ: Đã thanh toán, Chưa thanh toán
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE TransportRoute (
    id INT PRIMARY KEY IDENTITY(1,1),
    departure NVARCHAR(255) NOT NULL,
    destination NVARCHAR(255) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    price DECIMAL(18, 2),
    service_provider INT FOREIGN KEY REFERENCES TourService(id),
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE Payment (
    id INT PRIMARY KEY IDENTITY(1,1),
    booking_id INT FOREIGN KEY REFERENCES Booking(id),
    amount DECIMAL(18, 2) NOT NULL,
    payment_method NVARCHAR(50), -- Ví dụ: Thẻ tín dụng, Chuyển khoản, Tiền mặt
    payment_date DATETIME DEFAULT GETDATE(),
    payment_status NVARCHAR(50), -- Ví dụ: Thành công, Thất bại
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);
