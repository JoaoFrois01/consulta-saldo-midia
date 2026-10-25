import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

# Carregamento de configurações via variáveis de ambiente
raw_midias = os.getenv("MIDIAS", "21")
midias = [m.strip() for m in raw_midias.split(",") if m.strip()]


def ConsultaSaldo():
    username = os.getenv("ORGANIZE_USERNAME")
    password = os.getenv("ORGANIZE_PASSWORD")
    base_url = os.getenv(
        "ORGANIZE_BASE_URL",
        "https://organize.grupoorgafarma.com.br/midias/consumptions",
    )

    if not username or not password:
        raise ValueError(
            "Credenciais não configuradas. Verifique as variáveis ORGANIZE_USERNAME e ORGANIZE_PASSWORD no arquivo .env."
        )

    midias_saldo = []

    with sync_playwright() as p:
        # 1.1. Inicia o navegador e a página
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 2. Iteração sobre todas as mídias
        for i, row in enumerate(midias):
            cod_midia = row
            page.goto(base_url)

            # O login só será executado na primeira iteração
            if i == 0:
                page.wait_for_selector("#username")
                page.fill("#username", username)
                page.fill("#password", password)
                page.get_by_role("button", name="ENTRAR").click(no_wait_after=True)
                page.wait_for_timeout(5000)  # Espera 5 segundos para garantir que a página carregou após o login
            try:
                page.goto(f"{base_url}/{cod_midia}")
                page.wait_for_timeout(5000)  # Espera 5 segundos para garantir que a página carregou após o redirecionamento
                saldo_midia = (
                    page.locator("div.col-md-6 h5:has-text('Saldo:')")
                    .inner_text()
                    .replace("Saldo: ", "")
                    .strip()
                )
                midias_saldo.append((cod_midia, saldo_midia))
            except Exception as e:
                midias_saldo.append((cod_midia, "Erro ao capturar saldo"))

        browser.close()

    resultado = ""
    for i in midias_saldo:
        resultado += f"Midia: {i[0]} | Saldo: {i[1]}\n"
    print(resultado)
    return resultado
