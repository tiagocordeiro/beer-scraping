import csv

import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.tabeladacerveja.com.br/')
soup = BeautifulSoup(page.content, 'html.parser')
colunas = soup.find_all("div", {"class": "span-1"})

file = csv.writer(open("beers.csv", "w"))
# Write column headers as the first line
file.writerow(["Style", "Name", "Info",
               "Exemplos", "ABV", "IBU", "SRM", "Gravidade Inicianl",
               "Gravidade Final"])

for coluna in colunas:
    type_title = coluna.find("h3", {"class": "type-title"})
    if type_title:
        type_title_clean = type_title.text.replace("  ", "").replace('\n', '')
        print('Tipo: ', type_title_clean)

        beers = coluna.find_all("div", {"class": "element"})
        for beer in beers:
            beer_details = beer.find("div", {"class": "beerName"})
            if beer_details:
                beer_info = beer.find("div", {"class": "beerInfo"})
                beer_example = beer.find("div", {"class", "beerExample"})
                beer_name_clean = beer_details.text.replace("  ", "").replace('\n', '')
                beer_info_clean = beer_info.text.replace("  ", "").replace('\n', '')
                beer_example_clean = beer_example.text
                top = beer.find("div", {"class": "top"})
                top_right = top.find("div", {"class": "right"})
                bottom = beer.find("div", {"class", "bottom"})
                bottom_left = bottom.find("div", {"class", "left"})
                bottom_right = bottom.find("div", {"class": "right"})
                gravidade_inicial = top_right.find_all("div")[0].text
                gravidade_final = top_right.find_all("div")[1].text
                abv = bottom_left.find_all("div")[0].text
                ibu = bottom_left.find_all("div")[1].text
                srm = bottom_right.find_all("div")[1].text

                print("Nome: ", beer_name_clean)
                print("Info: ", beer_info_clean)
                print("Exemplos: ", beer_example_clean)
                print("ABV: ", abv)
                print("IBU: ", ibu)
                print("SRM: ", srm)
                print("Gravidade Inicial: ", gravidade_inicial)
                print("Gravidade Final: ", gravidade_final)
                print("-" * 77)

                file.writerow((type_title_clean,
                               beer_name_clean,
                               beer_info_clean,
                               beer_example_clean,
                               abv, ibu, srm,
                               gravidade_inicial,
                               gravidade_final))

        print("/" * 77)

hibridos = soup.find_all("div", {"class": "span-6"})
for elemento in hibridos:
    beers = elemento.find_all("div", "element")
    for beer in beers:
        beer_details = beer.find("div", {"class": "beerName"})
        if beer_details:
            beer_info = beer.find("div", {"class": "beerInfo"})
            beer_example = beer.find("div", {"class", "beerExample"})
            beer_name_clean = beer_details.text.replace("  ", "").replace('\n', '')
            beer_info_clean = beer_info.text.replace("  ", "").replace('\n', '')
            beer_example_clean = beer_example.text
            top = beer.find("div", {"class": "top"})
            top_right = top.find("div", {"class": "right"})
            bottom = beer.find("div", {"class", "bottom"})
            bottom_left = bottom.find("div", {"class", "left"})
            bottom_right = bottom.find("div", {"class": "right"})
            gravidade_inicial = top_right.find_all("div")[0].text
            gravidade_final = top_right.find_all("div")[1].text
            abv = bottom_left.find_all("div")[0].text
            ibu = bottom_left.find_all("div")[1].text
            srm = bottom_right.find_all("div")[1].text

            print("Tipo: ", "ESTILOS HÍBRIDOS")
            print("Nome: ", beer_name_clean)
            print("Info: ", beer_info_clean)
            print("Exemplos: ", beer_example_clean)
            print("ABV: ", abv)
            print("IBU: ", ibu)
            print("SRM: ", srm)
            print("Gravidade Inicial: ", gravidade_inicial)
            print("Gravidade Final: ", gravidade_final)
            print("-" * 77)

            file.writerow(("ESTILOS HÍBRIDOS",
                           beer_name_clean,
                           beer_info_clean,
                           beer_example_clean,
                           abv, ibu, srm,
                           gravidade_inicial,
                           gravidade_final))
