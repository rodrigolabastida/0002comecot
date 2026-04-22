import json
import re

members = [
    ("Ana Montiel", "Tlaxcala Digital"),
    ("Ana Hernández", "Pixel 3000"),
    ("Constanza Guarneros", "385 Grados"),
    ("Edgar García", "La Bestia Política"),
    ("Edgardo Cabrera", "Gentetlx"),
    ("Emilio Vázquez", "Escena Informativa"),
    ("Enrique Gasga", "Generación Press"),
    ("Francisco Ortiz", "Cobertura Nacional"),
    ("Francisco Conde", "Índice Media"),
    ("Gonzálo Pérez", "Nierika Imagen"),
    ("Iliana Cervantes", "Estilo Tlax"),
    ("Isabel Aquino", "Telemedios"),
    ("Ismael Gracia", "Multimedia MX"),
    ("Maribel Saldaña", "Huamantla Hoy"),
    ("Marisol Saldaña", "¿Qué Pasa Tlaxcala?"),
    ("Martín Rodríguez", "Noticias MR"),
    ("Mary Sánchez", "TV Red Tlaxcala"),
    ("Miguel García", "Agencia Informativa"),
    ("Miriam Bueno", "Elipse Comunicaciones"),
    ("Orquidea Sánchez", "Crónica y Contexto"),
    ("Rene Arellano", "El Gritón Digital"),
    ("Ricardo Salazar", "TV Zacatelco"),
    ("Rodrigo Labastida", "Intlax"),
    ("Rubén Hernández", "Tlaxcala Time"),
    ("Teresa Lara", "El Regional"),
    ("Victor Rodríguez", "DT Noticias"),
    ("Viridiana Marroquín", "Línea de Contraste")
]

try:
    with open('media_urls.json', 'r') as f:
        urls = json.load(f)
except:
    urls = {}

manual_urls = {
    "Índice Media": "https://indicemedia.com.mx/",
    "Estilo Tlax": "https://estilotlax.com/",
    "Telemedios": "https://telemedios.mx/",
    "¿Qué Pasa Tlaxcala?": "https://quepasatlaxcala.com",
    "Huamantla Hoy": "https://huamantlahoy.mx",
    "El Gritón Digital": "https://elgriton.mx",
    "Noticias MR": "https://martinrodriguezhernandez.com/",
    "Crónica y Contexto": "https://cronicaycontexto.com.mx/",
    "385 Grados": "https://385grados.com/"
}

cards_html = ""
for name, media in members:
    url = "#"
    for k, v in urls.items():
        if k.lower() in media.lower() or media.lower() in k.lower():
            if v != "#": url = v
    if media in manual_urls:
        url = manual_urls[media]
    
    card = f"""
                    <div class="media-card">
                        <div class="media-logo-placeholder">
                            {media}
                        </div>
                        <div class="media-card-content">
                            <h3>{media}</h3>
                            <p style="color: var(--color-primary); font-weight: 600; font-size: 0.9rem; margin-bottom: 0.5rem;">{name}</p>
                            <p>Medio de comunicación y noticias del estado.</p>
                            <a href="{url}" target="_blank" rel="noopener noreferrer" class="media-link">
                                Visitar Sitio Web 
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </a>
                        </div>
                    </div>"""
    cards_html += card

with open('directorio.html', 'r') as f:
    content = f.read()

new_content = re.sub(r'<div class=\"directory-grid\">.*?</div>\n            </div>\n        </section>', '<div class=\"directory-grid\">' + cards_html + '</div>\n            </div>\n        </section>', content, flags=re.DOTALL)
with open('directorio.html', 'w') as f:
    f.write(new_content)
