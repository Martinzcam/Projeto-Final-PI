# Estude Mais — Plataforma de Cursos Online

Projeto desenvolvido como trabalho final da disciplina de Programação para Internet (PI), do curso de Informática.

A plataforma Estude Mais permite que usuários criem contas, explorem cursos disponíveis, realizem inscrições e acessem conteúdos organizados em módulos e aulas.

---

## 1. Objetivo do projeto

O objetivo do projeto é desenvolver uma plataforma de ensino online que permita a organização e disponibilização de cursos para estudantes.

O sistema oferece uma interface para que os usuários encontrem cursos, realizem inscrições e acompanhem os conteúdos disponibilizados.

Também possui uma área administrativa para gerenciar os cursos, módulos e aulas cadastrados.

---

## 2. Funcionalidades

### Autenticação de usuários

- Cadastro de novos usuários.
- Login utilizando nome de usuário e senha.
- Logout da conta.
- Validação dos dados dos formulários.
- Exibição de mensagens de sucesso e erro.

### Cursos

- Listagem dos cursos publicados.
- Visualização dos detalhes de cada curso.
- Gerenciamento dos cursos pelo Django Admin.

### Inscrições

- Inscrição de usuários em cursos.
- Registro automático da data da inscrição.
- Impedimento de inscrições duplicadas.
- Área pessoal para visualizar os cursos inscritos.

### Área de aprendizagem

- Visualização dos módulos de cada curso.
- Listagem das aulas de cada módulo.
- Organização dos conteúdos pela ordem cadastrada.
- Exibição do título e conteúdo textual das aulas.
- Acesso a vídeos por meio de URLs cadastradas.
- Navegação entre módulos e aulas.

### Controle de acesso

- Restrição das páginas de aprendizagem a usuários autenticados.
- Verificação da inscrição do usuário no curso.
- Proteção dos conteúdos contra acesso direto por URLs.
- Separação das inscrições de cada usuário.

### Interface

- Layout compartilhado entre as páginas.
- Identidade visual padronizada.
- Formulários e mensagens estilizados.
- Layout responsivo para computadores, tablets e celulares.
- Interface desenvolvida com HTML e CSS, sem necessidade de JavaScript.

---

## 3. Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem de programação principal |
| Django 5.2.18 | Framework web |
| SQLite 3 | Banco de dados |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e responsividade |
| Git | Controle de versão |
| GitHub | Hospedagem do código e colaboração |

### Dependências Python

As dependências e suas versões estão registradas no arquivo `requirements.txt`.

- Django 5.2.18
- asgiref 3.13.0
- sqlparse 0.6.0
- tzdata 2026.6

Para instalar todas as dependências, utilize:

```bash
pip install -r requirements.txt
```

---

## 4. Requisitos para execução

Antes de instalar o projeto, é necessário possuir:

- Python 3.10 ou superior, em uma versão compatível com Django 5.2.
- Git.
- Pip (gerenciador de pacotes do Python).
- Acesso à internet para baixar o repositório e instalar as dependências.

O projeto utiliza SQLite, portanto não é necessário instalar ou configurar um servidor de banco de dados separado para executá-lo localmente.

---

## 5. Instalação do projeto

### 5.1. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/Martinzcam/Projeto-Final-PI.git
```

Entre na pasta do projeto:

```bash
cd Projeto-Final-PI
```

### 5.2. Criar o ambiente virtual

O ambiente virtual mantém as dependências do projeto isoladas de outras aplicações Python.

No Windows:

```bash
python -m venv .venv
```

No Linux ou macOS:

```bash
python3 -m venv .venv
```

### 5.3. Ativar o ambiente virtual

No Windows, utilizando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Windows, utilizando o Prompt de Comando:

```cmd
.venv\Scripts\activate.bat
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Após a ativação, o nome do ambiente virtual deverá aparecer no início do terminal.

### 5.4. Atualizar o pip

Execute:

```bash
python -m pip install --upgrade pip
```

### 5.5. Instalar as dependências

Execute:

```bash
pip install -r requirements.txt
```

Esse comando instala as bibliotecas necessárias para executar o projeto.

---

## 6. Configuração do banco de dados

O projeto utiliza SQLite 3 como banco de dados.

A configuração está localizada em:

```text
config/settings.py
```

O banco está configurado utilizando o mecanismo:

```python
'ENGINE': 'django.db.backends.sqlite3'
```

O arquivo do banco de dados é:

```text
db.sqlite3
```

Ele fica localizado na pasta principal do projeto.

Não é necessário criar o banco manualmente. O Django cria o arquivo e as tabelas necessárias durante a aplicação das migrações.

### 6.1. Aplicar as migrações

Com o ambiente virtual ativado, execute:

```bash
python manage.py migrate
```

Esse comando cria as tabelas necessárias no banco de dados.

### 6.2. Criar novas migrações

Quando houver alterações nos modelos do projeto, utilize:

```bash
python manage.py makemigrations
```

Depois aplique as alterações:

```bash
python manage.py migrate
```

**Observação:** ao clonar o projeto, as migrações existentes já estão versionadas no repositório. Por isso, normalmente basta executar `python manage.py migrate`.

---

## 7. Criar um usuário administrador

Para acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

O terminal solicitará:

- Nome de usuário.
- E-mail.
- Senha.
- Confirmação da senha.

Após a criação, será possível acessar o painel administrativo.

Endereço:

```text
http://127.0.0.1:8000/admin/
```

Por meio do painel administrativo, é possível gerenciar os cursos, módulos, aulas e inscrições.

---

## 8. Executar o projeto

Após instalar as dependências e aplicar as migrações, execute:

```bash
python manage.py runserver
```

O servidor de desenvolvimento será iniciado.

Acesse a plataforma pelo navegador:

```text
http://127.0.0.1:8000/
```

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

---

## 9. Principais endereços do sistema

| Página | Endereço |
|---|---|
| Página inicial | `/` |
| Cadastro | `/accounts/cadastro/` |
| Login | `/accounts/login/` |
| Logout | `/accounts/logout/` |
| Catálogo de cursos | `/cursos/catalogo/` |
| Detalhes do curso | `/cursos/detalhes/<curso_id>/` |
| Meus cursos | `/cursos/meus-cursos/` |
| Área de aprendizagem | `/cursos/aprender/<curso_id>/` |
| Detalhes do módulo | `/cursos/modulo/<modulo_id>/` |
| Detalhes da aula | `/cursos/aula/<aula_id>/` |
| Painel administrativo | `/admin/` |

**Observações:**

- Os endereços de aprendizagem exigem autenticação e inscrição no curso correspondente.
- O logout é realizado por formulário POST, por meio do botão disponível na navegação.
- Os identificadores (`<curso_id>`, `<modulo_id>` e `<aula_id>`) são substituídos pelos IDs dos registros cadastrados.

---

## 10. Executar os testes

O projeto possui testes automatizados para verificar suas principais funcionalidades.

Para executar todos os testes, utilize:

```bash
python manage.py test
```

Para verificar a configuração do projeto:

```bash
python manage.py check
```

O resultado esperado dos testes é:

```text
Ran XX tests

OK
```

O número de testes pode variar conforme novas funcionalidades forem implementadas.

---

## 11. Estrutura do projeto

```text
Projeto-Final-PI/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── cursos/
│   ├── migrations/
│   ├── templates/
│   │   └── cursos/
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── test_fluxos.py
│   ├── urls.py
│   └── views.py
│
├── docs/
│   ├── issue-3-arquitetura.md
│   └── issue-4-template-base.md
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   └── base.html
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

### Responsabilidade dos aplicativos

**accounts:** responsável pelas funcionalidades relacionadas aos usuários, incluindo cadastro, login, logout e autenticação.

**cursos:** responsável pelo gerenciamento de cursos, módulos, aulas e inscrições, além da área de aprendizagem.

**config:** contém as configurações gerais do projeto Django e as URLs principais.

**templates:** contém o template base compartilhado pelas páginas.

**static:** contém os arquivos estáticos, incluindo o CSS da plataforma.

**docs:** reúne diagramas e documentos técnicos do projeto.

---

## 12. Documentação e diagramas

Os seguintes documentos complementam a documentação do projeto:

- [Diagrama de arquitetura e configuração inicial — Issue #3](docs/issue-3-arquitetura.md).
- [Diagrama do template base e estrutura visual — Issue #4](docs/issue-4-template-base.md).

As issues originais também podem ser consultadas:

- [Issue #3 — Configurar o projeto Django e criar os aplicativos](https://github.com/Martinzcam/Projeto-Final-PI/issues/3).
- [Issue #4 — Criar o template base e a estrutura visual do site](https://github.com/Martinzcam/Projeto-Final-PI/issues/4).

---

## 13. Organização do projeto

**Repositório GitHub:**

[Projeto-Final-PI](https://github.com/Martinzcam/Projeto-Final-PI)

**GitHub Project:**

[Projeto-Final-PI-Kanban](https://github.com/users/Martinzcam/projects/5)

O GitHub Project é utilizado para organizar as tarefas, acompanhar as issues e monitorar o andamento do desenvolvimento.

---

## 14. Observações importantes

- O banco de dados SQLite é criado localmente e não precisa ser enviado ao GitHub.
- O arquivo `db.sqlite3` está incluído nas regras de exclusão do Git.
- As dependências devem ser instaladas por meio do `requirements.txt`.
- As migrações devem ser aplicadas antes de iniciar a aplicação.
- A configuração atual do Django é destinada ao desenvolvimento local. Antes de publicar o sistema em produção, é necessário revisar configurações de segurança, como `DEBUG`, `SECRET_KEY` e `ALLOWED_HOSTS`.

---

## 15. Equipe

Projeto desenvolvido em equipe como atividade final da disciplina de Programação para Internet.