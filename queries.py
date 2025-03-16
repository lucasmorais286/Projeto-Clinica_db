from database import connect

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
