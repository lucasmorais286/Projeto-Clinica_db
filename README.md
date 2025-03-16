# Sistema de Gestão de Clínica

Este projeto é um sistema de gerenciamento de dados para uma clínica médica, com funcionalidades para gerenciar consultas, pacientes, profissionais, pagamentos e muito mais. O sistema é desenvolvido em Python, utilizando o banco de dados PostgreSQL para armazenar as informações.

## Funcionalidades

- **Gestão de Clínicas**: Cadastro de clínicas com informações como nome, endereço, especialidade e horário de funcionamento.
- **Gestão de Profissionais**: Cadastro de profissionais de saúde, associando-os a uma clínica e sua especialidade.
- **Gestão de Pacientes**: Cadastro de pacientes com informações como nome, data de nascimento, telefone, email e plano de saúde.
- **Agendamento de Consultas**: Agendamento de consultas com associados a profissionais e clínicas.
- **Gestão de Pagamentos**: Controle de pagamentos dos pacientes por consulta, com suporte a diferentes métodos de pagamento.
- **Serviços de Saúde**: Cadastro e associação de serviços de saúde oferecidos nas consultas.
- **Relatórios Financeiros**: Geração de relatórios financeiros baseados em pagamentos realizados por paciente, clínica ou status de pagamento.
- **Prontuários Médicos**: Registro de diagnósticos, prescrições e observações relacionadas a cada consulta.
- **Controle de Estoque e Equipamentos**: Gerenciamento de itens de estoque e equipamentos da clínica, com controle de quantidade e manutenção.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para desenvolvimento das funcionalidades.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar os dados.
- **psycopg2**: Biblioteca Python para interação com o banco de dados PostgreSQL.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- **`database.py`**: Contém funções de conexão com o banco de dados e criação das tabelas.
- **`queries.py`**: Contém funções de consulta e manipulação de dados, como inserção de dados e geração de relatórios.
- **`main.py`**: Arquivo principal para rodar o sistema, contendo a criação das tabelas e inserção de dados iniciais.

## Como Usar

### Pré-requisitos

- Python 3.x
- PostgreSQL
- Biblioteca `psycopg2`

### Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seuusuario/clinica-sistema.git
   cd clinica-sistema
