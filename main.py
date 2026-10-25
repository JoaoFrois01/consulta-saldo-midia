from dotenv import load_dotenv
from montar_email import Enviar_Email

# Carrega variáveis de ambiente
load_dotenv()


def main():
    print("=== Iniciando conferência de saldos das mídias ===")
    Enviar_Email()


if __name__ == "__main__":
    main()
