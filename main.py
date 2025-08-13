import os
import time  # Adicionado este import
from supabase import create_client, Client
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print(os.getenv("ZAPI_TOKEN"))

def verificar_status_zapi():
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/status"
    try:
        response = requests.get(url, timeout=10)
        status_data = response.json()
        print(f"Status atual: {status_data}")
        return status_data.get('connected', False)
    except Exception as e:
        print(f"Erro ao verificar status: {str(e)}")
        return False

def buscar_contatos(limit=3):
    try:
        response = supabase.table("contatos").select("*").limit(limit).execute()
        print(f"Contatos encontrados: {len(response.data)}")
        return response.data or []
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []

def enviar_mensagem(numero, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"  # Alterado para send-text
    mensagem = f"Olá {nome}, tudo bem com você?"
    
    print(f"Tentando enviar para {nome} ({numero})")
    
    try:
        resp = requests.post(url, json={
            "phone": numero,
            "message": mensagem,
            "isGroup": False
        }, timeout=30)
        resp.raise_for_status()
        print(f"Mensagem enviada para {nome} ({numero})")
    except Exception as e:
        print(f"Erro ao enviar para {nome} ({numero}): {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"Resposta da API: {e.response.text}")

def forcar_reconexao_zapi():
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/restart"
    try:
        print("Tentando forçar reconexão...")
        response = requests.post(url, timeout=30)
        print(f"Resposta da reconexão: {response.status_code}")
        if response.status_code == 200:
            print("Reconexão solicitada - aguarde 30 segundos")
            time.sleep(30)
            return True
        return False
    except Exception as e:
        print(f"Erro ao forçar reconexão: {str(e)}")
        return False

def main():
    print("Iniciando script...")
    
    # Verificação inicial
    if not verificar_status_zapi():
        print("Instância desconectada - tentando reconectar...")
        if not forcar_reconexao_zapi():
            print("Falha ao reconectar - verifique manualmente no painel")
            return
    
    # Segunda verificação
    if not verificar_status_zapi():
        print("Instância permanece desconectada após tentativa de reconexão")
        return
    
    print("Conexão verificada com sucesso")
    
    # Busca e envio
    contatos = buscar_contatos()
    if not contatos:
        print("Nenhum contato encontrado")
        return
    
    print(f"Enviando mensagens para {len(contatos)} contatos...")
    for contato in contatos:
        enviar_mensagem(contato["numero_telefone"], contato["nome_contato"])

    print("Processo concluído")

if __name__ == "__main__":
    main()