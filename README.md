# 🐍 Portfólio de Projetos em Python

Bem-vindo ao meu repositório dedicado ao desenvolvimento em Python. Este espaço foi criado para centralizar, documentar e versionar os projetos que construo, refletindo minha evolução contínua na linguagem e a aplicação prática de boas práticas de Engenharia de Software.

Meu objetivo aqui é ir além da sintaxe básica, desenvolvendo soluções estruturadas que demonstrem domínio em lógica de programação, manipulação de dados e arquitetura de código — competências essenciais para a atuação como desenvolvedor Full Stack.

---

## 🚀 Projetos em Destaque

### 1. Sistema de Gerenciamento de Contatos (CLI)
Uma aplicação de linha de comando (CLI) desenvolvida com foco em Orientação a Objetos (POO), validação rigorosa de dados e manipulação de arquivos.

* **Descrição:** Este projeto é um gerenciador de contatos completo que opera via terminal. Ele garante que dados "sujos" não entrem no sistema aplicando regras de negócio diretamente na construção dos objetos. A aplicação consome a biblioteca `phonenumbers` para garantir que apenas números de telefone válidos (padrão BR) sejam aceitos e utiliza serialização em JSON para manter os dados salvos entre as sessões.
* **Principais Funcionalidades e Conceitos Aplicados:**
  * **Programação Orientada a Objetos (POO):** Divisão de responsabilidades entre as classes `Contato` (modelo/validação) e `GerenciadorContatos` (lógica de persistência e listagem).
  * **Validação de Dados e Regras de Negócio:** Tratamento de strings (formatação automática para Title Case), bloqueio de números em nomes, verificação de sintaxe de e-mail e validação real de telefones via API/biblioteca externa.
  * **Tratamento de Exceções:** Uso de `try/except` e `raise ValueError` para capturar erros de input do usuário sem "quebrar" a aplicação.
  * **Persistência de Dados (JSON):** Salvamento e carregamento automático do arquivo `contatos.json` utilizando a biblioteca nativa `json`, incluindo tratamento para a ausência do arquivo na primeira execução (`FileNotFoundError`).
* **Bibliotecas Utilizadas:** `json` (nativa) e `phonenumbers` (externa).
* **Status:** Concluído ✔️

*(Novos projetos serão adicionados continuamente conforme o avanço dos estudos e desenvolvimentos...)*

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.x
* **Armazenamento:** JSON para persistência leve de dados
* **Versionamento:** Git e GitHub
* **Práticas Adotadas:** Clean Code, modularização e lógica estruturada

---

## ⚙️ Como Executar os Projetos localmente

Para testar os projetos deste repositório na sua máquina, siga os passos abaixo:

1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
