from database import connect

# 🔹 LISTAR TODOS OS PACIENTES
def get_all_patients():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Patients ORDER BY Name
    """)
    patients = cur.fetchall()
    cur.close()
    conn.close()
    return patients

# 🔹 LISTAR TODOS OS PROFISSIONAIS
def get_all_professionals():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.*, c.Name as ClinicName 
        FROM Professionals p
        JOIN Clinics c ON p.ClinicID = c.ClinicID
        ORDER BY p.Name
    """)
    professionals = cur.fetchall()
    cur.close()
    conn.close()
    return professionals

# 🔹 LISTAR CONSULTAS POR CLÍNICA
def get_appointments_by_clinic(clinic_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            a.AppointmentID,
            c.Name as ClinicName,
            p.Name as ProfessionalName,
            pat.Name as PatientName,
            a.Date,
            a.Time,
            a.Status
        FROM Appointments a
        JOIN Clinics c ON a.ClinicID = c.ClinicID
        JOIN Professionals p ON a.ProfessionalID = p.ProfessionalID
        JOIN Patients pat ON a.PatientID = pat.PatientID
        WHERE a.ClinicID = %s
        ORDER BY a.Date DESC, a.Time DESC
    """, (clinic_id,))
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return appointments

# 🔹 LISTAR CONSULTAS POR PACIENTE COM DETALHES
def get_appointments_by_patient(patient_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            a.AppointmentID,
            c.Name as ClinicName,
            p.Name as ProfessionalName,
            a.Date,
            a.Time,
            a.Status,
            s.Name as ServiceName,
            s.Price,
            pay.PaymentMethod,
            pay.Status as PaymentStatus
        FROM Appointments a
        JOIN Clinics c ON a.ClinicID = c.ClinicID
        JOIN Professionals p ON a.ProfessionalID = p.ProfessionalID
        LEFT JOIN AppointmentServices aps ON a.AppointmentID = aps.AppointmentID
        LEFT JOIN Services s ON aps.ServiceID = s.ServiceID
        LEFT JOIN Payments pay ON a.AppointmentID = pay.AppointmentID
        WHERE a.PatientID = %s
        ORDER BY a.Date DESC, a.Time DESC
    """, (patient_id,))
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return appointments

# 🔹 LISTAR CONSULTAS POR PROFISSIONAL COM PRONTUÁRIOS
def get_appointments_by_professional(professional_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            a.AppointmentID,
            pat.Name as PatientName,
            a.Date,
            a.Time,
            a.Status,
            mr.Diagnosis,
            mr.Prescription,
            mr.Observations
        FROM Appointments a
        JOIN Patients pat ON a.PatientID = pat.PatientID
        LEFT JOIN MedicalRecords mr ON a.AppointmentID = mr.AppointmentID
        WHERE a.ProfessionalID = %s
        ORDER BY a.Date DESC, a.Time DESC
    """, (professional_id,))
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return appointments

# 🔹 LISTAR EQUIPAMENTOS POR CLÍNICA COM STATUS DE MANUTENÇÃO
def get_equipment_by_clinic(clinic_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            e.EquipmentID,
            e.Name,
            e.Description,
            e.MaintenanceDate,
            c.Name as ClinicName,
            CASE 
                WHEN e.MaintenanceDate < CURRENT_DATE THEN 'Manutenção Pendente'
                ELSE 'Em dia'
            END as MaintenanceStatus
        FROM Equipment e
        JOIN Clinics c ON e.ClinicID = c.ClinicID
        WHERE e.ClinicID = %s
        ORDER BY e.MaintenanceDate
    """, (clinic_id,))
    equipment = cur.fetchall()
    cur.close()
    conn.close()
    return equipment

# 🔹 LISTAR INVENTÁRIO COM BAIXO ESTOQUE
def get_low_inventory(min_quantity=10):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            i.ItemID,
            i.Name,
            i.Description,
            i.Quantity,
            i.UnitPrice,
            c.Name as ClinicName
        FROM Inventory i
        JOIN Clinics c ON i.ClinicID = c.ClinicID
        WHERE i.Quantity <= %s
        ORDER BY i.Quantity ASC
    """, (min_quantity,))
    inventory = cur.fetchall()
    cur.close()
    conn.close()
    return inventory

# 🔹 RELATÓRIO DE VALOR TOTAL DO INVENTÁRIO POR CLÍNICA
def get_inventory_value_by_clinic():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            c.Name as ClinicName,
            COUNT(i.ItemID) as TotalItems,
            SUM(i.Quantity) as TotalQuantity,
            SUM(i.Quantity * i.UnitPrice) as TotalValue
        FROM Clinics c
        LEFT JOIN Inventory i ON c.ClinicID = i.ClinicID
        GROUP BY c.ClinicID, c.Name
        ORDER BY TotalValue DESC
    """)
    report = cur.fetchall()
    cur.close()
    conn.close()
    return report

# 🔹 RELATÓRIO DE CONSULTAS E PAGAMENTOS
def get_appointment_payment_report():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            c.Name as ClinicName,
            COUNT(DISTINCT a.AppointmentID) as TotalAppointments,
            COUNT(DISTINCT p.PaymentID) as TotalPayments,
            COALESCE(SUM(p.Amount), 0) as TotalRevenue,
            COUNT(DISTINCT CASE WHEN p.Status = 'Pendente' THEN p.PaymentID END) as PendingPayments
        FROM Clinics c
        LEFT JOIN Appointments a ON c.ClinicID = a.ClinicID
        LEFT JOIN Payments p ON a.AppointmentID = p.AppointmentID
        GROUP BY c.ClinicID, c.Name
        ORDER BY TotalRevenue DESC
    """)
    report = cur.fetchall()
    cur.close()
    conn.close()
    return report

# 🔹 BUSCAR PROFISSIONAIS COM SUAS ESPECIALIDADES E TOTAL DE CONSULTAS
def get_professional_specialties_report():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            p.Name as ProfessionalName,
            p.Specialty,
            c.Name as ClinicName,
            COUNT(a.AppointmentID) as TotalAppointments,
            COUNT(DISTINCT pat.PatientID) as UniquePatients
        FROM Professionals p
        JOIN Clinics c ON p.ClinicID = c.ClinicID
        LEFT JOIN Appointments a ON p.ProfessionalID = a.ProfessionalID
        LEFT JOIN Patients pat ON a.PatientID = pat.PatientID
        GROUP BY p.ProfessionalID, p.Name, p.Specialty, c.Name
        ORDER BY TotalAppointments DESC
    """)
    report = cur.fetchall()
    cur.close()
    conn.close()
    return report

# 🔹 RELATÓRIO DE SERVIÇOS MAIS UTILIZADOS
def get_popular_services_report():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            s.Name as ServiceName,
            COUNT(aps.AppointmentID) as TimesUsed,
            AVG(s.Price) as AveragePrice,
            SUM(aps.Quantity) as TotalQuantity
        FROM Services s
        LEFT JOIN AppointmentServices aps ON s.ServiceID = aps.ServiceID
        GROUP BY s.ServiceID, s.Name
        ORDER BY TimesUsed DESC
    """)
    report = cur.fetchall()
    cur.close()
    conn.close()
    return report

# 🔹 LISTAR CONSULTAS POR STATUS
def get_appointments_by_status(status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Appointments
        WHERE Status = %s
        ORDER BY Date DESC, Time DESC
    """, (status,))
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return appointments

# 🔹 ATUALIZAR STATUS DE UMA CONSULTA
def update_appointment_status(appointment_id, status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Appointments
        SET Status = %s
        WHERE AppointmentID = %s
    """, (status, appointment_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Status da consulta {appointment_id} atualizado para '{status}' com sucesso!")

# 🔹 REMOVER UMA CONSULTA
def delete_appointment(appointment_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM Appointments
        WHERE AppointmentID = %s
    """, (appointment_id,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Consulta {appointment_id} removida com sucesso!")

# 🔹 REMOVER UM PACIENTE (VERIFICANDO CONSULTAS)
def delete_patient(patient_id):
    conn = connect()
    cur = conn.cursor()
    
    # Verifica se o paciente tem consultas associadas
    cur.execute("""
        SELECT COUNT(*) FROM Appointments WHERE PatientID = %s
    """, (patient_id,))
    count = cur.fetchone()[0]
    
    if count > 0:
        print(f"Erro: O paciente {patient_id} tem consultas registradas. Exclua as consultas antes de remover o paciente.")
    else:
        cur.execute("""
            DELETE FROM Patients WHERE PatientID = %s
        """, (patient_id,))
        conn.commit()
        print(f"Paciente {patient_id} removido com sucesso!")

    cur.close()
    conn.close()

# 🔹 LISTAR TODOS OS PAGAMENTOS
def get_all_payments():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Payments ORDER BY Date DESC
    """)
    payments = cur.fetchall()
    cur.close()
    conn.close()
    return payments

# 🔹 RELATÓRIO DE PAGAMENTOS POR PACIENTE
def get_payments_by_patient_report(patient_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUM(Amount), COUNT(*) 
        FROM Payments
        WHERE PatientID = %s
    """, (patient_id,))
    report = cur.fetchone()
    cur.close()
    conn.close()
    return report  # Retorna (total pago, número de pagamentos)

# 🔹 RELATÓRIO DE PAGAMENTOS POR CLÍNICA
def get_payments_by_clinic_report(clinic_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUM(p.Amount), COUNT(*)
        FROM Payments p
        JOIN Appointments a ON p.AppointmentID = a.AppointmentID
        WHERE a.ClinicID = %s
    """, (clinic_id,))
    report = cur.fetchone()
    cur.close()
    conn.close()
    return report  # Retorna (total pago, número de pagamentos)

# 🔹 RELATÓRIO DE PAGAMENTOS POR STATUS
def get_payments_by_status_report(status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUM(Amount), COUNT(*)
        FROM Payments
        WHERE Status = %s
    """, (status,))
    report = cur.fetchone()
    cur.close()
    conn.close()
    return report  # Retorna (total pago, número de pagamentos)
