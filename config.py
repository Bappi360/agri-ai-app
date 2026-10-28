"""
Configuration and Bilingual UI Strings (বাংলা & English)
"""

APP_NAME_BN = "কৃষি সাথী এআই (AgriSathi AI)"
APP_NAME_EN = "AgriSathi AI - Smart Agriculture Assistant"
APP_TAGLINE_BN = "কৃষকের বিশ্বস্ত ডিজিটাল কৃষি বিজ্ঞানী ও আধুনিক চাষাবাদ পরামর্শক"
APP_TAGLINE_EN = "Your Trusted AI Agricultural Scientist & Modern Farming Advisor"

TRANSLATIONS = {
    "bn": {
        "app_title": "🌱 কৃষি সাথী এআই (AgriSathi AI)",
        "tagline": "কৃষকের বিশ্বস্ত ডিজিটাল কৃষি বিজ্ঞানী ও চাষাবাদ পরামর্শক 🌾",
        "language_select": "ভাষা নির্বাচন / Language:",
        "nav_chat": "💬 এআই কৃষি পরামর্শক",
        "nav_disease": "🔍 রোগবালাই নির্ণয় ও প্রতিকার",
        "nav_fertilizer": "⚖️ স্মার্ট সার ক্যালকুলেটর",
        "nav_calendar": "📅 মৌসুমি ফসল ক্যালেন্ডার",
        "nav_settings": "⚙️ এআই সেটিংস ও এপিআই",
        
        # Chat tab
        "chat_header": "🌾 আপনার ফসল বা কৃষিকাজ নিয়ে যে কোনো প্রশ্ন করুন",
        "chat_placeholder": "উদাহরণ: ধানের পাতা হলুদ হয়ে যাচ্ছে কি করব? অথবা ইউরিয়ার সঠিক মাত্রা কত?",
        "chat_welcome": "নমস্কার/সালাম! আমি **কৃষি সাথী এআই**। আপনার ধান, আলু, গম, ভুট্টা, সবজি বা যেকোনো ফসলের রোগ, সার, সেচ বা চাষাবাদ নিয়ে প্রশ্ন করুন। আমি এখনই সমাধান দিচ্ছি!",
        "quick_questions_title": "💡 দ্রুত প্রশ্নসমূহ (ক্লিক করুন):",
        "quick_queries": [
            "ধানের ব্লাস্ট ও পাতাপোড়া রোগের সমাধান কি?",
            "আলুর নাবি ধসা (Late Blight) রোগের লক্ষণ ও ওষুধ",
            "টমেটোর পাতা কুঁকড়ে যাওয়া ও ফুল ঝরা রোধের উপায়",
            "বিঘাপ্রতি বোরো ধানের জন্য কোন সার কতটুকু দিতে হয়?",
            "বেগুনের ডগা ও ফল ছিদ্রকারী পোকা দমনের উপায়",
            "ঘরোয়া উপায়ে নিম তেলের কীটনাশক তৈরির নিয়ম"
        ],
        "clear_chat": "🗑️ কথোপকথন মুছে ফেলুন",
        
        # Disease Diagnostic tab
        "disease_header": "🔍 ফসলের রোগ ও ক্ষতিকর পোকা নির্ণয়",
        "disease_sub": "আপনার ফসলের ধরন নির্বাচন করুন এবং দৃশ্যমান লক্ষণ বা পাতা/গাছের ছবি আপলোড করুন।",
        "select_crop": "ফসল নির্বাচন করুন:",
        "crop_options": {
            "all": "সব ফসল / সাধারণ খোঁজ",
            "rice": "ধান (Rice)",
            "potato": "আলু (Potato)",
            "tomato": "টমেটো (Tomato)",
            "wheat": "গম (Wheat)",
            "eggplant": "বেগুন (Brinjal)",
            "mustard": "সরিষা (Mustard)",
            "maize": "ভুট্টা (Maize)"
        },
        "describe_symptoms": "পাতায় বা গাছে কি লক্ষণ দেখছেন তা লিখুন:",
        "symptoms_placeholder": "যেমন: পাতায় চোখের মত দাগ, নিচের পাতা শুকিয়ে যাচ্ছে, ডগায় ছিদ্র ইত্যাদি...",
        "upload_leaf_photo": "📸 গাছের পাতার ছবি আপলোড করুন (ঐচ্ছিক):",
        "btn_diagnose": "🔎 রোগ বালাই নির্ণয় করুন",
        "diagnosis_result_title": "📋 রোগ নির্ণয় ফলাফল ও চিকিৎসা পরামর্শ",
        "symptoms_label": "লক্ষণসমূহ:",
        "chemical_cure_label": "🧪 রাসায়নিক সমাধান ও ডোজ:",
        "organic_cure_label": "🌿 জৈব ও প্রতিরোধমূলক ব্যবস্থা:",
        
        # Fertilizer tab
        "fertilizer_header": "⚖️ বিজ্ঞানসম্মত সার ক্যালকুলেটর",
        "fertilizer_sub": "বাংলাদেশ কৃষি গবেষণা কাউন্সিল (BARC) অনুমোদিত মাত্রায় আপনার জমির জন্য সারের সঠিক পরিমাণ হিসাব করুন।",
        "select_fert_crop": "ফসলের ধরন বেছে নিন:",
        "land_area": "জমির পরিমাণ লিখুন:",
        "unit_select": "জমির একক:",
        "units": {
            "decimal": "শতক (Decimal)",
            "katha": "কাঠা (Katha - ১.৬৫ শতক)",
            "bigha": "বিঘা (Bigha - ৩৩ শতক)",
            "acre": "একর (Acre - ১০০ শতক)",
            "hectare": "হেক্টর (Hectare - ২৪৭ শতক)"
        },
        "btn_calculate": "🧮 সার হিসাব করুন",
        "calc_result_header": "📊 আপনার জমির জন্য মোট সারের তালিকা:",
        "schedule_header": "⏰ সার প্রয়োগের সময়সূচি ও কিস্তি:",
        
        # Calendar tab
        "calendar_header": "📅 বাংলাদেশের তিন মৌসুমের ফসল ও নির্দেশিকা",
        "calendar_sub": "কোন মৌসুমে কোন ফসল সবচেয়ে বেশি লাভজনক ও উপযোগী তা জানুন।",
        
        # Settings tab
        "settings_header": "⚙️ এআই ইঞ্জিন ও এপিআই কনফিগারেশন",
        "settings_desc": "AgriSathi AI তিনটি শক্তিশালী মোডে কাজ করতে পারে। আপনার পছন্দমতো মোড নির্বাচন করুন।",
        "provider_select": "এআই ইঞ্জিন প্রোভাইডার নির্বাচন করুন:",
        "provider_local": "🟢 বিল্ট-ইন এগ্রি এক্সপার্ট (সম্পূর্ণ ফ্রি, কোনো API Key লাগবে না)",
        "provider_groq": "⚡ Groq Cloud (Llama 3.3 70B - সুপার ফাস্ট ও নিখুঁত)",
        "provider_gemini": "✨ Google Gemini API (Gemini 2.5/1.5 Flash)",
        "api_key_label": "আপনার API Key লিখুন:",
        "api_key_help": "আপনার কি নিরাপদে সংরক্ষিত থাকবে এবং ব্রাউজার সেশনে ব্যবহার হবে।",
        "btn_save_key": "💾 সেটিংস সংরক্ষণ করুন",
        "groq_free_guide": "👉 **Groq API Key একদম ফ্রি!** [console.groq.com/keys](https://console.groq.com/keys) এ গিয়ে ১ মিনিটে বিনামূল্যে কি তৈরি করুন।",
        "gemini_free_guide": "👉 **Gemini API Key একদম ফ্রি!** [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) এ গিয়ে ১ ক্লিকে বিনামূল্যে কি নিন।"
    },
    
    "en": {
        "app_title": "🌱 AgriSathi AI - Agricultural Assistant",
        "tagline": "Empowering Farmers & Agronomists with Intelligent AI Guidance 🌾",
        "language_select": "Language / ভাষা নির্বাচন:",
        "nav_chat": "💬 AI Agri Chat Assistant",
        "nav_disease": "🔍 Disease & Pest Diagnostic",
        "nav_fertilizer": "⚖️ Smart Fertilizer Calculator",
        "nav_calendar": "📅 Seasonal Crop Calendar",
        "nav_settings": "⚙️ AI Engine Settings",
        
        # Chat tab
        "chat_header": "🌾 Ask Any Agricultural or Crop Question",
        "chat_placeholder": "Example: Rice blast disease cure, or NPK fertilizer dose for potato per bigha...",
        "chat_welcome": "Hello! I am **AgriSathi AI**. Ask me anything about crop cultivation, soil health, fertilizer scheduling, disease management, and pest control. Let's make farming smarter!",
        "quick_questions_title": "💡 Suggested Questions (Click to ask):",
        "quick_queries": [
            "How to treat Rice Blast and Bacterial Blight?",
            "Symptoms and chemical treatment for Potato Late Blight",
            "How to control Tomato Leaf Curl Virus & Whiteflies?",
            "Fertilizer dose and schedule for Boro Rice per Bigha",
            "Brinjal Fruit & Shoot Borer organic and chemical control",
            "How to prepare homemade organic neem pesticide spray?"
        ],
        "clear_chat": "🗑️ Clear Chat History",
        
        # Disease Diagnostic tab
        "disease_header": "🔍 Crop Disease & Pest Diagnostic",
        "disease_sub": "Select your crop, describe symptoms, or upload leaf images for instant agricultural remedies.",
        "select_crop": "Select Crop:",
        "crop_options": {
            "all": "All Crops / General Search",
            "rice": "Rice / Paddy",
            "potato": "Potato",
            "tomato": "Tomato",
            "wheat": "Wheat",
            "eggplant": "Brinjal / Eggplant",
            "mustard": "Mustard",
            "maize": "Maize / Corn"
        },
        "describe_symptoms": "Describe visible symptoms on leaf or plant:",
        "symptoms_placeholder": "e.g., Eye-shaped spots on leaves, drying tips, rotting fruit, wilting stem...",
        "upload_leaf_photo": "📸 Upload Crop/Leaf Photo (Optional):",
        "btn_diagnose": "🔎 Diagnose Disease",
        "diagnosis_result_title": "📋 Diagnostic Findings & Recommendation",
        "symptoms_label": "Symptoms:",
        "chemical_cure_label": "🧪 Chemical Treatment & Dosages:",
        "organic_cure_label": "🌿 Organic & Agronomic Practices:",
        
        # Fertilizer tab
        "fertilizer_header": "⚖️ Precision Fertilizer Calculator",
        "fertilizer_sub": "Calculate balanced fertilizer requirements based on official agricultural research recommendations.",
        "select_fert_crop": "Choose Crop:",
        "land_area": "Enter Land Size:",
        "unit_select": "Land Unit:",
        "units": {
            "decimal": "Decimal (শতক)",
            "katha": "Katha (1.65 decimals)",
            "bigha": "Bigha (33 decimals)",
            "acre": "Acre (100 decimals)",
            "hectare": "Hectare (247 decimals)"
        },
        "btn_calculate": "🧮 Compute Fertilizers",
        "calc_result_header": "📊 Recommended Fertilizer Quantities:",
        "schedule_header": "⏰ Application Timing & Split Schedule:",
        
        # Calendar tab
        "calendar_header": "📅 Subcontinental Agricultural Seasons & Crops",
        "calendar_sub": "Optimal planting windows, climate conditions, and high-yielding crop recommendations.",
        
        # Settings tab
        "settings_header": "⚙️ AI Engine & API Configuration",
        "settings_desc": "AgriSathi AI supports three versatile execution modes. Select your preferred engine below.",
        "provider_select": "Select AI Engine Provider:",
        "provider_local": "🟢 Built-in Agri Expert (100% Free, No API Key Required)",
        "provider_groq": "⚡ Groq Cloud (Llama 3.3 70B - Lightning Fast & High Accuracy)",
        "provider_gemini": "✨ Google Gemini API (Gemini 2.5/1.5 Flash)",
        "api_key_label": "Enter your API Key:",
        "api_key_help": "Your key is stored securely in your browser session or local .env.",
        "btn_save_key": "💾 Save Settings",
        "groq_free_guide": "👉 **Get Free Groq API Key:** Visit [console.groq.com/keys](https://console.groq.com/keys) to get a free key in under a minute.",
        "gemini_free_guide": "👉 **Get Free Gemini API Key:** Visit [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) to generate a free key."
    }
}
