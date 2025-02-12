# CRM Tool - Python Project

This project is a simple Customer Relationship Management (CRM) tool built in Python. It allows you to manage contacts, appointments, and schedules directly from the command line.

## Features
1. **Contact Management**: Add, update, remove, and list contacts (name, phone, email);
2. **Task and Appointment Scheduling**: Add, update, remove, and list appointments (title, date/time, description);
3. **Activity Tracking**: Tracking interactions with customers, such as calls and meetings;

## 🏗️ **Classes e Funcionalidades**

### 📌 `Contact`
Classe que representa um **contato** no sistema.

#### **Atributos**:
- `cpf`: Identificador único do contato.
- `name`: Nome do contato.
- `phone`: Número de telefone.
- `email`: Endereço de e-mail.

#### **Métodos**:
- `__str__()`: Retorna uma string formatada com os dados do contato.

---

### 📌 `ContactManager`
Classe responsável por gerenciar os contatos.

#### **Atributos**:
- `contacts`: Dicionário que armazena os contatos cadastrados.

#### **Métodos**:
- `add_contact(cpf, name, phone, email)`: Adiciona um novo contato.
- `list_contacts()`: Lista todos os contatos cadastrados.
- `search_contact(cpf)`: Retorna um contato pelo CPF.
- `remove_contact(cpf)`: Remove um contato pelo CPF.
- `update_contact(cpf, name, phone, email)`: Atualiza as informações de um contato.

---

### 📌 `SalesOpportunity`
Classe que representa uma **oportunidade de venda**.

#### **Atributos**:
- `cpf`: CPF do contato relacionado à oportunidade.
- `description`: Descrição da oportunidade.
- `stage`: Estágio da oportunidade (ex.: Prospecção, Negociação, Fechado).

#### **Métodos**:
- `__str__()`: Retorna uma string formatada com os dados da oportunidade.

---

### 📌 `SalesPipeline`
Classe responsável por gerenciar oportunidades de vendas.

#### **Atributos**:
- `opportunities`: Lista de oportunidades de venda.
- `contact_manager`: Instância de `ContactManager` para buscar contatos.

#### **Métodos**:
- `add_opportunity()`: Adiciona uma nova oportunidade.
- `list_opportunities()`: Lista todas as oportunidades cadastradas.

---

### 📌 `Activity`
Classe que representa uma **atividade** relacionada a um contato.

#### **Atributos**:
- `cpf`: CPF do contato associado à atividade.
- `activity_type`: Tipo da atividade (ex.: chamada, reunião, e-mail).
- `description`: Descrição da interação.
- `timestamp`: Data e hora da atividade.

#### **Métodos**:
- `__str__()`: Retorna uma string formatada com os detalhes da atividade.

---

### 📌 `ActivityTracker`
Classe responsável por rastrear atividades.

#### **Atributos**:
- `activities`: Lista de atividades registradas.

#### **Métodos**:
- `add_activity()`: Adiciona uma atividade ao sistema.
- `list_activities()`: Lista todas as atividades registradas.
- `find_activities_by_contact(cpf)`: Busca atividades associadas a um CPF.

---