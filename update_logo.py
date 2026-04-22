import os

html_files = ["index.html", "nosotros.html", "directorio.html", "contacto.html"]
old_logo = '<img src="logo.png" alt="Logo COMECOT" class="logo" style="mix-blend-mode: multiply;">'
new_logo = '<span class="logo-text">COMECOT</span>'

for filename in html_files:
    filepath = os.path.join("/Users/rodrigolabastida/Documents/COMECOT", filename)
    with open(filepath, 'r') as f:
        content = f.read()
    content = content.replace(old_logo, new_logo)
    with open(filepath, 'w') as f:
        f.write(content)

# Add CSS for logo-text
css_to_add = """
.logo-text {
    font-size: 1.8rem;
    font-weight: 900;
    letter-spacing: 2px;
    color: var(--color-primary);
    text-transform: uppercase;
}
"""

with open("/Users/rodrigolabastida/Documents/COMECOT/styles.css", 'a') as f:
    f.write(css_to_add)

print("Replacement complete.")
