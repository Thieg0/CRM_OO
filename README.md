# CRM Tool - Sistema de Gerenciamento de Relacionamento com o Cliente

## 📋 Descrição
Sistema CRM desenvolvido em Python, oferecendo funcionalidades completas para gerenciamento de clientes, vendas, atividades e documentos.

## 🚀 Funcionalidades Implementadas
1. Contact Management
2. Sales Pipeline Management
3. Activity Tracking
4. Task and Appointment Scheduling
5. Email Integration and Campaign Management
6. Lead Generation and Tracking
7. Customizable Dashboards
8. Reporting and Analytics
9. Document Storage and Management

## 🏗️ Estrutura de Classes

### 📌 `Contact` e `ContactManager`
**Gerenciamento de Contatos**
- `Contact`: Representa um contato no sistema
  - Atributos: cpf, name, phone, email
  - Métodos: update_contact()

- `ContactManager`: Gerencia os contatos
  - Atributos: contacts (dicionário)
  - Métodos: add_contact(), list_contacts(), search_contact(), remove_contact(), update_contact()

### 📌 `SalesOpportunity` e `SalesPipeline`
**Gerenciamento de Vendas**
- `SalesOpportunity`: Representa uma oportunidade de venda
  - Atributos: id, contact, value, stage
  - Métodos: update_stage()

- `SalesPipeline`: Gerencia oportunidades de vendas
  - Métodos: add_opportunity(), list_opportunities(), update_opportunity_stage(), remove_opportunity()

### 📌 `Activity` e `ActivityTracker`
**Rastreamento de Atividades**
- `Activity`: Representa uma atividade com cliente
  - Atributos: cpf, activity_type, description, timestamp

- `ActivityTracker`: Gerencia atividades
  - Métodos: add_activity(), list_activities(), find_activities_by_contact()

### 📌 `Appointment` e `TaskScheduler`
**Agendamento de Compromissos**
- `Appointment`: Representa um compromisso
  - Atributos: contact, title, date_time, description, status

- `TaskScheduler`: Gerencia compromissos
  - Métodos: add_appointment(), list_appointments(), update_appointment_status()

### 📌 `EmailTemplate` e `CampaignManager`
**Gestão de Campanhas de Email**
- `EmailTemplate`: Modelo de email
  - Atributos: name, subject, content, variables

- `CampaignManager`: Gerencia campanhas
  - Métodos: create_campaign(), schedule_campaign(), list_campaigns()

### 📌 `Lead` e `LeadManager`
**Gestão de Leads**
- `Lead`: Representa um lead potencial
  - Atributos: name, email, phone, source, status, score

- `LeadManager`: Gerencia leads
  - Métodos: add_lead(), update_status(), add_note(), view_details()

### 📌 `Dashboard` e `DashboardManager`
**Painéis Personalizáveis**
- `DashboardWidget`: Componente do dashboard
  - Atributos: title, widget_type, data_source

- `DashboardManager`: Gerencia dashboards
  - Métodos: create_dashboard(), customize_dashboard(), view_dashboard()

### 📌 `Report` e `AnalyticsManager`
**Relatórios e Análises**
- `Report`: Representa um relatório
  - Atributos: title, report_type, data

- `AnalyticsManager`: Gerencia relatórios
  - Métodos: generate_sales_report(), generate_lead_report(), view_report()

### 📌 `Document` e `DocumentManager`
**Gestão de Documentos**
- `Document`: Representa um documento
  - Atributos: name, category, content, version

- `DocumentManager`: Gerencia documentos
  - Métodos: upload_document(), search_documents(), update_document()

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Programação Orientada a Objetos
- Estruturas de Dados (Dicionários, Listas)
- Manipulação de Datas e Arquivos