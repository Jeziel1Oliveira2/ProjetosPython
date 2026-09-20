# 🐍 Portfólio de Projetos em Python

Bem-vindo ao meu repositório dedicado ao desenvolvimento em Python. Este espaço foi criado para centralizar, documentar e versionar os projetos que construo, refletindo minha evolução contínua na linguagem e a aplicação prática de boas práticas de Engenharia de Software.

Meu objetivo aqui é ir além da sintaxe básica, desenvolvendo soluções estruturadas que demonstrem domínio em lógica de programação, manipulação de dados e arquitetura de código — competências essenciais para a atuação como desenvolvedor Full Stack.

---

## 🚀 Projetos em Destaque

### 1. Sistema de Gerenciamento de Contatos (CLI)
Uma aplicação de linha de comando (CLI) desenvolvida com foco em Orientação a Objetos (POO), validação rigorosa de dados e manipulação de arquivos.

* **Descrição:** Gerenciador de contatos completo que opera via terminal. Garante que dados inválidos não entrem no sistema aplicando regras de negócio diretamente na construção dos objetos. Consome a biblioteca `phonenumbers` para validar números de telefone (padrão BR) e utiliza serialização em JSON para manter os dados salvos entre sessões.
* **Principais Funcionalidades e Conceitos Aplicados:**
  * **POO:** Divisão de responsabilidades entre `Contato` (modelo/validação) e `GerenciadorContatos` (persistência e listagem)
  * **Validação de Dados:** Formatação automática para Title Case, bloqueio de números em nomes, verificação de e-mail e validação de telefones via biblioteca externa
  * **Tratamento de Exceções:** `try/except` e `raise ValueError` para capturar erros sem quebrar a aplicação
  * **Persistência em JSON:** Salvamento e carregamento automático com tratamento de `FileNotFoundError`
* **Bibliotecas:** `json` (nativa) e `phonenumbers` (externa)
* **Status:** Concluído ✔️

---

### 2. Banco de Dados de Filmes (CLI)
Uma aplicação de linha de comando para gerenciar uma biblioteca de filmes, utilizando banco de dados relacional SQLite.

* **Descrição:** Sistema completo para cadastrar, listar, buscar e deletar filmes via terminal. Utiliza SQLite como banco de dados relacional, garantindo persistência dos dados e consultas eficientes com SQL.
* **Principais Funcionalidades e Conceitos Aplicados:**
  * **POO:** Divisão de responsabilidades entre `Film` (modelo) e `FilmsManager` (operações no banco)
  * **Banco de Dados Relacional:** Criação de tabelas, inserção, consulta e remoção de dados com SQL
  * **Múltiplas Buscas:** Por gênero, ano de lançamento e título do filme
  * **match/case:** Uso do switch moderno do Python 3.10+ para o menu interativo
* **Bibliotecas:** `sqlite3` (nativa)
* **Status:** Concluído ✔️

---

*(Novos projetos serão adicionados continuamente conforme o avanço dos estudos...)*

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.x
* **Armazenamento:** JSON para persistência leve e SQLite para banco de dados relacional
* **Versionamento:** Git e GitHub
* **Práticas Adotadas:** Clean Code, modularização e lógica estruturada

---

## ⚙️ Como Executar os Projetos Localmente

1. **Clone o repositório:**
```bash
   git clone https://github.com/Jeziel1Oliveira2/ProjetosPython.git
```
2. **Entre na pasta do projeto:**
```bash
   cd ProjetosPython
```

3. **Instale as dependências:**
```bash
   pip install -r requirements.txt
```

4. **Execute o projeto desejado:**
```bash
   python nome_do_arquivo.py
```

---

## 📁 Estrutura do Repositório

```
ProjetosPython/
├── SistemaConta/
│   └── gerenciador.py
├── BancodeFilmes/
│   └── filmes.py
└── README.md
```