import streamlit as st
import streamlit.components.v1 as components

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Bilanco Analiz Sistemi",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# HTML, CSS ve JS dosyalarını oku
def read_file_content(filename):
    """Dosya içeriğini oku"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        st.error(f"Dosya bulunamadı: {filename}")
        return ""

# Dosyaları oku
html_content = read_file_content("index.html")
css_content = read_file_content("styles.css")
js_content = read_file_content("script.js")

# HTML içeriğini Streamlit'e uygun hale getir
def create_streamlit_html():
    """Streamlit için HTML oluştur"""
    
    # HTML'den head kısmını çıkar ve sadece body içeriğini al
    body_start = html_content.find('<body>')
    body_end = html_content.find('</body>')
    
    if body_start != -1 and body_end != -1:
        body_content = html_content[body_start + 6:body_end]
    else:
        body_content = html_content
    
    # Streamlit için HTML oluştur
    streamlit_html = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bilanco Analiz Sistemi</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            {css_content}
            
            /* Streamlit için özel stiller */
            .main .block-container {{
                padding: 0;
                max-width: 100%;
            }}
            
            .stApp {{
                background: #f8f9fa;
            }}
            
            /* Streamlit sidebar'ı gizle */
            .css-1d391kg {{
                display: none !important;
            }}
            
            /* Streamlit header'ı gizle */
            header[data-testid="stHeader"] {{
                display: none !important;
            }}
            
            /* Streamlit footer'ı gizle */
            footer[data-testid="stFooter"] {{
                display: none !important;
            }}
            
            /* Mobil optimizasyonları */
            @media (max-width: 768px) {{
                .container {{
                    flex-direction: column !important;
                }}
                
                .sidebar {{
                    width: 100% !important;
                    height: auto !important;
                    max-height: 300px !important;
                    position: sticky !important;
                    top: 0 !important;
                    z-index: 100 !important;
                    left: 0 !important;
                }}
                
                .main-content {{
                    margin-left: 0 !important;
                    width: 100% !important;
                }}
                
                .stock-list {{
                    max-height: 200px !important;
                    height: 200px !important;
                }}
                
                .nav-tabs {{
                    flex-wrap: wrap !important;
                    justify-content: center !important;
                }}
                
                .tab-btn {{
                    padding: 8px 12px !important;
                    font-size: 12px !important;
                    min-height: 40px !important;
                }}
                
                .tab-btn i {{
                    display: none !important;
                }}
                
                .analysis-grid, .summary-cards, .ratios-grid, .chart-grid {{
                    grid-template-columns: 1fr !important;
                }}
                
                .card, .summary-card, .ratio-card, .chart-card {{
                    padding: 15px !important;
                }}
                
                canvas {{
                    height: 200px !important;
                    max-height: 200px !important;
                }}
                
                .selected-stock h1 {{
                    font-size: 1.3rem !important;
                }}
                
                .content-area {{
                    padding: 15px !important;
                }}
                
                .top-nav {{
                    padding: 10px 15px !important;
                }}
            }}
            
            @media (max-width: 480px) {{
                .sidebar {{
                    max-height: 250px !important;
                }}
                
                .stock-list {{
                    max-height: 180px !important;
                    height: 180px !important;
                }}
                
                .stock-item {{
                    padding: 12px 15px !important;
                    min-height: 40px !important;
                }}
                
                .tab-btn {{
                    padding: 10px 8px !important;
                    font-size: 11px !important;
                    min-width: 60px !important;
                }}
                
                .card, .summary-card, .ratio-card, .chart-card {{
                    padding: 12px !important;
                }}
                
                .summary-card .value {{
                    font-size: 1.3rem !important;
                }}
                
                canvas {{
                    height: 180px !important;
                    max-height: 180px !important;
                }}
                
                .content-area {{
                    padding: 10px !important;
                }}
                
                .top-nav {{
                    padding: 8px 10px !important;
                }}
                
                .selected-stock h1 {{
                    font-size: 1.1rem !important;
                }}
            }}
        </style>
    </head>
    <body>
        {body_content}
        
        <script>
            {js_content}
        </script>
    </body>
    </html>
    """
    
    return streamlit_html

# Ana uygulama
def main():
    """Ana Streamlit uygulaması"""
    
    # HTML içeriğini oluştur
    html_content = create_streamlit_html()
    
    # HTML'i Streamlit'e göm - Mobil için dinamik yükseklik
    components.html(
        html_content,
        height=700,  # Mobil için optimize edilmiş yükseklik
        scrolling=True
    )
    
    # Sidebar'ı tamamen gizle
    st.markdown("""
    <style>
    .css-1d391kg {{
        display: none !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# Uygulamayı çalıştır
if __name__ == "__main__":
    main()