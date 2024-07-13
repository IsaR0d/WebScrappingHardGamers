import re
import requests
import math

def buscarRes(palabra_clave, contenido, ProggresBar):
    resultado = []
    print(ProggresBar.value())
    actual = int(ProggresBar.value())
    restante = 100 - actual
    if palabra_clave == "":
        for i in range(len(contenido[0])):
            resultado.append({"nombre":contenido[0][i], "precio":contenido[1][i].replace(".",""), "tienda":contenido[2][i]})
            ProggresBar.setValue(actual+int((i/len(contenido[0]))*restante))
        resultado.sort(key=lambda x: int(x["precio"]), reverse=False)
        return resultado
    for i in range(len(contenido[0])):
        if re.search(palabra_clave, contenido[0][i].upper()):
            resultado.append({"nombre":contenido[0][i], "precio":contenido[1][i].replace(".",""), "tienda":contenido[2][i]})
        ProggresBar.setValue(actual+int((i/len(contenido[0]))*restante))
    resultado.sort(key=lambda x: int(x["precio"]), reverse=False)
    return resultado

def buscarContenido(ProggresBar):
    website = "https://www.hardgamers.com.ar/deals"
    response = requests.get(website)
    content = str(response.text)
    cantidad_contenido_patron = r'\b(\d+)\s+resultados\b'
    cantidad_contenido = re.findall(cantidad_contenido_patron, str(content))
    todos_nombres = []
    todos_precios = []
    todas_tiendas = []
    pages = math.ceil(int(cantidad_contenido[0]) / 21) + 1

    for i in range(1,pages):  # Ajustado para iterar desde página 1 hasta página 'pages'
        website = f"https://www.hardgamers.com.ar/deals?page={i}"

        response = requests.get(website)
        content = str(response.text)
        
        patron_nombre = r'(?<=<h3 itemprop="name" class="product-title line-clamp">).*?(?=</h3>)'
        nombre_producto = re.findall(patron_nombre, content)
        
        precio_producto_regex = r'<h2 itemprop="price" content="\d+" class="product-price">\s*([\d.,]+)\s*</h2>'
        precio_producto = re.findall(precio_producto_regex, content)
        
        tienda_regex = r'<h4 class="subtitle">\s*(.*?)\s*</h4>'
        tienda = re.findall(tienda_regex, content)
        tienda_modificada = [elemento.replace("&", "") for elemento in tienda]
        if i != pages-1:
            todos_nombres.extend(nombre_producto[:21])
            todos_precios.extend(precio_producto[:21])
            todas_tiendas.extend(tienda_modificada[:21])
        else:
            corte = int(cantidad_contenido[0]) - (21 * (i-1))
            todos_nombres.extend(nombre_producto[:corte])
            todos_precios.extend(precio_producto[:corte])
            todas_tiendas.extend(tienda_modificada[:corte])

        ProggresBar.setValue(int((i/pages)*90))
    contenido = (todos_nombres, todos_precios, todas_tiendas)
    return contenido