import json

def generate_manresia():
    with open('database.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    info = data['manresIA_content']
    paraules = info['hemeroteca_parlar']
    word_today = paraules[0] # La més recent
    
    # Generem l'HTML de l'hemeroteca amb sistema de clic
    hemeroteca_html = ""
    for i, p in enumerate(paraules):
        # Fem que totes siguin clicables, fins i tot la d'avui a la llista
        hemeroteca_html += f"""
        <div class="hemeroteca-item">
            <button class="accordion" onclick="toggleAccordion(this)">
                <strong>{p['word']}</strong> <span class="date">({p['date']})</span>
                <span class="icon">+</span>
            </button>
            <div class="panel">
                <p><strong>Definició:</strong> {p['definition']}</p>
                <p><em>"{p['example']}"</em></p>
            </div>
        </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="ca">
    <head>
        <meta charset="UTF-8">
        <title>ManresIA | Manresa.is</title>
        <style>
            body {{ font-family: -apple-system, sans-serif; padding: 40px; max-width: 800px; margin: auto; line-height: 1.6; color: #1a1a1a; }}
            .nav-back {{ margin-bottom: 20px; }}
            .nav-back a {{ text-decoration: none; color: #f05a28; font-weight: bold; }}
            h1 {{ font-family: Georgia, serif; font-size: 3.5rem; margin-bottom: 10px; }}
            .orange {{ color: #f05a28; }}
            
            .ia-card {{ border: 2px solid #f05a28; padding: 30px; border-radius: 12px; margin-bottom: 30px; background: #fffcfb; }}
            .tifa {{ background: #1a1a1a; color: white; padding: 25px; border-radius: 8px; font-style: italic; margin: 30px 0; border-left: 5px solid #f05a28; }}
            
            /* Estils Acordió */
            .hemeroteca {{ margin-top: 50px; }}
            .accordion {{ 
                background-color: #f4f4f4; color: #444; cursor: pointer; padding: 18px; width: 100%;
                border: none; text-align: left; outline: none; font-size: 1.1rem; transition: 0.4s;
                border-radius: 8px; margin-bottom: 5px; display: flex; justify-content: space-between;
            }}
            .active, .accordion:hover {{ background-color: #eee; border-left: 4px solid #f05a28; }}
            .panel {{ 
                padding: 0 18px; background-color: white; max-height: 0; overflow: hidden;
                transition: max-height 0.2s ease-out; border-bottom: 1px solid #eee; margin-bottom: 10px;
            }}
            .date {{ font-size: 0.8rem; color: #888; margin-left: 10px; }}
            
            footer {{ margin-top: 60px; font-size: 0.85rem; color: #666; border-top: 1px solid #eee; padding-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="nav-back"><a href="index.html">← Tornar a Manresa.is</a></div>
        <h1>Manres<span class="orange">IA</span></h1>
        <p><i>Trets formals, fonètics, morfològics, sintàctics, lèxics i de fraseologia propis de la ciutat.</i></p>
        
        <div class="ia-card">
            <span class="orange">LA PARAULA D'AVUI:</span>
            <h2 style="font-size: 2.5rem; margin: 10px 0;">{word_today['word']}</h2>
            <p style="font-size: 1.2rem;">{word_today['definition']}</p>
        </div>

        <div class="tifa">
            <strong>🕵️ El pardal manresà diu:</strong><br>
            "{info['agent_tifa_avui']}"
        </div>

        <div class="hemeroteca">
            <h3>📚 Hemeroteca del parlar</h3>
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 15px;">Fes clic a cada paraula per veure'n el significat i l'exemple.</p>
            {hemeroteca_html}
        </div>

        <footer>
            Dades: El parlar de Manresa, de Jaume Puig Ibáñez.
        </footer>

        <script>
            function toggleAccordion(btn) {{
                btn.classList.toggle("active");
                var icon = btn.querySelector(".icon");
                var panel = btn.nextElementSibling;
                if (panel.style.maxHeight) {{
                    panel.style.maxHeight = null;
                    icon.innerHTML = "+";
                }} else {{
                    panel.style.maxHeight = panel.scrollHeight + "px";
                    icon.innerHTML = "-";
                }}
            }}
        </script>
    </body>
    </html>
    """
    
    with open('manresia.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    generate_manresia()
