import os
import datetime as dt
import win32com.client as win32
from dotenv import load_dotenv
from consulta_saldo import ConsultaSaldo

load_dotenv()


def Enviar_Email():
    saldos_midias = ConsultaSaldo()  # Chama a função ConsultaSaldo para obter os saldos das mídias

    hoje = dt.datetime.now().strftime("%d/%m")  # Obtém a data atual no formato dd/mm

    # Inicializa a aplicação do Outlook
    outlook = win32.Dispatch("outlook.application")
    email = outlook.CreateItem(0)

    # Configuração dos destinatários e assunto
    email_to = os.getenv("EMAIL_TO", "joao.frois@orgafarma.com.br")
    email_cc = os.getenv("EMAIL_CC")

    email.To = email_to
    if email_cc:
        email.CC = email_cc

    email.Subject = f"Relatório Diário - Conferência de Saldos - Mídias {hoje}"

    # Corpo do e-mail (suporta formatação em HTML)
    email.HTMLBody = f"""
    <p>Bom dia,</p>
    <p>A conferência de saldos das mídias foi concluída com sucesso!</p>
    <p>Segue abaixo a relação de mídia | saldo:</p>
    <pre>{saldos_midias}</pre>
    <br>
    <p>Atenciosamente,<br><b>Assistente de Conferência - Saldos das Mídias</b></p>
    """

    # Envia o e-mail
    email.Send()
    print("E-mail enviado com sucesso via Outlook!")


if __name__ == "__main__":
    Enviar_Email()
