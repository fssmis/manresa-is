import json
import os

def generate_html():
    with open('database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Template base per a totes les pàgines
    template = """
    <!DOCTYPE html>
    <html lang="ca">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | Manresa.is</title>
        <link rel="stylesheet" href="style.css">
        <script src="script.js" defer></script>
    </head>
    <body>
        <nav>...</nav>
        <main>{content}</main>
        <footer>...</footer>
    </body>
    </html>
    """
    
    # Genera cada pàgina definida al JSON
    for page in data['pages']:
        filename = page['filename']
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template.format(title=page['title'], content=page['html_content']))
        print(f"Creada: {filename}")

if __name__ == "__main__":
    generate_html()
