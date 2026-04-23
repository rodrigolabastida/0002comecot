import os

html_files = ["index.html", "nosotros.html", "directorio.html", "contacto.html"]
old_logo = '<span class="logo-text">COMECOT</span>'
new_logo = '<img src="logo.jpg" alt="Logo COMECOT" class="logo" style="mix-blend-mode: multiply;">'

for filename in html_files:
    filepath = os.path.join("/Users/rodrigolabastida/Documents/COMECOT", filename)
    with open(filepath, 'r') as f:
        content = f.read()
    content = content.replace(old_logo, new_logo)
    with open(filepath, 'w') as f:
        f.write(content)

print("Replacement complete.")
