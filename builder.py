import json

def generate_manresia():
    with open('database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    info = data['manresIA_content']
    
    html = f"""
    <!DOCTYPE html>
    <html lang="ca">
    <head>
        <meta charset="UTF-8">
        <title>ManresIA | Manresa.is</title>
        <link rel="stylesheet" href="style.css">
        <style>
            body {{ font-family: -apple-system, sans-serif; padding: 40px; max-width: 800px; margin: auto; }}
            .ia-card {{ border: 2px solid #f05a28; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
            .tifa {{ background: #1a1a1a; color: white; padding: 15px; border-radius: 8px; font-style: italic; }}
            .orange {{ color: #f05a28; font-weight: bold; }}
        </style>
    </head>
    <body>
        <nav><a href="index.html">← Tornar a la web principal</a></nav>
        <h1 style="font-family: Georgia, serif; font-size: 3rem;">Manres<span class="orange">IA</span></h1>
        <p>Aquest espai s'alimenta sol cada 24 hores.</p>
        
        <div class="ia-card">
            <span class="orange">PARAULA DEL DIA:</span>
            <h2>{info['word_of_the_day']['word']}</h2>
            <p>{info['word_of_the_day']['definition']}</p>
            <p><i>"{info['word_of_the_day']['example']}"</i></p>
        </div>

        <div class="tifa">
            <strong>🕵️ Agent Tifa diu:</strong><br>
            "{info['word_of_the_day']['agent_tifa']}"
        </div>

        <div style="margin-top: 40px;">
            <h3>Dades de Smart City</h3>
            <p>{info['smart_city_news']}</p>
            <hr>
            <h3>Memòria Històrica</h3>
            <p>{info['history_snippet']}</p>
        </div>
    </body>
    </html>
    """
    
    with open('manresia.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    generate_manresia()
