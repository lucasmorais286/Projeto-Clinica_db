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

