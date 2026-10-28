"""
AgriSathi AI - Agricultural AI Web Application (কৃষি সাথী এআই)
A comprehensive bilingual AI Assistant for Agriculture, Crops, Diseases, and Fertilizers.
"""

import os
import socket
import streamlit as st
from PIL import Image
from dotenv import load_dotenv, set_key

# Load environment variables
load_dotenv()

def get_local_ip():
    """Retrieve active local network IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        try:
            return socket.gethostbyname(socket.gethostname())
        except Exception:
            return "192.168.1.x"


# Internal modules
from config import TRANSLATIONS, APP_NAME_BN, APP_NAME_EN
from agri_ai_engine import get_agri_ai_response
from fertilizer_calc import calculate_fertilizer, FERTILIZER_RATES_PER_DECIMAL
from disease_diagnostics import diagnose_by_symptoms
from agri_knowledge_base import CROPS_DATA, ORGANIC_PESTICIDES, SEASONAL_CALENDAR

# ---------------------------------------------------------
# Streamlit Page Setup
# ---------------------------------------------------------
st.set_page_config(
    page_title="AgriSathi AI | কৃষি সাথী এআই",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Custom CSS
css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "bn"  # Default to Bengali

if "ai_provider" not in st.session_state:
    st.session_state.ai_provider = os.getenv("DEFAULT_AI_PROVIDER", "local")

if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = os.getenv("GROQ_API_KEY", "")

if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = os.getenv("GEMINI_API_KEY", "")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Quick Query Handler
if "preset_prompt" not in st.session_state:
    st.session_state.preset_prompt = None

# Current active translation dictionary
T = TRANSLATIONS[st.session_state.lang]

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🌾 কৃষি সাথী কন্ট্রোল প্যানেল")
    
    # 1. Language Toggle
    lang_choice = st.radio(
        label=T["language_select"],
        options=["🇧🇩 বাংলা", "🇬🇧 English"],
        index=0 if st.session_state.lang == "bn" else 1,
        horizontal=True
    )
    new_lang = "bn" if "বাংলা" in lang_choice else "en"
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()

    st.markdown("---")
    
    # 2. AI Engine Status
    st.markdown("#### ⚡ এআই ইঞ্জিন স্ট্যাটাস / AI Engine")
    provider = st.session_state.ai_provider
    if provider == "groq" and st.session_state.groq_api_key:
        st.success("⚡ Groq Llama-3.3-70B (সক্রিয় / Active)")
    elif provider == "gemini" and st.session_state.gemini_api_key:
        st.success("✨ Google Gemini 2.5 (সক্রিয় / Active)")
    else:
        st.info("🟢 অফলাইন এগ্রি এক্সপার্ট (Active - No Key Needed)")

    st.markdown("---")
    
    # 3. Mobile Connect Expander
    local_net_ip = get_local_ip()
    mobile_url = f"http://{local_net_ip}:8501"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={mobile_url}"
    
    with st.expander("📱 মোবাইলে চালান / Mobile Access", expanded=False):
        if st.session_state.lang == "bn":
            st.markdown(
                f"""
                **মোবাইলে যেভাবে ওপেন করবেন:**
                1. ফোন ও পিসি একই Wi-Fi বা Hotspot-এ রাখুন।
                2. ফোনের ব্রাউজারে লিংকটি লিখুন:
                """
            )
            st.code(mobile_url, language="text")
            st.markdown(f"<div style='text-align:center;'><img src='{qr_url}' width='130' style='border-radius:8px; margin:6px 0;'/><br><small>ক্যামেরা দিয়ে স্ক্যান করুন</small></div>", unsafe_allow_html=True)
        else:
            st.markdown(
                f"""
                **Open on Mobile Phone:**
                1. Connect phone & PC to same Wi-Fi / Hotspot.
                2. Open link in mobile browser:
                """
            )
            st.code(mobile_url, language="text")
            st.markdown(f"<div style='text-align:center;'><img src='{qr_url}' width='130' style='border-radius:8px; margin:6px 0;'/><br><small>Scan with phone camera</small></div>", unsafe_allow_html=True)

    st.markdown("---")
    
    # 4. Quick Farmer Helpline
    st.markdown("#### 📞 জরুরি কৃষি হেল্পলাইন")
    st.markdown(
        """
        - **কৃষি কল সেন্টার:** ☎️ `16123` (বিনামূল্যে যে কোনো সিম থেকে)
        - **মৌসুম:** 🌾 **রবি মৌসুম (Rabi Season)**
        - **সেবা:** ধান, গম, আলু, ভুট্টা, সবজি ও সার পরামর্শ
        """ if st.session_state.lang == "bn" else
        """
        - **Agri Call Center (BD):** ☎️ `16123` (Toll-free)
        - **Active Season:** 🌾 **Rabi Season**
        - **Scope:** Paddy, Potato, Wheat, Maize, Vegetables & Fertilizer Advisory
        """
    )
    
    st.markdown("---")
    st.caption("AgriSathi AI v1.0 • Made with ❤️ for modern smart agriculture")

# ---------------------------------------------------------
# Header Banner
# ---------------------------------------------------------
banner_title = "🌱 কৃষি সাথী এআই — ডিজিটাল কৃষি বিজ্ঞানী" if st.session_state.lang == "bn" else "🌱 AgriSathi AI — Smart Agriculture Assistant"
banner_desc = "কৃষকদের জন্য নির্ভরযোগ্য আধুনিক রোগ নির্ণয়, সার ক্যালকুলেটর ও এআই পরামর্শক" if st.session_state.lang == "bn" else "Intelligent Crop Health Diagnostics, Precise Fertilizer Formulation & Agricultural Advisory"

st.markdown(
    f"""
    <div class="agri-banner">
        <h1>{banner_title}</h1>
        <p>{banner_desc}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Main Navigation Tabs
# ---------------------------------------------------------
tab_chat, tab_disease, tab_fertilizer, tab_calendar, tab_settings = st.tabs([
    T["nav_chat"],
    T["nav_disease"],
    T["nav_fertilizer"],
    T["nav_calendar"],
    T["nav_settings"]
])

# =========================================================
# TAB 1: AI AGRI CHAT ASSISTANT (এআই কৃষি পরামর্শক)
# =========================================================
with tab_chat:
    st.subheader(T["chat_header"])
    
    # Clickable Suggestion Chips
    st.markdown(f"**{T['quick_questions_title']}**")
    cols = st.columns(3)
    for idx, query in enumerate(T["quick_queries"]):
        with cols[idx % 3]:
            if st.button(f"🌾 {query}", key=f"chip_{idx}", use_container_width=True):
                st.session_state.preset_prompt = query
                st.rerun()

    st.markdown("---")
    
    # Display Welcome Message if no history
    if not st.session_state.messages:
        with st.chat_message("assistant", avatar="🌱"):
            st.markdown(T["chat_welcome"])

    # Render previous messages
    for msg in st.session_state.messages:
        avatar = "👨‍🌾" if msg["role"] == "user" else "🌱"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    # Handle Preset or Direct Chat Input
    user_prompt = st.chat_input(placeholder=T["chat_placeholder"])
    
    if st.session_state.preset_prompt:
        user_prompt = st.session_state.preset_prompt
        st.session_state.preset_prompt = None

    if user_prompt:
        # Append User Message
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user", avatar="👨‍🌾"):
            st.markdown(user_prompt)

        # Generate AI Response
        active_key = ""
        if st.session_state.ai_provider == "groq":
            active_key = st.session_state.groq_api_key
        elif st.session_state.ai_provider == "gemini":
            active_key = st.session_state.gemini_api_key

        with st.chat_message("assistant", avatar="🌱"):
            with st.spinner("কৃষি তথ্য বিশ্লেষণ করা হচ্ছে..." if st.session_state.lang == "bn" else "Analyzing agricultural data..."):
                response_text = get_agri_ai_response(
                    messages=st.session_state.messages,
                    provider=st.session_state.ai_provider,
                    api_key=active_key,
                    lang=st.session_state.lang
                )
                st.markdown(response_text)

        # Append Assistant Response
        st.session_state.messages.append({"role": "assistant", "content": response_text})

    # Clear Chat Button
    if st.session_state.messages:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(T["clear_chat"], type="secondary"):
            st.session_state.messages = []
            st.rerun()


# =========================================================
# TAB 2: CROP DISEASE DIAGNOSTIC (রোগবালাই নির্ণয়)
# =========================================================
with tab_disease:
    st.subheader(T["disease_header"])
    st.write(T["disease_sub"])
    
    col_d1, col_d2 = st.columns([1, 1])
    
    with col_d1:
        crop_options_dict = T["crop_options"]
        selected_crop_key = st.selectbox(
            T["select_crop"],
            options=list(crop_options_dict.keys()),
            format_func=lambda x: crop_options_dict[x]
        )
        
        symptom_input = st.text_area(
            T["describe_symptoms"],
            placeholder=T["symptoms_placeholder"],
            height=110
        )
        
        uploaded_image = st.file_uploader(
            T["upload_leaf_photo"],
            type=["jpg", "jpeg", "png"]
        )
        
        diagnose_btn = st.button(T["btn_diagnose"], type="primary", use_container_width=True)

    with col_d2:
        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, caption="📸 আপলোডকৃত ফসলের ছবি" if st.session_state.lang == "bn" else "📸 Uploaded Crop Image", use_container_width=True)
            st.info("✅ ছবিটি সংরক্ষিত হয়েছে। লক্ষণ বিশ্লেষণের সাথে চিত্র পর্যালোচিত হবে।" if st.session_state.lang == "bn" else "✅ Image captured. Visual indicators will accompany symptom evaluation.")
        else:
            st.markdown(
                """
                <div class="agri-card">
                    <h4>💡 রোগ নির্ণয় সহজ করার টিপস:</h4>
                    <ul>
                        <li>পাতার দাগের আকৃতি ও রঙ (যেমন: বাদামি, ছাই রঙ, বাটি বা নৌকার আকৃতি) উল্লেখ করুন।</li>
                        <li>গাছের কোন অংশে আক্রমণ হয়েছে (ডগা, শিকড়, কাণ্ড, পাতা বা ফল) তা জানান।</li>
                        <li>লক্ষণ দেখা দিলে পরিষ্কার রৌদ্রোজ্জ্বল আলোতে পাতার স্পষ্ট ছবি তুলুন।</li>
                    </ul>
                </div>
                """ if st.session_state.lang == "bn" else
                """
                <div class="agri-card">
                    <h4>💡 Tips for Accurate Diagnosis:</h4>
                    <ul>
                        <li>Specify lesion color, margin patterns (e.g. concentric rings, spindle shape).</li>
                        <li>Identify the affected plant part (leaf, neck, stem base, foliage, or fruit).</li>
                        <li>Capture photos in good ambient daylight focusing closely on the diseased spot.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Perform Diagnosis
    if diagnose_btn:
        search_query = symptom_input.strip()
        if not search_query and uploaded_image:
            search_query = "leaf spot disease infection"
        elif not search_query:
            search_query = selected_crop_key
            
        diagnoses = diagnose_by_symptoms(selected_crop_key, search_query, lang=st.session_state.lang)
        
        st.markdown(f"### {T['diagnosis_result_title']}")
        if not diagnoses:
            st.warning("কোনো সুনির্দিষ্ট রোগ বা পোকা শনাক্ত করা যায়নি। আরও বিস্তারিত লক্ষণ লিখুন।" if st.session_state.lang == "bn" else "No exact match found. Please describe more detailed symptoms.")
        else:
            for item in diagnoses:
                data = item["data"]
                crop_data = item["crop"]
                is_bn = st.session_state.lang == "bn"
                
                name = data["name_bn"] if is_bn else data["name_en"]
                crop_name = crop_data["name_bn"] if is_bn else crop_data["name_en"]
                
                if item["type"] == "disease":
                    symptoms = data["symptoms_bn"] if is_bn else data["symptoms_en"]
                    chem_cure = data["chemical_cure_bn"] if is_bn else data["chemical_cure_en"]
                    org_cure = data["organic_cure_bn"] if is_bn else data["organic_cure_en"]
                    
                    st.markdown(
                        f"""
                        <div class="agri-card">
                            <span class="badge-amber">{crop_name}</span>
                            <h3 style="color:#1b4332; margin-top:8px;">🔬 {name}</h3>
                            <p><strong>{T['symptoms_label']}</strong> {symptoms}</p>
                            <div style="background-color:#f1f8e9; padding:10px 14px; border-radius:8px; margin:8px 0;">
                                <strong>{T['chemical_cure_label']}</strong><br>{chem_cure}
                            </div>
                            <div style="background-color:#e8f5e9; padding:10px 14px; border-radius:8px;">
                                <strong>{T['organic_cure_label']}</strong><br>{org_cure}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    # Pest
                    remedy = data["remedy_bn"] if is_bn else data["remedy_en"]
                    st.markdown(
                        f"""
                        <div class="agri-card">
                            <span class="badge-amber">{crop_name}</span>
                            <h3 style="color:#b91c1c; margin-top:8px;">🐛 {name}</h3>
                            <div style="background-color:#fff1f2; padding:12px; border-radius:8px;">
                                <strong>প্রতিকার ও দমন ব্যবস্থা:</strong><br>{remedy}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


# =========================================================
# TAB 3: PRECISION FERTILIZER CALCULATOR (সার ক্যালকুলেটর)
# =========================================================
with tab_fertilizer:
    st.subheader(T["fertilizer_header"])
    st.write(T["fertilizer_sub"])
    
    c_f1, c_f2, c_f3 = st.columns([1.5, 1, 1])
    
    with c_f1:
        crop_keys = list(FERTILIZER_RATES_PER_DECIMAL.keys())
        selected_fert_crop = st.selectbox(
            T["select_fert_crop"],
            options=crop_keys,
            format_func=lambda k: FERTILIZER_RATES_PER_DECIMAL[k]["name_bn"] if st.session_state.lang == "bn" else FERTILIZER_RATES_PER_DECIMAL[k]["name_en"]
        )
        
    with c_f2:
        land_size = st.number_input(T["land_area"], min_value=0.1, value=33.0, step=1.0)
        
    with c_f3:
        units_dict = T["units"]
        selected_unit = st.selectbox(
            T["unit_select"],
            options=list(units_dict.keys()),
            format_func=lambda u: units_dict[u]
        )

    calc_btn = st.button(T["btn_calculate"], type="primary", use_container_width=True)
    
    if calc_btn or land_size:
        fert_res = calculate_fertilizer(selected_fert_crop, land_size, selected_unit)
        is_bn = st.session_state.lang == "bn"
        crop_title = fert_res["name_bn"] if is_bn else fert_res["name_en"]
        
        st.markdown(f"### {T['calc_result_header']} — {crop_title} ({land_size} {units_dict[selected_unit]} / {fert_res['total_decimals']} শতক)")
        
        m_col1, m_col2, m_col3, m_col4, m_col5, m_col6 = st.columns(6)
        
        with m_col1:
            st.markdown(
                f"""
                <div class="fert-metric-box">
                    <div class="fert-metric-label">ইউরিয়া (Urea)</div>
                    <div class="fert-metric-val">{fert_res['urea_kg']} <span style="font-size:1rem;">কেজি</span></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m_col2:
            st.markdown(
                f"""
                <div class="fert-metric-box">
                    <div class="fert-metric-label">টিএসপি/ডিএপি (TSP)</div>
                    <div class="fert-metric-val">{fert_res['tsp_kg']} <span style="font-size:1rem;">কেজি</span></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m_col3:
            st.markdown(
                f"""
                <div class="fert-metric-box">
                    <div class="fert-metric-label">এমওপি/পটাশ (MOP)</div>
                    <div class="fert-metric-val">{fert_res['mop_kg']} <span style="font-size:1rem;">কেজি</span></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m_col4:
            st.markdown(
                f"""
                <div class="fert-metric-box">
                    <div class="fert-metric-label">জিপসাম (Gypsum)</div>
                    <div class="fert-metric-val">{fert_res['gypsum_kg']} <span style="font-size:1rem;">কেজি</span></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m_col5:
            st.markdown(
                f"""
                <div class="fert-metric-box">
                    <div class="fert-metric-label">দস্তা (Zinc)</div>
                    <div class="fert-metric-val">{fert_res['zinc_kg']} <span style="font-size:1rem;">কেজি</span></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with m_col6:
            st.markdown(
                f"""
                <div class="fert-metric-box">
                    <div class="fert-metric-label">জৈব সার/গোবর</div>
                    <div class="fert-metric-val">{fert_res['cowdung_kg']} <span style="font-size:1rem;">কেজি</span></div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Application Schedule
        st.markdown(f"#### {T['schedule_header']}")
        schedule = fert_res["schedule_bn"] if is_bn else fert_res["schedule_en"]
        for step in schedule:
            st.markdown(f"- 🕒 {step}")


# =========================================================
# TAB 4: CROP CALENDAR & ORGANIC FARMING (ক্যালেন্ডার ও জৈব)
# =========================================================
with tab_calendar:
    st.subheader(T["calendar_header"])
    st.write(T["calendar_sub"])
    
    cal_col1, cal_col2 = st.columns([1.3, 1])
    
    with cal_col1:
        is_bn = st.session_state.lang == "bn"
        for season_key, season in SEASONAL_CALENDAR.items():
            s_title = season["season_bn"] if is_bn else season["season_en"]
            s_weather = season["weather_bn"] if is_bn else season["weather_en"]
            crops_list = ", ".join(season["major_crops_bn"] if is_bn else season["major_crops_en"])
            
            st.markdown(
                f"""
                <div class="agri-card">
                    <h4>🌾 {s_title}</h4>
                    <p><strong>{'আবহাওয়া বৈশিষ্ট্য' if is_bn else 'Weather'}:</strong> {s_weather}</p>
                    <p><strong>{'প্রধান ফসলসমূহ' if is_bn else 'Key Crops'}:</strong> <span style="color:#2d6a4f; font-weight:600;">{crops_list}</span></p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    with cal_col2:
        st.markdown(f"### {'🌿 নিরাপদ জৈব বালাইনাশক রেসিপি' if is_bn else '🌿 Natural Organic Remedies'}")
        for p_key, pest_data in ORGANIC_PESTICIDES.items():
            p_title = pest_data["title_bn"] if is_bn else pest_data["title_en"]
            p_desc = pest_data["usage_bn"] if is_bn else pest_data["usage_en"]
            st.markdown(
                f"""
                <div class="agri-card" style="border-left: 4px solid #52b788;">
                    <h4 style="color:#2d6a4f;">✅ {p_title}</h4>
                    <p style="font-size:0.95rem; line-height:1.5;">{p_desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# TAB 5: AI ENGINE SETTINGS & API CONFIGURATION
# =========================================================
with tab_settings:
    st.subheader(T["settings_header"])
    st.write(T["settings_desc"])
    
    prov_choice = st.radio(
        T["provider_select"],
        options=["local", "groq", "gemini"],
        format_func=lambda x: {
            "local": T["provider_local"],
            "groq": T["provider_groq"],
            "gemini": T["provider_gemini"]
        }[x],
        index=["local", "groq", "gemini"].index(st.session_state.ai_provider)
    )
    
    if prov_choice != st.session_state.ai_provider:
        st.session_state.ai_provider = prov_choice
        st.rerun()

    st.markdown("---")
    
    if prov_choice == "local":
        st.success(
            "🟢 **অফলাইন মোড সক্রিয়!** এই মোডে কোনো API Key ছাড়াই অ্যাপটি কাজ করবে। এতে ধান, গম, আলু, টমেটো, বেগুন সহ প্রধান ফসলের রোগবালাই, সার ব্যবস্থাপনা ও ক্যালেন্ডারের তথ্য সরাসরি বিল্ট-ইন ডেটাবেস থেকে সরবরাহ করা হয়।"
            if st.session_state.lang == "bn" else
            "🟢 **Offline Mode Active!** No API key needed. AgriSathi AI serves verified agronomical guidance, disease remedies, and fertilizer formulations directly from the built-in research knowledge base."
        )
        
    elif prov_choice == "groq":
        st.info(T["groq_free_guide"])
        groq_input = st.text_input(
            "Groq API Key (gsk_...):",
            value=st.session_state.groq_api_key,
            type="password",
            help=T["api_key_help"]
        )
        if st.button(T["btn_save_key"], key="save_groq"):
            st.session_state.groq_api_key = groq_input.strip()
            # Save into local .env for persistence
            env_file = os.path.join(os.path.dirname(__file__), ".env")
            set_key(env_file, "GROQ_API_KEY", groq_input.strip())
            set_key(env_file, "DEFAULT_AI_PROVIDER", "groq")
            st.success("✅ Groq API Key সফলভাবে সংরক্ষিত হয়েছে!" if st.session_state.lang == "bn" else "✅ Groq API Key saved successfully!")
            st.rerun()

    elif prov_choice == "gemini":
        st.info(T["gemini_free_guide"])
        gemini_input = st.text_input(
            "Google Gemini API Key (AIzaSy...):",
            value=st.session_state.gemini_api_key,
            type="password",
            help=T["api_key_help"]
        )
        if st.button(T["btn_save_key"], key="save_gemini"):
            st.session_state.gemini_api_key = gemini_input.strip()
            # Save into local .env for persistence
            env_file = os.path.join(os.path.dirname(__file__), ".env")
            set_key(env_file, "GEMINI_API_KEY", gemini_input.strip())
            set_key(env_file, "DEFAULT_AI_PROVIDER", "gemini")
            st.success("✅ Gemini API Key সফলভাবে সংরক্ষিত হয়েছে!" if st.session_state.lang == "bn" else "✅ Gemini API Key saved successfully!")
            st.rerun()

    st.markdown("---")
    st.markdown("#### 📁 পরিবেশ ও ফাইল অবস্থান (Environment & Storage)")
    st.code(f"App Directory: {os.path.abspath(os.path.dirname(__file__))}\nEnvironment Config: .env", language="text")
