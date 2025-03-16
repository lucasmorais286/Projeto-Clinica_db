# main.py
from database import create_tables, connect

def insert_sample_data():
    conn = connect()
    cur = conn.cursor()
    
    # Inserir Clínicas
    cur.execute("""
        INSERT INTO Clinics (Name, Address, Phone, Specialty, OpeningHours) VALUES
        ('Clínica A', 'Rua 1', '1111-1111', 'Cardiologia', '08:00-18:00'),
        ('Clínica B', 'Rua 2', '2222-2222', 'Ortopedia', '09:00-19:00'),
        ('Clínica C', 'Rua 3', '3333-3333', 'Dermatologia', '10:00-20:00'),
        ('Clínica D', 'Rua 4', '4444-4444', 'Pediatria', '07:00-17:00'),
        ('Clínica E', 'Rua 5', '5555-5555', 'Neurologia', '08:30-18:30')
    """)
    
    # Inserir Profissionais
    cur.execute("""
        INSERT INTO Professionals (Name, Specialty, Phone, Email, ClinicID, Role) VALUES
        ('Dr. João', 'Cardiologia', '9999-9999', 'joao@clinica.com', 1, 'Médico'),
        ('Dra. Maria', 'Ortopedia', '8888-8888', 'maria@clinica.com', 2, 'Médica'),
        ('Dr. Carlos', 'Dermatologia', '7777-7777', 'carlos@clinica.com', 3, 'Médico'),
        ('Ana Souza', NULL, '6666-6666', 'ana@clinica.com', 1, 'Recepcionista'),
        ('Paulo Lima', NULL, '5555-5555', 'paulo@clinica.com', 2, 'Técnico')
    """)
    
    # Inserir Pacientes
    cur.execute("""
        INSERT INTO Patients (Name, BirthDate, Phone, Email, Address, Insurance) VALUES
        ('Lucas Silva', '1990-05-15', '4444-4444', 'lucas@email.com', 'Rua X', 'Unimed'),
        ('Mariana Costa', '1985-08-20', '3333-3333', 'mariana@email.com', 'Rua Y', 'Particular'),
        ('José Pereira', '1972-11-10', '2222-2222', 'jose@email.com', 'Rua Z', 'SulAmérica'),
        ('Fernanda Lima', '2000-02-05', '1111-1111', 'fernanda@email.com', 'Rua W', 'Hapvida'),
        ('Carlos Mendes', '1995-06-25', '0000-0000', 'carlos@email.com', 'Rua V', 'Particular')
    """)
    
    # Inserir Consultas
    cur.execute("""
        INSERT INTO Appointments (ClinicID, ProfessionalID, PatientID, Date, Time, Reason, Status, AppointmentType) VALUES
        (1, 1, 1, '2024-03-01', '10:00', 'Check-up', 'Agendado', 'Presencial'),
        (2, 2, 2, '2024-03-02', '11:00', 'Dor no joelho', 'Concluído', 'Presencial'),
        (3, 3, 3, '2024-03-03', '12:00', 'Alergia na pele', 'Cancelado', 'Teleconsulta'),
        (4, 1, 4, '2024-03-04', '13:00', 'Exame de rotina', 'Agendado', 'Presencial'),
        (5, 2, 5, '2024-03-05', '14:00', 'Consulta neurológica', 'Concluído', 'Presencial')
    """)
    
    # Inserir Serviços
    cur.execute("""
        INSERT INTO Services (Name, Description, Price, Duration) VALUES
        ('Consulta Cardiológica', 'Avaliação do coração', 200.00, 30),
        ('Fisioterapia', 'Reabilitação muscular', 150.00, 40),
        ('Exame de Sangue', 'Coleta para exames laboratoriais', 80.00, 20),
        ('Ultrassom', 'Imagem interna do corpo', 250.00, 50),
        ('Consulta Dermatológica', 'Avaliação da pele', 180.00, 30)
    """)
    
    # Inserir Serviços por Consulta
    cur.execute("""
        INSERT INTO AppointmentServices (AppointmentID, ServiceID, Quantity) VALUES
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 1),
        (4, 4, 1),
        (5, 5, 2)
    """)
    
    # Inserir Pagamentos
    cur.execute("""
        INSERT INTO Payments (PatientID, AppointmentID, Amount, PaymentMethod, Date, Status, Discount) VALUES
        (1, 1, 200.00, 'Cartão', '2024-03-01', 'Pago', 0),
        (2, 2, 300.00, 'Pix', '2024-03-02', 'Pago', 10),
        (3, 3, 100.00, 'Dinheiro', '2024-03-03', 'Pendente', 5),
        (4, 4, 150.00, 'Cartão', '2024-03-04', 'Pago', 0),
        (5, 5, 250.00, 'Pix', '2024-03-05', 'Pago', 20)
    """)
    
    # Inserir Prontuários
    cur.execute("""
        INSERT INTO MedicalRecords (PatientID, ProfessionalID, AppointmentID, Diagnosis, Prescription, Observations, FollowUpDate) VALUES
        (1, 1, 1, 'Hipertensão', 'Remédio X', 'Monitorar pressão', '2024-06-01'),
        (2, 2, 2, 'Lesão no joelho', 'Fisioterapia', 'Evitar esforço', '2024-07-01'),
        (3, 3, 3, 'Alergia', 'Antialérgico', 'Evitar alérgenos', '2024-05-10'),
        (4, 1, 4, 'Check-up normal', 'Nenhum', 'Revisão anual', '2025-01-01'),
        (5, 2, 5, 'Enxaqueca', 'Analgésico', 'Reduzir estresse', '2024-08-15')
    """)
    
    conn.commit()
    cur.close()
    conn.close()
    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    print("Banco de dados e dados iniciais prontos!")
