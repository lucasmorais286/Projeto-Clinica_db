from database import connect

#Appointments--------------------------------------------------

def get_appointments_by_patient(patient_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Appointments
        WHERE PatientID = %s
    """, (patient_id,))
    
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return appointments

def get_appointments_by_status(status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Appointments
        WHERE Status = %s
    """, (status,))
    
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return appointments

def get_appointments_by_professional(professional_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Appointments
        WHERE ProfessionalID = %s
    """, (professional_id,))
    
    appointments = cur.fetchall()
    cur.close()
    conn.close()
    return appointments


#Payments---------------------------------------------------------------

def get_payments_by_patient(patient_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Payments
        WHERE PatientID = %s
    """, (patient_id,))
    
    payments = cur.fetchall()
    cur.close()
    conn.close()
    return payments

def get_payments_by_status(status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Payments
        WHERE Status = %s
    """, (status,))
    
    payments = cur.fetchall()
    cur.close()
    conn.close()
    return payments

def get_payments_by_appointment(appointment_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Payments
        WHERE AppointmentID = %s
    """, (appointment_id,))
    
    payments = cur.fetchall()
    cur.close()
    conn.close()
    return payments


#Services-----------------------------------------

def get_all_services():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Services
    """)
    
    services = cur.fetchall()
    cur.close()
    conn.close()
    return services


#MedicalRecords------------------------------------------------------

def get_medical_records_by_patient(patient_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM MedicalRecords
        WHERE PatientID = %s
    """, (patient_id,))
    
    medical_records = cur.fetchall()
    cur.close()
    conn.close()
    return medical_records

def get_medical_records_by_professional(professional_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM MedicalRecords
        WHERE ProfessionalID = %s
    """, (professional_id,))
    
    medical_records = cur.fetchall()
    cur.close()
    conn.close()
    return medical_records


#UpdateStatus-------------------------------------------------------
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

