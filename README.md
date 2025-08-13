# Bot Supabase + Z-API

Script em Python que busca contatos no Supabase e envia mensagem personalizada pelo WhatsApp usando a Z-API.

## .env:
SUPABASE_URL=https://hgnirjusasdcfnbmpuww.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhnbmlyanVzYXNkY2ZuYm1wdXd3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUwMDk0MzQsImV4cCI6MjA3MDU4NTQzNH0.omT6JiGog1ZrcUUsotPtxWX3LRwfYvmJglVWKFqcoaE
ZAPI_INSTANCE_ID=3E59E6286616F1F54BC55AA063CFBDB5
ZAPI_TOKEN=6C0C338254A35FCC0590D23C

Requisitos
- Python 3.8+
- Conta gratuita no [Supabase](https://supabase.com/)
- Conta gratuita na [Z-API](https://z-api.io/)
-------------------------------------------------------
Instalação
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
pip install -r requirements.txt
--------------------------------------------------
Crie uma tabela contatos no Supabase com as colunas:
id (integer).
nome_contato (text).
numero_telefone (text).
Cadastre até 3 contatos com número no formato internacional.
Crie um arquivo .env.

Uso:
python main.py
Buscar 3 contatos no Supabase.


Enviar a mensagem "Olá {{nome_contato}}, tudo bem com você?" pelo WhatsApp via Z-API.