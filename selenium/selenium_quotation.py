# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decimal import Decimal
from random import random, randint
import time


def gen_decimal(max_digits=5, decimal_places=2, min_value=0, max_value=9):
    num_as_str = lambda x: ''.join(
        [str(randint(min_value, max_value)) for i in range(x)])
    return Decimal("%s.%s" % (num_as_str(max_digits - decimal_places), num_as_str(decimal_places)))
gen_decimal.required = ['max_digits', 'decimal_places']


customer = webdriver.Firefox()
customer.get('http://localhost:8000/quotations/')
time.sleep(0.5)

stores = [
    'Compre Aqui',
    'Sorriso',
    'Sol',
    'Carrinho Cheio',
    'Registro'
]

products = [
    ['arroz 5 Kg', 4, 1, 4],
    ['feijão 1 Kg', 4, 1, 3],
    ['milho 500 g', 3, 1, 9],
    ['amendoim 500 g', 3, 1, 9],
    ['grão de bico 500 g', 3, 1, 9],
    ['água mineral 1.5 l', 3, 1, 9],
    ['refrigerante 1.5 l', 3, 1, 9],
    ['refrigerante 350 ml', 3, 1, 9],
    ['cerveja 350 ml', 3, 1, 9],
    ['suco integral 1 l', 3, 1, 9],
    ['creme dental 1 unid', 3, 1, 9],
    ['sabonete 1 pcte', 3, 1, 9],
    ['shampoo 350 ml', 3, 1, 9],
    ['absorvente 1 pcte', 3, 1, 9],
    ['fralda M 1 pcte', 4, 1, 4],
    ['sabão em pó 1 Kg', 4, 1, 4],
    ['sabão em barra 100 g', 3, 1, 9],
    ['detergente 500 ml', 3, 1, 9],
    ['desinfetante 1 l', 3, 1, 9],
    ['água sanitária 1 l', 3, 1, 9],
    ['leite 1 l', 3, 1, 9],
    ['pão integral 1 pcte', 3, 1, 9],
    ['queijo mussarela 500 g', 3, 1, 9],
    ['café em pó 1 Kg', 3, 1, 9],
    ['chocolate em pó 500 g', 3, 1, 9],
]

for s in stores:
    for i in products:
        button = customer.find_element_by_id('quotation_add')
        button.click()
        time.sleep(0.5)

        search = customer.find_element_by_id('id_product')
        search.send_keys(i[0])

        search = customer.find_element_by_id('id_store')
        search.send_keys(s)

        search = customer.find_element_by_id('id_price')
        search.send_keys(gen_decimal(i[1], 2, i[2], i[3]))

        search = customer.find_element_by_id('id_quantity')
        search.send_keys(randint(1, 9))

        button = customer.find_element_by_id('id_submit')
        button.click()
