"""
Crop Disease Diagnostics Engine (উদ্ভিদ রোগ ও বালাই নির্ণয় ইঞ্জিন)
Provides symptom matching, pest identification, and visual diagnostic guidance.
"""

from agri_knowledge_base import CROPS_DATA

DISEASE_SYMPTOM_PATTERNS = [
    {
        "keywords": ["ব্লাস্ট", "blast", "নৌকা", "চোখের মত", "spindle", "গলা পচা", "চিটা"],
        "crop": "rice",
        "disease_id": "rice_blast"
    },
    {
        "keywords": ["পাতাপোড়া", "leaf blight", "ঢেউ খেলানো", "bacterial leaf blight", "ডগা শুকিয়ে"],
        "crop": "rice",
        "disease_id": "bacterial_leaf_blight"
    },
    {
        "keywords": ["খোলপোড়া", "sheath blight", "সাপের খোলস", "পানির ওপর দাগ", "খোসা"],
        "crop": "rice",
        "disease_id": "sheath_blight"
    },
    {
        "keywords": ["নাবি ধসা", "লেট ব্লাইট", "late blight", "কুয়াশা", "কালো দাগ", "পচে যাওয়া", "আলু পচা"],
        "crop": "potato",
        "disease_id": "potato_late_blight"
    },
    {
        "keywords": ["দাদ", "খোসপাঁচড়া", "scab", "আলুর চামড়ায় দাগ"],
        "crop": "potato",
        "disease_id": "potato_scab"
    },
    {
        "keywords": ["কুঁকড়ে", "কোঁকড়ানো", "curl", "leaf curl", "সাদা মাছি", "টমেটো পাতা ছোট"],
        "crop": "tomato",
        "disease_id": "tomato_leaf_curl"
    },
    {
        "keywords": ["ব্লসম", "তল পচা", "নিচের অংশ কালো", "blossom end rot", "ক্যালসিয়াম"],
        "crop": "tomato",
        "disease_id": "blossom_end_rot"
    },
    {
        "keywords": ["ঢলে পড়া", "wilt", "ঝিমিয়ে", "bacterial wilt", "বেগুন গাছ মরে যাওয়া"],
        "crop": "eggplant",
        "disease_id": "bacterial_wilt"
    },
    {
        "keywords": ["অল্টারনারিয়া", "alternaria", "সরিষার পাতা দাগ", "কালো দাগ"],
        "crop": "mustard",
        "disease_id": "mustard_alternaria_blight"
    },
    {
        "keywords": ["মাজরা", "stem borer", "মরা ডিগ", "সাদা শীষ", "গাছের কাণ্ডে ছিদ্র"],
        "crop": "rice",
        "pest_name_bn": "মাজরা পোকা"
    },
    {
        "keywords": ["কারেন্ট পোকা", "বাদামি গাছফড়িং", "bph", "হপার বার্ন", "গাছ পুড়ে যাওয়া"],
        "crop": "rice",
        "pest_name_bn": "বাদামি গাছফড়িং / কারেন্ট পোকা"
    },
    {
        "keywords": ["ডগা ও ফল ছিদ্রকারী", "borer", "বেগুন পোকা", "ফল পচা পোকা"],
        "crop": "eggplant",
        "pest_name_bn": "ডগা ও ফল ছিদ্রকারী পোকা"
    },
    {
        "keywords": ["ফল আর্মিওয়ার্ম", "armyworm", "ভুট্টার পোকা", "কুঁড়ি খাওয়া পোকা"],
        "crop": "maize",
        "pest_name_bn": "ফল আর্মিওয়ার্ম (FAW)"
    }
]


def diagnose_by_symptoms(crop_key: str, symptom_text: str, lang: str = "bn") -> list:
    """
    Diagnose possible diseases or pests matching user query or symptoms.
    """
    results = []
    text_lower = symptom_text.lower()
    
    # 1. First check crop-specific diseases
    if crop_key in CROPS_DATA:
        crop_info = CROPS_DATA[crop_key]
        for disease in crop_info.get("diseases", []):
            name = (disease["name_bn"] + " " + disease["name_en"]).lower()
            symptom_desc = (disease["symptoms_bn"] + " " + disease["symptoms_en"]).lower()
            if any(term in text_lower for term in [w for w in text_lower.split() if len(w) > 2]):
                if any(k in text_lower for k in disease["name_bn"].lower().split()) or any(k in symptom_desc for k in text_lower.split()):
                    results.append({"type": "disease", "data": disease, "crop": crop_info})
                    
        for pest in crop_info.get("pests", []):
            name = (pest["name_bn"] + " " + pest["name_en"]).lower()
            if any(k in text_lower for k in name.split()):
                results.append({"type": "pest", "data": pest, "crop": crop_info})
                
    # 2. Check pattern map
    for pattern in DISEASE_SYMPTOM_PATTERNS:
        if pattern["crop"] == crop_key or crop_key == "all":
            if any(kw in text_lower for kw in pattern["keywords"]):
                matched_crop = CROPS_DATA.get(pattern["crop"])
                if not matched_crop:
                    continue
                if "disease_id" in pattern:
                    for d in matched_crop.get("diseases", []):
                        if d["id"] == pattern["disease_id"] and not any(r["data"].get("id") == d["id"] for r in results):
                            results.append({"type": "disease", "data": d, "crop": matched_crop})
                elif "pest_name_bn" in pattern:
                    for p in matched_crop.get("pests", []):
                        if p["name_bn"] == pattern["pest_name_bn"] and not any(r["data"].get("name_bn") == p["name_bn"] for r in results):
                            results.append({"type": "pest", "data": p, "crop": matched_crop})
                            
    # 3. If still empty, return top common diseases of that crop
    if not results and crop_key in CROPS_DATA:
        crop_info = CROPS_DATA[crop_key]
        for d in crop_info.get("diseases", [])[:2]:
            results.append({"type": "disease", "data": d, "crop": crop_info})
            
    return results
