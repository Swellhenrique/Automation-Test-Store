from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from datetime import datetime


@given("que acesso o site Automation Test Store")
def step_acessar_site(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)
    context.driver.get("https://automationteststore.com/")
    context.driver.set_window_size(1936, 1048)


@when("acesso a pagina de login")
def step_acessar_pagina_login(context):
    context.driver.find_element(By.LINK_TEXT, "Login or register").click()


@when("escolho criar uma nova conta")
def step_escolher_criar_conta(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()


@when("preencho os dados obrigatorios do cadastro")
def step_preencher_cadastro(context):
    codigo = datetime.now().strftime("%d%m%Y%H%M%S")

    context.driver.find_element(By.ID, "AccountFrm_firstname").send_keys("Yago Victor")
    context.driver.find_element(By.ID, "AccountFrm_lastname").send_keys("da silva")
    context.driver.find_element(By.ID, "AccountFrm_email").send_keys(f"yago_victor{codigo}@gmail.com")
    context.driver.find_element(By.ID, "AccountFrm_telephone").send_keys("55(48)99926-7821")
    context.driver.find_element(By.ID, "AccountFrm_address_1").send_keys("Rua 1980")
    context.driver.find_element(By.ID, "AccountFrm_address_2").send_keys("371")
    context.driver.find_element(By.ID, "AccountFrm_city").send_keys("Balneario Camboriu")

    pais = context.driver.find_element(By.ID, "AccountFrm_country_id")
    pais.find_element(By.XPATH, "//option[. = 'Brazil']").click()

    context.driver.find_element(By.ID, "AccountFrm_postcode").send_keys("88330491")

    estado = context.driver.find_element(By.ID, "AccountFrm_zone_id")
    estado.find_element(By.XPATH, "//option[. = 'Santa Catarina']").click()

    context.driver.find_element(By.ID, "AccountFrm_loginname").send_keys(f"yagovictor{codigo}")
    context.driver.find_element(By.ID, "AccountFrm_password").send_keys("Yagovictor22#")
    context.driver.find_element(By.ID, "AccountFrm_confirm").send_keys("Yagovictor22#")


@when("aceito os termos")
def step_aceitar_termos(context):
    context.driver.find_element(By.ID, "AccountFrm_agree").click()


@when("confirmo a criacao da conta")
def step_confirmar_criacao(context):
    context.driver.find_element(By.CSS_SELECTOR, ".lock-on-click").click()


@when("informo usuario e senha validos")
def step_informar_login_valido(context):
    context.driver.find_element(By.ID, "loginFrm_loginname").send_keys("yagovictor22")
    context.driver.find_element(By.ID, "loginFrm_password").send_keys("Yagovictor22#")


@when("informo usuario e senha invalidos")
def step_informar_login_invalido(context):
    context.driver.find_element(By.ID, "loginFrm_loginname").send_keys("yagovictor27")
    context.driver.find_element(By.ID, "loginFrm_password").send_keys("Yagovictor27")


@when("clico no botao login")
def step_clicar_botao_login(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(7)").click()


@when("clico no botao de login")
def step_clicar_botao_de_login(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(7)").click()


@when("acesso a categoria de roupas")
def step_acessar_categoria_roupas(context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-pills > li:nth-child(2) > a").click()
    context.driver.find_element(By.LINK_TEXT, "T-shirts").click()


@when("escolho um produto")
def step_escolher_produto(context):
    context.driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(2) .fa").click()


@when("adiciono o produto ao carrinho")
def step_adicionar_produto_carrinho(context):
    context.driver.find_element(By.LINK_TEXT, "Add to Cart").click()


@when("removo o produto do carrinho")
def step_remover_produto_carrinho(context):
    context.driver.find_element(By.CSS_SELECTOR, ".fa-trash-o").click()


@when("realizo logout")
def step_realizar_logout(context):
    context.driver.get("https://automationteststore.com/index.php?rt=account/logout")


@then('devo visualizar a area "{mensagem}"')
def step_visualizar_area(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, ".maintext").text == mensagem


@then('devo visualizar a pagina "{mensagem}"')
def step_visualizar_pagina(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, ".maintext").text == mensagem


@then('devo visualizar a mensagem "{mensagem}"')
def step_visualizar_mensagem(context, mensagem):
    wait = WebDriverWait(context.driver, 10)

    if mensagem == "YOUR ACCOUNT HAS BEEN CREATED!":
        texto = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "h1.heading1 > span")
            )
        ).text
    else:
        texto = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, ".maintext")
            )
        ).text

    assert texto == mensagem
    context.driver.quit()


@then('devo visualizar a mensagem de erro "{mensagem}"')
def step_visualizar_mensagem_erro(context, mensagem):
    assert mensagem in context.driver.find_element(By.CSS_SELECTOR, ".alert").text
    context.driver.quit()
