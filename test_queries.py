from queries import (
    get_all_patients,
    get_all_professionals,
    get_appointments_by_clinic,
    get_appointments_by_patient,
    get_appointments_by_professional,
    get_appointments_by_status,
    get_equipment_by_clinic,
    get_low_inventory,
    get_inventory_value_by_clinic,
    get_appointment_payment_report,
    get_professional_specialties_report,
    get_popular_services_report
)

def test_queries():
    print("\n🔹 Testando todas as funções de consulta 🔹\n")

    # Teste: Listar todos os pacientes
    print("\n1. Listando todos os pacientes:")
    patients = get_all_patients()
    for patient in patients:
        print(f"ID: {patient[0]}, Nome: {patient[1]}, Data Nasc.: {patient[2]}, Telefone: {patient[3]}")

    # Teste: Listar todos os profissionais com suas clínicas
    print("\n2. Listando todos os profissionais:")
    professionals = get_all_professionals()
    for prof in professionals:
        print(f"ID: {prof[0]}, Nome: {prof[1]}, Especialidade: {prof[2]}, Clínica: {prof[7]}")

    # Teste: Listar consultas detalhadas da Clínica A
    print("\n3. Listando consultas detalhadas da Clínica A (ID=1):")
    clinic_appointments = get_appointments_by_clinic(1)
    for app in clinic_appointments:
        print(f"ID: {app[0]}, Clínica: {app[1]}, Profissional: {app[2]}, Paciente: {app[3]}, Data: {app[4]}, Hora: {app[5]}")

    # Teste: Listar consultas detalhadas do paciente
    print("\n4. Listando consultas detalhadas do paciente Lucas Silva (ID=1):")
    patient_appointments = get_appointments_by_patient(1)
    for app in patient_appointments:
        print(f"Consulta: {app[0]}, Clínica: {app[1]}, Profissional: {app[2]}, Serviço: {app[6]}, Valor: R${app[7]}")

    # Teste: Listar consultas e prontuários do profissional
    print("\n5. Listando consultas e prontuários do Dr. João (ID=1):")
    professional_appointments = get_appointments_by_professional(1)
    for app in professional_appointments:
        print(f"Consulta: {app[0]}, Paciente: {app[1]}, Data: {app[2]}, Diagnóstico: {app[5]}")

    # Teste: Listar equipamentos da clínica
    print("\n6. Listando equipamentos da Clínica A (ID=1):")
    equipment = get_equipment_by_clinic(1)
    for eq in equipment:
        print(f"ID: {eq[0]}, Nome: {eq[1]}, Status: {eq[5]}")

    # Teste: Listar itens com baixo estoque
    print("\n7. Listando itens com estoque baixo (menos de 10 unidades):")
    low_stock = get_low_inventory(10)
    for item in low_stock:
        print(f"Item: {item[1]}, Quantidade: {item[3]}, Clínica: {item[5]}")

    # Teste: Relatório de valor do inventário por clínica
    print("\n8. Relatório de valor do inventário por clínica:")
    inventory_value = get_inventory_value_by_clinic()
    for inv in inventory_value:
        total_items = inv[1] if inv[1] is not None else 0
        total_value = inv[3] if inv[3] is not None else 0.0
        print(f"Clínica: {inv[0]}, Total Items: {total_items}, Valor Total: R${total_value:.2f}")

    # Teste: Relatório de consultas e pagamentos
    print("\n9. Relatório de consultas e pagamentos por clínica:")
    appointment_payment = get_appointment_payment_report()
    for ap in appointment_payment:
        print(f"Clínica: {ap[0]}, Consultas: {ap[1]}, Pagamentos: {ap[2]}, Receita: R${ap[3]:.2f}")

    # Teste: Relatório de profissionais e especialidades
    print("\n10. Relatório de profissionais e suas especialidades:")
    prof_specialties = get_professional_specialties_report()
    for ps in prof_specialties:
        print(f"Profissional: {ps[0]}, Especialidade: {ps[1]}, Total Consultas: {ps[3]}")

    # Teste: Relatório de serviços populares
    print("\n11. Relatório de serviços mais utilizados:")
    popular_services = get_popular_services_report()
    for ps in popular_services:
        print(f"Serviço: {ps[0]}, Utilizações: {ps[1]}, Preço Médio: R${ps[2]:.2f}")



    print("\n✅ Todos os testes de consulta foram executados!")

if __name__ == "__main__":
    test_queries() 