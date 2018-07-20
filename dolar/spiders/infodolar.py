# -*- coding: utf-8 -*-
import scrapy


class InfodolarSpider(scrapy.Spider):
    name = 'infodolar'
    allowed_domains = ['www.infodolar.com/']
    start_urls = ['https://www.infodolar.com//']

    def parse(self, response):
        cotizaciones = {"results":[]}
        for table in response.css('[id="ctl00_PlaceHolderLeftColumn_GridViewDolar"]'):
            for row in table.css('tr'):
                cells = row.css('td')
                if cells != []:
                    cotizacion = {
                        "banco": cells.css('span::text').extract()[0],
                        "compra": cells.css('.colCompraVenta::text').extract()[0].strip(),
                        "venta": cells.css('.colCompraVenta::text').extract()[1].strip(),
                        "update": cells.css('abbr::attr(title)').extract()[0].strip()
                    }
                    cotizaciones["results"].append(cotizacion)
            yield cotizaciones
