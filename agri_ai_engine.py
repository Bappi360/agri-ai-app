"""
Agri AI Engine (কৃষি এআই ইঞ্জিন)
Handles communication with:
1. Groq Cloud (Llama 3.3 70B / 3.1 8B)
2. Google Gemini API (Direct REST endpoint)
3. Smart Built-in Agriculture Expert Engine (Offline & Free)
"""

import os
import json
import requests
from typing import List, Dict, Any, Optional
from agri_knowledge_base import CROPS_DATA, ORGANIC_PESTICIDES, SEASONAL_CALENDAR
from fertilizer_calc import FERTILIZER_RATES_PER_DECIMAL

# Default Agricultural System Prompt
AGRI_SYSTEM_PROMPT = """You are 'AgriSathi AI' (কৃষি সাথী এআই), an expert senior agricultural scientist and farm extension advisor.
You provide farmers, agronomists, and home gardeners with scientifically accurate, practical, and eco-friendly farming advice.

Guidelines:
1. Language: Answer in Bengali if the user asks in Bengali or selects Bengali. Answer in English if the user asks in English. If the user uses Banglish, reply in clear, friendly Bengali (বাংলা).
2. Structure your answers clearly:
   - 🌾 পরিচিতি ও কারণ (Overview & Causes)
   - 🔍 লক্ষণসমূহ (Visible Symptoms / Identification)
   - 🌿 জৈব ও প্রাকৃতিক প্রতিকার (Organic & Eco-friendly Remedies)
   - 🧪 রাসায়নিক সমাধান ও সঠিক ডোজ (Chemical Solutions with exact generic name & dosage)
   - 🛡️ প্রতিরোধমূলক সতর্কতা (Preventive agronomic practices for next season)
3. Be encouraging, empathetic, and respectful to farmers.
4. Always prioritize farmer safety (protective gear when spraying, safe waiting period before harvesting).
"""

def generate_local_expert_response(prompt: str, lang: str = "bn") -> str:
    """
    Intelligent local agricultural response generator using domain knowledge base.
    Works 100% offline without needing any external API keys!
    """
    prompt_lower = prompt.lower()
    
    # 1. Check for specific crops
    detected_crop = None
    for crop_id, crop in CROPS_DATA.items():
        if crop_id in prompt_lower or any(word in prompt_lower for word in crop["name_bn"].lower().split()) or any(word in prompt_lower for word in crop["name_en"].lower().split()):
            detected_crop = crop
            break
            
    # Check for fertilizer queries
    is_fertilizer_query = any(k in prompt_lower for k in ["সার", "ইউরিয়া", "টিএসপি", "পটাশ", "fertilizer", "dose", "ডোজ", "মাত্রা", "জিপসাম"])
    # Check for disease / pest queries
    is_disease_query = any(k in prompt_lower for k in ["রোগ", "পোকা", "বালাই", "পোকামাকড়", "পাতা", "দাগ", "পচা", "disease", "pest", "fungus", "blight", "blast", "পোকা"])
    # Check for organic pesticide queries
    is_organic_query = any(k in prompt_lower for k in ["জৈব", "প্রাকৃতিক", "নিম", "organic", "bio", "ট্রাইকোডার্মা"])
    # Check for seasonal calendar queries
    is_season_query = any(k in prompt_lower for k in ["মৌসুম", "ক্যালেন্ডার", "কখন", "সময়", "রবি", "খরিফ", "season", "calendar", "when to plant"])

    if detected_crop:
        if is_fertilizer_query:
            if lang == "bn":
                return (
                    f"### 🌾 {detected_crop['name_bn']} - সারের সঠিক মাত্রা ও প্রয়োগ নির্দেশিকা\n\n"
                    f"**উপযুক্ত মাটি:** {detected_crop['soil_bn']}\n\n"
                    f"**সারের পরিমাণ:**\n{detected_crop['fertilizer_guide_bn']}\n\n"
                    f"💡 *টিপস:* বিস্তারিত হিসাব পেতে আমাদের 'সার ক্যালকুলেটর' (Fertilizer Calculator) ট্যাব ব্যবহার করুন।"
                )
            else:
                return (
                    f"### 🌾 {detected_crop['name_en']} - Fertilizer Guidelines\n\n"
                    f"**Optimal Soil:** {detected_crop['soil_en']}\n\n"
                    f"**Dosage Recommendation:**\n{detected_crop['fertilizer_guide_en']}\n\n"
                    f"💡 *Tip:* Use our built-in 'Fertilizer Calculator' tab for area-specific calculations."
                )
                
        if is_disease_query:
            diseases_info = ""
            if lang == "bn":
                for d in detected_crop.get("diseases", []):
                    diseases_info += (
                        f"#### 🔍 {d['name_bn']}\n"
                        f"- **লক্ষণ:** {d['symptoms_bn']}\n"
                        f"- **রাসায়নিক প্রতিকার:** {d['chemical_cure_bn']}\n"
                        f"- **জৈব ও প্রতিরোধমূলক ব্যবস্থা:** {d['organic_cure_bn']}\n\n"
                    )
                pests_info = ""
                for p in detected_crop.get("pests", []):
                    pests_info += f"- **{p['name_bn']}:** {p['remedy_bn']}\n"
                
                return (
                    f"### 🌾 {detected_crop['name_bn']} - রোগবালাই ও পোকা দমন নির্দেশিকা\n\n"
                    f"{diseases_info}\n"
                    f"#### 🐛 ক্ষতিকর পোকা ও দমন ব্যবস্থা:\n{pests_info}\n\n"
                    f"⚠️ *সতর্কতা:* যে কোনো বালাইনাশক স্প্রে করার সময় মুখে মাস্ক ও হাতে গ্লাভস পরিধান করুন এবং বিকেলে স্প্রে করুন।"
                )
            else:
                for d in detected_crop.get("diseases", []):
                    diseases_info += (
                        f"#### 🔍 {d['name_en']}\n"
                        f"- **Symptoms:** {d['symptoms_en']}\n"
                        f"- **Chemical Treatment:** {d['chemical_cure_en']}\n"
                        f"- **Organic/Cultural Care:** {d['organic_cure_en']}\n\n"
                    )
                pests_info = ""
                for p in detected_crop.get("pests", []):
                    pests_info += f"- **{p['name_en']}:** {p['remedy_en']}\n"
                
                return (
                    f"### 🌾 {detected_crop['name_en']} - Disease & Pest Management\n\n"
                    f"{diseases_info}\n"
                    f"#### 🐛 Major Pests & Control:\n{pests_info}\n\n"
                    f"⚠️ *Safety:* Wear protective gear when applying chemicals, and avoid spraying during high wind or noon heat."
                )

        # General info about detected crop
        if lang == "bn":
            return (
                f"### 🌾 {detected_crop['name_bn']} চাষাবাদ নির্দেশিকা\n\n"
                f"- **ক্যাটাগরি:** {detected_crop['category_bn']}\n"
                f"- **উপযুক্ত মৌসুম:** {detected_crop['seasons_bn']}\n"
                f"- **মাটি ও পরিবেশ:** {detected_crop['soil_bn']}\n\n"
                f"**সারের পরামর্শ:**\n{detected_crop['fertilizer_guide_bn']}\n\n"
                f"আপনি কি এই ফসলের নির্দিষ্ট কোনো রোগ বা পোকা সম্পর্কে জানতে চান? নিচে প্রশ্ন লিখুন।"
            )
        else:
            return (
                f"### 🌾 {detected_crop['name_en']} Farming Overview\n\n"
                f"- **Category:** {detected_crop['category_en']}\n"
                f"- **Growing Seasons:** {detected_crop['seasons_en']}\n"
                f"- **Soil & Environment:** {detected_crop['soil_en']}\n\n"
                f"**Fertilizer Recommendations:**\n{detected_crop['fertilizer_guide_en']}\n\n"
                f"Would you like details on specific diseases, pests, or irrigation stages for this crop?"
            )

    if is_organic_query:
        if lang == "bn":
            res = "### 🌿 প্রাকৃতিক ও জৈব বালাইনাশক তৈরি ও প্রয়োগ:\n\n"
            for k, item in ORGANIC_PESTICIDES.items():
                res += f"#### ✅ {item['title_bn']}\n{item['usage_bn']}\n\n"
            return res
        else:
            res = "### 🌿 Eco-friendly & Organic Pesticides:\n\n"
            for k, item in ORGANIC_PESTICIDES.items():
                res += f"#### ✅ {item['title_en']}\n{item['usage_en']}\n\n"
            return res

    if is_season_query:
        if lang == "bn":
            res = "### 📅 বাংলাদেশের কৃষি মৌসুম ও ফসলের তালিকা:\n\n"
            for k, s in SEASONAL_CALENDAR.items():
                crops = ", ".join(s["major_crops_bn"])
                res += f"#### 🌾 {s['season_bn']}\n- **আবহাওয়া:** {s['weather_bn']}\n- **প্রধান ফসলসমূহ:** {crops}\n\n"
            return res
        else:
            res = "### 📅 Agricultural Crop Calendar:\n\n"
            for k, s in SEASONAL_CALENDAR.items():
                crops = ", ".join(s["major_crops_en"])
                res += f"#### 🌾 {s['season_en']}\n- **Weather Conditions:** {s['weather_en']}\n- **Major Crops:** {crops}\n\n"
            return res

    # General fallback response
    if lang == "bn":
        return (
            "🌾 **কৃষি সাথী এআই (AgriSathi AI) আপনার সেবায় প্রস্তুত!**\n\n"
            "আপনি কৃষি বিষয়ক যে কোনো প্রশ্ন করতে পারেন। যেমন:\n"
            "- ধানের ব্লাস্ট বা পাতাপোড়া রোগের ওষুধ কি?\n"
            "- বিঘাতে আলুর সার ব্যবস্থাপনা ও সঠিক ডোজ\n"
            "- টমেটো পাতা কুঁকড়ে যাওয়া বা ফুল ঝরে পড়ার সমাধান\n"
            "- জৈব পদ্ধতিতে পোকা দমন বা নিম তেলের স্প্রে তৈরি\n"
            "- গম, ভুট্টা বা বেগুনের চাষাবাদ ও রোগ নিয়ন্ত্রণ\n\n"
            "💬 *আপনার ফসলের নাম ও সমস্যার লক্ষণ লিখে বিস্তারিত প্রশ্ন করুন।*"
        )
    else:
        return (
            "🌾 **AgriSathi AI is ready to help you!**\n\n"
            "You can ask any agriculture-related questions, such as:\n"
            "- How to treat Rice Blast or Bacterial Leaf Blight?\n"
            "- Fertilizer calculation for potato or wheat per acre\n"
            "- How to prevent Tomato Leaf Curl Virus?\n"
            "- How to prepare organic neem pesticide?\n"
            "- Pest management for Brinjal Shoot Borer or Fall Armyworm\n\n"
            "💬 *Please specify your crop and visible symptoms for a tailored recommendation.*"
        )


def query_groq_api(api_key: str, messages: List[Dict[str, str]], model: str = "llama-3.3-70b-versatile") -> str:
    """Query Groq Cloud LLM"""
    from groq import Groq
    client = Groq(api_key=api_key)
    
    # Ensure system prompt is present
    formatted_messages = []
    has_system = any(m["role"] == "system" for m in messages)
    if not has_system:
        formatted_messages.append({"role": "system", "content": AGRI_SYSTEM_PROMPT})
    formatted_messages.extend(messages)
    
    response = client.chat.completions.create(
        model=model,
        messages=formatted_messages,
        temperature=0.3,
        max_tokens=2048,
    )
    return response.choices[0].message.content


def query_gemini_api(api_key: str, messages: List[Dict[str, str]], model: str = "gemini-2.5-flash") -> str:
    """Query Google Gemini API via REST endpoint"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    
    contents = []
    # Add system instruction if supported or prepend to first message
    system_text = AGRI_SYSTEM_PROMPT
    
    for idx, msg in enumerate(messages):
        role = "user" if msg["role"] == "user" else "model"
        text = msg["content"]
        if idx == 0 and role == "user":
            text = f"[SYSTEM INSTRUCTION: {system_text}]\n\n{text}"
        contents.append({
            "role": role,
            "parts": [{"text": text}]
        })
        
    payload = {
        "contents": contents,
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 2048
        }
    }
    
    resp = requests.post(url, json=payload, timeout=40)
    if resp.status_code != 200:
        # Fallback to gemini-1.5-flash if 2.5 is not accessible
        if model != "gemini-1.5-flash":
            fallback_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            resp = requests.post(fallback_url, json=payload, timeout=40)
            
    if resp.status_code == 200:
        data = resp.json()
        candidates = data.get("candidates", [])
        if candidates and "content" in candidates[0]:
            parts = candidates[0]["content"].get("parts", [])
            if parts:
                return parts[0].get("text", "")
        return "Gemini API responded without text."
    else:
        raise Exception(f"Gemini API Error ({resp.status_code}): {resp.text}")


def get_agri_ai_response(
    messages: List[Dict[str, str]],
    provider: str = "local",
    api_key: Optional[str] = None,
    lang: str = "bn"
) -> str:
    """
    Main dispatch function: queries Groq, Gemini, or Local Expert
    """
    latest_query = messages[-1]["content"] if messages else ""
    
    # 1. Groq Provider
    if provider == "groq" and api_key and api_key.strip():
        try:
            return query_groq_api(api_key.strip(), messages)
        except Exception as e:
            fallback = generate_local_expert_response(latest_query, lang=lang)
            err_msg = f"*(Groq API সংযোগে ত্রুটি: {str(e)}। নিচে স্মার্ট অফলাইন কৃষি ইঞ্জিনের উত্তর দেওয়া হলো)*\n\n" if lang == "bn" else f"*(Groq API Error: {str(e)}. Fallback to Offline Engine)*\n\n"
            return err_msg + fallback

    # 2. Gemini Provider
    elif provider == "gemini" and api_key and api_key.strip():
        try:
            return query_gemini_api(api_key.strip(), messages)
        except Exception as e:
            fallback = generate_local_expert_response(latest_query, lang=lang)
            err_msg = f"*(Gemini API সংযোগে ত্রুটি: {str(e)}। নিচে স্মার্ট অফলাইন কৃষি ইঞ্জিনের উত্তর দেওয়া হলো)*\n\n" if lang == "bn" else f"*(Gemini API Error: {str(e)}. Fallback to Offline Engine)*\n\n"
            return err_msg + fallback

    # 3. Built-in Local Expert Engine (Zero API Key needed)
    else:
        return generate_local_expert_response(latest_query, lang=lang)
