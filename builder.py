import json

def generate_manresia():
    with open('database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    info = data['manresIA_content']
    paraules = info['hemeroteca_parlar']
    word_today = paraules[0] # La primera de la llista és la d'avui
    
    # Generem l'HTML de l'hemeroteca
    hemeroteca_html = ""
    for p in paraules[1:]: # Les altres van a l'històric
        hemeroteca_html += f"<li><strong>{p['word']}</strong> ({p['date']}): {p['definition']}</li>"

    html = f"""
    <!DOCTYPE html>
    <html lang="ca">
    <head>
        <meta charset="UTF-8">
        <title>ManresIA | Manresa.is</title>
        <link rel="stylesheet" href="style.css">
        <style>
            body {{ font-family: -apple-system, sans-serif; padding: 40px; max-width: 800px; margin: auto; line-height: 1.6; }}
            .ia-card {{ border: 2px solid #f05a28; padding: 25px; border-radius: 12px; margin-bottom: 20px; background: #fffcfb; }}
            .tifa {{ background: #1a1a1a; color: white; padding: 20px; border-radius: 8px; font-style: italic; margin: 20px 0; }}
            .hemeroteca {{ background: #f4f4f4; padding: 20px; border-radius: 8px; margin-top: 40px; border-top: 4px solid #ccc; }}
            .orange {{ color: #f05a28; font-weight: bold; }}
        </style>
    </head>
    <body>
        <nav><a href="index.html">← Tornar a la web principal</a></nav>
        <h1 style="font-family: Georgia, serif; font-size: 3.5rem; margin-bottom:10px;">Manres<span class="orange">IA</span></h1>
        <p><i>L'algoritme que entén el Bages.</i></p>
        
        <div class="ia-card">
            <span class="orange">PARAULA DEL DIA:</span>
            <h2 style="font-size: 2.5rem; margin: 10px 0;">{word_today['word']}</h2>
            <p style="font-size: 1.2rem;">{word_today['definition']}</p>
            <p><i>"{word_today['example']}"</i></p>
        </div>

        <div class="tifa">
            <strong>🕵️ Agent Tifa diu:</strong><br>
            "{info['agent_tifa_avui']}"
        </div>

        <div class="hemeroteca">
            <h3>📚 Hemeroteca del parlar</h3>
            <ul>{hemeroteca_html}</ul>
        </div>

        <footer style="margin-top: 50px; font-size: 0.8rem; color: #666;">
            Dades: Ajuntament de Manresa | Fonts: El Pou de la Gallina.
        </footer>
    </body>
    </html>
    """
    
    with open('manresia.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    generate_manresia()
