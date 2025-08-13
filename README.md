# Bot Supabase + Z-API

Script em Python que busca contatos no Supabase e envia mensagem personalizada pelo WhatsApp usando a Z-API.

🛠 Requisitos
- Python 3.8+
- Conta gratuita no [Supabase](https://supabase.com/)
- Conta gratuita na [Z-API](https://z-api.io/)
-------------------------------------------------------
📦 Instalação
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