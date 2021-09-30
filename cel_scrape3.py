from bs4 import BeautifulSoup as bs
import requests

cel_page = requests.get('https://www.tudocelular.com/Motorola/precos/n6123/Motorola-Moto-G8-Power.html')
cel_page = cel_page.text

cel_soup = bs(cel_page, 'lxml')

#Celular

cel_nome = cel_soup.find('h2', attrs={'class','schedatitle'})
cel_nome = cel_nome.text
cel_nome = cel_nome.replace('Preço','')

#Descrição do celular

cel_desc = cel_soup.find('div', attrs={'modeldesc'})
cel_desc = cel_desc.text

#Top3 preços

parte_preco = cel_soup.find('div', attrs={'id' : 'table1'})
parte_preco = parte_preco.find_all('div')

lista_prices = []

for n in range(0,2):
     for div in parte_preco:
          try:
               div = div.find('div', attrs={'class': 'price'})
               lista_prices.append(div.text)
          except:
               pass

melhores_precos = ''' '''

top3 = lista_prices[1:4]
first_item = top3[0]


for oferta in top3:
     melhores_precos += oferta

melhores_precos = melhores_precos.replace('VER OFERTA', '')
melhores_precos = melhores_precos.replace('R$', ' reais')
melhores_precos = melhores_precos.replace('\n\n', '\n')

#Final

msg_final = f'''\t{cel_nome} 
➜ {cel_desc}
➜ Melhores Ofertas:{melhores_precos}'''

print(msg_final)

input('')
