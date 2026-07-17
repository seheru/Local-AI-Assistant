from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import json

app = Flask(__name__)
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# --- YAPAY ZEKA HAFIZASI ---
user_memory = {
    "gender": "Female",
    "body": "BMI 20.0, Long limbs.",
    "cycle": "Day 20 (Luteal Phase / PMS).",
    "chronic": ["Chronic Hypotension", "Mild Meniscus Wear", "Sensitive Wrists"],
    "acute": ["Severe Leg DOMS"],
    "history": "2 years yoga, occasional HIIT cardio",
    "goals": "Gain functional strength via Calisthenics"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/profile', methods=['POST'])
def update_profile():
    data = request.json
    user_memory["chronic"] = data.get("chronic", [])
    user_memory["acute"] = data.get("acute", [])
    user_memory["history"] = data.get("history", "")
    user_memory["goals"] = data.get("goals", "")
    return jsonify({"status": "success", "message": "Memory updated!"})

# --- YENİ: BESLENME HESAPLAMA ROTASI ---
@app.route('/api/nutrition', methods=['POST'])
def analyze_nutrition():
    meal_text = request.json.get('meal')
    
    # AI'a sıkı bir talimat veriyoruz: "Sadece JSON döndür"
    system_instruction = """You are a precise nutrition calculator API. 
The user will tell you what they ate. You must estimate the macros (Protein, Carbs, Fat) in grams.
Respond ONLY with a valid JSON object. Do not write any other text.
Format must be exactly like this:
{"protein": 12, "carbs": 5, "fat": 10}
"""

    try:
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": meal_text}
            ],
            temperature=0.1 # Matematiğin düzgün olması için yaratıcılığı çok düşürüyoruz
        )
        
        ai_response = response.choices[0].message.content
        
        # AI'dan gelen metni gerçek bir JSON'a dönüştür
        try:
            macros = json.loads(ai_response)
            return jsonify(macros)
        except:
            # Eğer AI saçmalayıp metin yazarsa hata fırlat
            return jsonify({"error": "AI did not return proper JSON."}), 500
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    compiled_profile = f"""
User Profile & Medical Data:
- Gender: {user_memory['gender']}
- Body: {user_memory['body']}
- Cycle Phase: {user_memory['cycle']}
- Chronic Conditions: {', '.join(user_memory['chronic']) if user_memory['chronic'] else 'None'}
- Acute Conditions: {', '.join(user_memory['acute']) if user_memory['acute'] else 'None'}
- Workout History: {user_memory['history']}
- Goals: {user_memory['goals']}
"""

    system_instruction = f"""You are the user's personal health and fitness assistant, functioning as a professional yet friendly doctor. Your name is Dr. AI. 
Keep your answers concise, practical, and strictly to the point. Do not write long essays.
Always consider the user's medical profile below before answering:

{compiled_profile}
"""

    try:
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7 
        )
        
        return jsonify({"reply": response.choices[0].message.content})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)