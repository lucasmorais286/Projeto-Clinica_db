import psycopg2

DB_NAME = "clinica_db"
DB_USER = "seu_usuario"
DB_PASSWORD = "Llm1109@"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()
    
    queries = [
        """
        CREATE TABLE IF NOT EXISTS Clinics (
            ClinicID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Address TEXT NOT NULL,
            Phone VARCHAR(20),
            Specialty VARCHAR(100),
            OpeningHours VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Professionals (
            ProfessionalID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Specialty VARCHAR(100),
            Phone VARCHAR(20),
            Email VARCHAR(255) UNIQUE,
            ClinicID INT REFERENCES Clinics(ClinicID) ON DELETE CASCADE,
            Role VARCHAR(50)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Patients (
            PatientID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            BirthDate DATE NOT NULL,
            Phone VARCHAR(20),
            Email VARCHAR(255) UNIQUE,
            Address TEXT,
            Insurance VARCHAR(100)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Appointments (
            AppointmentID SERIAL PRIMARY KEY,
            ClinicID INT REFERENCES Clinics(ClinicID) ON DELETE CASCADE,
            ProfessionalID INT REFERENCES Professionals(ProfessionalID) ON DELETE CASCADE,
            PatientID INT REFERENCES Patients(PatientID) ON DELETE CASCADE,
            Date DATE NOT NULL,
            Time TIME NOT NULL,
            Reason TEXT,
            Status VARCHAR(50),
            AppointmentType VARCHAR(50)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Services (
            ServiceID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Description TEXT,
            Price DECIMAL(10,2) NOT NULL,
            Duration INTERVAL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS AppointmentServices (
            AppointmentID INT REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
            ServiceID INT REFERENCES Services(ServiceID) ON DELETE CASCADE,
            Quantity INT NOT NULL,
            PRIMARY KEY (AppointmentID, ServiceID)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Payments (
            PaymentID SERIAL PRIMARY KEY,
            PatientID INT REFERENCES Patients(PatientID) ON DELETE CASCADE,
            AppointmentID INT REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
            Amount DECIMAL(10,2) NOT NULL,
            PaymentMethod VARCHAR(50),
            Date DATE NOT NULL,
            Status VARCHAR(50),
            Discount DECIMAL(10,2)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS MedicalRecords (
            RecordID SERIAL PRIMARY KEY,
            PatientID INT REFERENCES Patients(PatientID) ON DELETE CASCADE,
            ProfessionalID INT REFERENCES Professionals(ProfessionalID) ON DELETE CASCADE,
            AppointmentID INT REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
            Diagnosis TEXT,
            Prescription TEXT,
            Observations TEXT,
            FollowUpDate DATE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Inventory (
            ItemID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Description TEXT,
            Quantity INT NOT NULL,
            UnitPrice DECIMAL(10,2),
            ClinicID INT REFERENCES Clinics(ClinicID) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Equipment (
            EquipmentID SERIAL PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Description TEXT,
            MaintenanceDate DATE,
            ClinicID INT REFERENCES Clinics(ClinicID) ON DELETE CASCADE
        )
        """
    ]
    
    for query in queries:
        cur.execute(query)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Tabelas criadas com sucesso!")