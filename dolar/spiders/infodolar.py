# -*- coding: utf-8 -*-
import scrapy


class InfodolarSpider(scrapy.Spider):
    name = 'infodolar'
    allowed_domains = ['www.infodolar.com/']
    start_urls = ['https://www.infodolar.com//']

    def parse(self, response):
        cotizaciones = {
            "dolar": self._parse_table(response, "ctl00_PlaceHolderMainContent_GridViewDolar"),
            "euro": self._parse_table(response, "ctl00_PlaceHolderMainContent_GridViewEuro"),
            "real": self._parse_table(response, "ctl00_PlaceHolderMainContent_GridViewReal"),
            "pesoUruguayo": self._parse_table(response, "ctl00_PlaceHolderMainContent_GridViewPesoUruguayo"),
            "pesoChileno": self._parse_table(response, "ctl00_PlaceHolderMainContent_GridViewPesoChileno")
        }
        yield cotizaciones

    @staticmethod
    def _parse_table(response, id):
        cotizaciones = []
        for table in response.css('[id="{0}"]'.format(id)):
            for row in table.css('tr'):
                cells = row.css('td')
                if cells != []:
                    cotizacion = {
                        "banco": cells.css('span::text').extract()[0],
                        "compra": cells.css('.colCompraVenta::text').extract()[0].strip(),
                        "venta": cells.css('.colCompraVenta::text').extract()[1].strip(),
                        "update": cells.css('abbr::attr(title)').extract()[0].strip()
                    }
                    cotizaciones.append(cotizacion)
        return cotizaciones
