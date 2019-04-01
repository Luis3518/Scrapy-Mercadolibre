import scrapy


class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #informacion del producto
    titulo = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    ubicacion = scrapy.Field()
    opiniones = scrapy.Field()

    #link perfil del vendedor
    vendedor_url = scrapy.Field()
