# Scrapy-Mercadolibre

*******************Desactualizado*********************
Scrapy de mercadolibre

Bot de scrapy python para descargar información de productos de mercadolibre.

Para scrappear hay que bajarse anaconda del siguiente enlace: https://www.anaconda.com/

 Abrir anaconda prompt, situarse en la carpeta del proyecto y ejecutar el comando
 
“scrapy crawl mercado -t csv (mercado es el nombre del bot y de la clase)”



MiniTutorial scrapy paso a paso

Primero seleccionar la página (yo la categoría del xiaomi note 6 pro en mercadolibre)

Crear un nuevo proyecto, importante que tenga un nombre coherente ya que después se va a usar para el código.

En la terminal de anaconda poner:

“scrapy startproject nombreproyecto”

El proyecto se va a crear dentro de la carpeta del usuario, en mi caso “Luis”

Elegir una URL de inicio, en mi caso “https://celulares.mercadolibre.com.ar/xiaomi/note-6-pro/”

También hay que buscar, la url en caso de segunda pagina, en mi caso “https://celulares.mercadolibre.com.ar/xiaomi/note-6-pro/_Desde_51”


Para que el sistema busque automáticamente todas las clases que tienen un link de producto valido, hay que buscar con el “inspeccionar elemento” cada clase y subclase que tiene un link.

En el caso del titulo, por ejemplo, es:

(Dentro de H2) la clase “item__title list-view-item-title” y dentro de esa clase la otra clase “item__info-title”

"response.xpath("//h2[contains(@class, 'item__title list-view-item-title')]/a[contains(@class, 'item__info-title')]//@href").extract()"

Luego en el link del producto, podemos buscar cada dato que queremos extraer, con el shell, en este caso

"scrapy shell (link del producto individual)"

Y luego este comando para extraer el titulo exacto:

"response.xpath("//h1[contains(@class, 'item-title__primary')]).extract()"


Este proyecto ya tiene configurado para extraer los siguientes datos:

Título del producto

Valor

Condición

Zona del producto

Perfil del vendedor


Link de los productos a extraer datos se coloca en spider/spider.py

Límite de productos se coloca en spider/spider.py

div o clase de html con cada item que se quiere extraer de un producto (precio, titulo, etc) en spider/spider.py

Los archivos más importantes para modificar son:

settings.py

pipelines.py

items.py

spider/spider.py

Para scrappear hay que bajarse anaconda, abrir anaconda prompt, stuarse en la carpeta del proyecto y ejecutar el comando
scrapy crawl mercado -t csv (mercado es el nombre del bot y de la clase)


Pueden seguirme en:

https://profeluisrodriguez.wordpress.com

https://www.linkedin.com/in/luis-rodriguez3518/
