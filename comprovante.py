import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Firefox()
driver.get("https://qacademico.ifpe.edu.br/qacademico/alunos/")
assert "Q-Acadêmico Web para IFPE - Bem Vindo!" in driver.title
login = driver.find_element(By.CSS_SELECTOR, '#txtLogin')
login.clear()
login.send_keys(os.getenv('MATRICULA'))
senha = driver.find_element(By.CSS_SELECTOR,'#txtSenha')
senha.clear()
senha.send_keys(os.getenv('SENHA'))
time.sleep(2)
enviar = driver.find_element(By.CSS_SELECTOR, '#btnOk').click()
time.sleep(5)
driver.get('https://qacademico.ifpe.edu.br/webapp/documentos')
time.sleep(4)
solicitar = driver.find_element(By.CSS_SELECTOR,'button.button-acao:nth-child(2)').click()
time.sleep(4)
tipo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/documentos.aluno.nova-solicitacao-component/div/div[2]/div[1]/div[1]/select').click()
tipo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/documentos.aluno.nova-solicitacao-component/div/div[2]/div[1]/div[1]/select/option[2]').click()
time.sleep(4)
semestre = Select(driver.find_element(By.CSS_SELECTOR, '.ng-pristine'))
semestre.select_by_visible_text('2023/1')
time.sleep(4)
enviar = driver.find_element(By.CSS_SELECTOR,'.button-primary').click()