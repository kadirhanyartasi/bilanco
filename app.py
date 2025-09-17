import streamlit as st
import streamlit.components.v1 as components
import os

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
    
    # HTML'i Streamlit'e göm
    components.html(
        html_content,
        height=800,
        scrolling=True
    )
    
    # Streamlit sidebar'da bilgi
    with st.sidebar:
        st.title("📊 Bilanco Analiz Sistemi")
        st.markdown("""
        ### 🎯 Özellikler
        - **150+ Hisse Analizi**
        - **Gerçek Finansal Veriler**
        - **İnteraktif Grafikler**
        - **Responsive Tasarım**
        - **Modern UI/UX**
        
        ### 🚀 Kullanım
        1. Sol taraftan hisse seçin
        2. Analiz türünü belirleyin
        3. Grafikleri inceleyin
        
        ### 📊 Analiz Türleri
        - **Genel Bilgi**: Sistem hakkında
        - **Veri Analizi**: Finansal grafikler
        - **Raporlama**: Özet raporlar
        - **Hesaplamalar**: Finansal oranlar
        - **Görselleştirme**: İnteraktif grafikler
        """)
        
        st.markdown("---")
        st.markdown("""
        ### 🔧 Teknik Detaylar
        - **Platform**: Streamlit + HTML/CSS/JS
        - **Grafikler**: Chart.js
        - **Veriler**: Gömülü finansal veriler
        - **Tasarım**: Modern responsive
        """)

# Uygulamayı çalıştır
if __name__ == "__main__":
    main()