Feature: Test Store

  Scenario: Criar usuario
    Given que acesso o site Automation Test Store
    When acesso a pagina de login
    When escolho criar uma nova conta
    When preencho os dados obrigatorios do cadastro
    When aceito os termos
    When confirmo a criacao da conta
    Then devo visualizar a mensagem "YOUR ACCOUNT HAS BEEN CREATED!"

  Scenario: Login positivo
    Given que acesso o site Automation Test Store
    When acesso a pagina de login
    When informo usuario e senha validos
    When clico no botao login
    Then devo visualizar a area "MY ACCOUNT"
    When realizo logout
    Then devo visualizar a mensagem "ACCOUNT LOGOUT"

  Scenario: Login negativo
    Given que acesso o site Automation Test Store
    When acesso a pagina de login
    When informo usuario e senha invalidos
    When clico no botao de login
    Then devo visualizar a mensagem de erro "Error: Incorrect login or password provided."

  Scenario: Fluxo de compra
    Given que acesso o site Automation Test Store
    When acesso a pagina de login
    When informo usuario e senha validos
    When clico no botao login
    Then devo visualizar a area "MY ACCOUNT"
    When acesso a categoria de roupas 
    When escolho um produto
    When adiciono o produto ao carrinho
    Then devo visualizar a pagina "SHOPPING CART"
    When removo o produto do carrinho
    When realizo logout
    Then devo visualizar a mensagem "ACCOUNT LOGOUT"
