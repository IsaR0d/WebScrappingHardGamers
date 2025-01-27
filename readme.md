# HardGamers Web Scraper

Este programa de Python realiza web scraping en la página de tecnología "HardGamers". Permite filtrar productos por palabras clave y ordena la lista de productos según sus precios de menor a mayor.

# Requisitos

- Python 3.x
- Librerías necesarias (pueden instalarse usando `pip`):
  - `requests`
  - `PyQt5`

# Instalación

1. Clona este repositorio en tu máquina local:
    bash
    git clone https://github.com/IsauroRod/WebScrappingHardGamers
    cd WEBSCRAPPING
    

2. Instala las dependencias requeridas:

# Uso

1. Ejecuta el script principal:
    bash
    python main.py
    

2. En la interfaz gráfica, ingresa una palabra clave para filtrar los productos y haz clic en "Buscar".

3. El programa realizará el web scraping en la página de "HardGamers", filtrará los productos según la palabra clave ingresada y ordenará la lista de productos de menor a mayor precio. Los resultados se mostrarán en una tabla.

# Estructura del Proyecto

- `main.py`: El script principal que ejecuta la interfaz gráfica y controla la lógica del programa.
- `controler.py`: Contiene las funciones para realizar el web scraping y el filtrado de productos.
- `scrapping.ui`: Archivo de diseño de la interfaz gráfica.
