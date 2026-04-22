import urllib.request
import urllib.parse
import re
import json

medias = [
    "Tlaxcala Digital",
    "Pixel 3000 Tlaxcala",
    "La Bestia Política Tlaxcala",
    "Gentetlx",
    "Escena Informativa Tlaxcala",
    "Generación Press",
    "Cobertura Nacional Tlaxcala",
    "Índice Media Tlaxcala",
    "Nierika Imagen",
    "Estilo Tlax",
    "Telemedios Tlaxcala",
    "Multimedia MX Tlaxcala",
    "Huamantla Hoy",
    "Qué Pasa Tlaxcala",
    "Martin Rodriguez Hernandez Tlaxcala",
    "TV Red Tlaxcala",
    "Agencia Informativa Tlaxcala",
    "Elipse Comunicaciones Tlaxcala",
    "Crónica y Contexto Tlaxcala",
    "El Gritón Digital",
    "TV Zacatelco",
    "Intlax",
    "Tlaxcala Time",
    "El Regional Tlaxcala",
    "DT Noticias Tlaxcala",
    "Línea de Contraste Tlaxcala"
]

results = {}

for media in medias:
    try:
        # DDG HTML search
        query = urllib.parse.urlencode({'q': media})
        req = urllib.request.Request(
            f'https://html.duckduckgo.com/html/?{query}',
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            # Extract first result link
            match = re.search(r'class="result__url" href="([^"]+)"', html)
            if match:
                url = match.group(1)
                # DDG urls are sometimes redirect urls, unescape if needed
                if "uddg=" in url:
                    url = urllib.parse.unquote(url.split("uddg=")[1].split("&")[0])
                results[media.replace(" Tlaxcala", "")] = url
            else:
                results[media.replace(" Tlaxcala", "")] = "#"
    except Exception as e:
        results[media.replace(" Tlaxcala", "")] = "#"

with open("/Users/rodrigolabastida/Documents/COMECOT/media_urls.json", "w") as f:
    json.dump(results, f, indent=4)

print("Done")
