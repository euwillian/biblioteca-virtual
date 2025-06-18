# 🧩 Projeto 1 — Sistema de Biblioteca Virtual

📚 **Objetivo do Projeto:**  
Sistema para gerenciar livros, empréstimos e usuários (alunos e administradores). Ideal para demonstrar domínio de funcionalidades CRUD, autenticação e relacionamento entre modelos no Django.

---

## ✅ Funcionalidades

- 📖 Cadastro de livros com: título, autor, ano, categoria  
- 👤 Cadastro de usuários com distinção entre **alunos** e **administradores**  
- 🔐 Autenticação com login e senha (Django padrão)  
- 🔄 Registro de empréstimos com data de devolução  
- 🔎 Filtragem por livros **disponíveis** ou **emprestados**

---

## 🛠 Tecnologias Utilizadas

- **Backend:** Django + SQLite  
- **Autenticação:** Django Auth  
- **Interface:** Django Admin + Django Templates  
- **Controle de versão:** Git

---

## 🧠 Aprendizados Demonstrados

- CRUD completo com autenticação integrada  
- Relacionamentos entre modelos: `Livro ↔ Empréstimo ↔ Usuário`  
- Organização de projeto Django com estrutura clara por apps  
- Criação de `README.md` para documentação do projeto

---

## 📁 Estrutura de Apps

- `app/` → configurações e urls principais  
- `livros/` → gerenciamento de livros  
- `usuarios/` → autenticação e gerenciamento de usuários  
- `emprestimos/` → controle de empréstimos

---

## 🚀 Como rodar o projeto

```bash
# Clone o repositório
git clone https://github.com/euwillian/biblioteca-virtual.git

# Acesse a pasta
cd seu-repo

# Crie um ambiente virtual e ative
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
