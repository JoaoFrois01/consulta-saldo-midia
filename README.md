# Consulta de Saldo de Mídias e Relatório Diário

Automação em Python desenvolvida para consultar saldos de consumo de mídias no portal Organize e enviar automaticamente um relatório diário por e-mail através do Microsoft Outlook.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/)**
- **[Playwright](https://playwright.dev/python/)**: Automação web (Web Scraping) para autenticação e extração dos saldos das mídias.
- **[pywin32](https://github.com/mhammond/pywin32)**: Integração com a API COM do Microsoft Outlook local para envio dos relatórios.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)**: Gerenciamento seguro de variáveis de ambiente e credenciais sensíveis.

---

## 📁 Estrutura do Projeto

```text
projetinho - consulta saldo mídia/
├── .env                  # Variáveis de ambiente e credenciais reais (ignorado no git)
├── .env.example          # Modelo de configuração para referência
├── .gitignore            # Arquivos e diretórios ignorados pelo controle de versão
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
├── main.py               # Ponto de entrada da aplicação
├── consulta_saldo.py     # Módulo responsável pela raspagem de saldos no Organize
└── montar_email.py       # Módulo para formatação e envio do e-mail via Outlook
```

---

## 🚀 Instalação e Configuração

### 1. Pré-requisitos

- **Python 3.10+** instalado.
- **Microsoft Outlook** instalado e logado na máquina local (necessário para o envio dos e-mails via `win32com`).

### 2. Clonar o Repositório e Criar o Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Ou no Prompt de Comando (CMD)
.\venv\Scripts\activate.bat
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configurar as Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env` (se ainda não existir):

```bash
copy .env.example .env
```

Edite o arquivo `.env` preenchendo as seguintes variáveis:

```env
# Credenciais do sistema Organize
ORGANIZE_USERNAME=seu_usuario
ORGANIZE_PASSWORD=sua_senha
ORGANIZE_BASE_URL=https://organize.grupoorgafarma.com.br/midias/consumptions

# Lista de IDs das mídias a consultar (separadas por vírgula)
MIDIAS=21

# Destinatários do relatório
EMAIL_TO=joao.frois@orgafarma.com.br
EMAIL_CC=giovanni.reis@orgafarma.com.br
```

> [!IMPORTANT]
> O arquivo `.env` contém credenciais e jamais deve ser versionado no Git. Ele já está devidamente listado no `.gitignore`.

---

## ▶️ Como Executar

Com o ambiente virtual ativado e o arquivo `.env` configurado, execute:

```bash
python main.py
```

O script irá:
1. Abrir o navegador e autenticar no portal Organize.
2. Acessar cada mídia configurada na variável `MIDIAS` e extrair o saldo atual.
3. Formatar o relatório diário com a data do dia.
4. Abrir a instância do Outlook e disparar o e-mail para os destinatários configurados.
