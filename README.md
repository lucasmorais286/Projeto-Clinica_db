# Sistema de Gestão de Clínica 🏥

Sistema de gerenciamento de dados para clínica médica desenvolvido em Python com PostgreSQL.

## Pré-requisitos 📋

1. Python 3.x instalado
2. PostgreSQL instalado e configurado
3. Biblioteca Python para PostgreSQL:
```bash
pip3 install psycopg2-binary
```

## Configuração 🔧

1. Configure as credenciais do banco no arquivo `database.py`:
```python
DB_NAME = "postgres"
DB_USER = "seu_usuario"
DB_PASSWORD = "sua_senha"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
```

## Executando o Projeto 🚀

1. Crie as tabelas:
```bash
python database.py
```

2. Insira dados de exemplo:
```bash
python main.py
```

3. Teste as consultas:
```bash
python test_queries.py
```

## ⚠️ Resolução de Problemas

Se encontrar erros de chave estrangeira ou sequência de IDs, execute no PostgreSQL:

```sql
-- Limpar todas as tabelas
TRUNCATE TABLE MedicalRecords, Payments, AppointmentServices, 
             Appointments, Services, Professionals, Patients, 
             Clinics, Inventory, Equipment CASCADE;

-- Resetar sequências
ALTER SEQUENCE "Clinics_ClinicID_seq" RESTART WITH 1;
ALTER SEQUENCE "Professionals_ProfessionalID_seq" RESTART WITH 1;
ALTER SEQUENCE "Patients_PatientID_seq" RESTART WITH 1;
ALTER SEQUENCE "Appointments_AppointmentID_seq" RESTART WITH 1;
ALTER SEQUENCE "Services_ServiceID_seq" RESTART WITH 1;
ALTER SEQUENCE "Payments_PaymentID_seq" RESTART WITH 1;
ALTER SEQUENCE "MedicalRecords_RecordID_seq" RESTART WITH 1;
ALTER SEQUENCE "Inventory_ItemID_seq" RESTART WITH 1;
ALTER SEQUENCE "Equipment_EquipmentID_seq" RESTART WITH 1;
```

Depois, execute novamente os passos 1, 2 e 3 da seção "Executando o Projeto".

## Funcionalidades ✨

- Gestão de Clínicas, Profissionais e Pacientes
- Agendamento de Consultas
- Gestão de Pagamentos e Serviços
- Relatórios Financeiros
- Prontuários Médicos
- Controle de Estoque e Equipamentos

## Contribuindo 🤝

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Suporte 💬

Em caso de dúvidas ou problemas, abra uma issue no repositório.
