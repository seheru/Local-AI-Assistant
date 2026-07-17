from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# LM Studio'ya (Local Server) bağlanmak için ayarlar
# base_url kısmında 1234 portu LM Studio'nun standart portudur
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

@app.route('/')
def home():
    return render_template('index.html')

# Yeni: Arayüzden gelen mesajları yapay zekaya ileten köprü
@app.route('/api/chat', methods=['POST'])
def chat():
    # HTML'den gelen mesajı al
    user_message = request.json.get('message')
    
    try:
        # LM Studio'ya (Llama 3'e) soruyu sor
        response = client.chat.completions.create(
            model="local-model", # LM Studio için isim fark etmez
            messages=[
                # AI'ın karakterini belirliyoruz (Sistem Promptu)
                {"role": "system", "content": "You are the user's personal health and fitness assistant, functioning as a professional yet friendly doctor. Your name is Dr. AI. Keep your answers concise, practical, and strictly to the point. Do not write long essays. Avoid unnecessary details. If the user asks for advice, provide clear and actionable steps. Always maintain a professional tone, but be approachable and empathetic."},
                # Kullanıcının yazdığı mesaj
                {"role": "user", "content": user_message}
            ],
            temperature=0.7 # Yaratıcılık seviyesi
        )
        
        # Gelen cevabı yakala ve HTML'e geri gönder
        ai_message = response.choices[0].message.content
        return jsonify({"reply": ai_message})
        
    except Exception as e:
        # Eğer LM Studio kapalıysa veya hata olursa ekrana bunu bas
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)