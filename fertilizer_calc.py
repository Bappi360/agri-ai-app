"""
Fertilizer Calculator (স্মার্ট সার ক্যালকুলেটর)
Scientific fertilizer recommendation according to BARC (Bangladesh Agricultural Research Council)
and standard agronomical guidelines.
"""

# Unit conversions relative to 1 Decimal (শতক)
UNIT_CONVERSION_TO_DECIMAL = {
    "decimal": 1.0,      # শতক
    "katha": 1.65,       # কাঠা (২০ কাঠা = ১ বিঘা)
    "bigha": 33.0,       # বিঘা (৩৩ শতক)
    "acre": 100.0,       # একর (১০০ শতক)
    "hectare": 247.1     # হেক্টর (২৪৭.১ শতক)
}

# Standard rate in kg per decimal (শতক) for key crops
FERTILIZER_RATES_PER_DECIMAL = {
    "boro_rice": {
        "name_bn": "বোরো ধান (Boro Rice)",
        "name_en": "Boro Rice",
        "urea": 1.15,
        "tsp": 0.45,
        "mop": 0.60,
        "gypsum": 0.45,
        "zinc": 0.045,
        "boron": 0.0,
        "cowdung": 25.0,
        "schedule_bn": [
            "১ম কিস্তি: জমি তৈরির শেষ চাষের সময় সব টিএসপি, এমওপি, জিপসাম, দস্তা ও গোবর মাটির সাথে ভালো করে মিশিয়ে দিন।",
            "২য় কিস্তি: চারা রোপণের ১৫-২০ দিন পর (কুশি গজানোর শুরুতে) ইউরিয়া সারের এক-তৃতীয়াংশ (১/৩ অংশ) উপরিপ্রয়োগ করুন।",
            "৩য় কিস্তি: চারা রোপণের ৩৫-৪০ দিন পর (সর্বোচ্চ কুশি অবস্থায়) ইউরিয়া সারের আরও এক-তৃতীয়াংশ দিন।",
            "৪র্থ কিস্তি: কাইচ থোড় আসার ৫-৭ দিন আগে বাকি এক-তৃতীয়াংশ ইউরিয়া উপরিপ্রয়োগ করুন।"
        ],
        "schedule_en": [
            "1st Split (Basal): Apply all TSP, MOP, Gypsum, Zinc, and Cowdung during final land preparation.",
            "2nd Split: Top-dress 1/3 of Urea 15-20 days after transplanting (early tillering).",
            "3rd Split: Top-dress 1/3 of Urea 35-40 days after transplanting (active tillering).",
            "4th Split: Top-dress remaining 1/3 of Urea 5-7 days before panicle initiation."
        ]
    },
    "aman_rice": {
        "name_bn": "আমন ধান (Aman Rice)",
        "name_en": "Aman Rice",
        "urea": 0.85,
        "tsp": 0.35,
        "mop": 0.45,
        "gypsum": 0.30,
        "zinc": 0.035,
        "boron": 0.0,
        "cowdung": 20.0,
        "schedule_bn": [
            "শেষ চাষে: সমুদয় টিএসপি, এমওপি, জিপসাম ও জিংক মাটিতে প্রয়োগ করুন।",
            "ইউরিয়া প্রয়োগ: ইউরিয়া সার সমান ৩ কিস্তিতে (রোপণের ১৪ দিন পর, ৩০ দিন পর এবং থোড় আসার আগে) উপরিপ্রয়োগ করুন।"
        ],
        "schedule_en": [
            "Basal dose: All TSP, MOP, Gypsum, and Zinc at final plowing.",
            "Urea top-dressing: Apply Urea in 3 equal splits (14 DAT, 30 DAT, and 5-7 days before boot stage)."
        ]
    },
    "potato": {
        "name_bn": "আলু (Potato)",
        "name_en": "Potato",
        "urea": 1.10,
        "tsp": 0.75,
        "mop": 1.10,
        "gypsum": 0.45,
        "zinc": 0.045,
        "boron": 0.045,
        "cowdung": 30.0,
        "schedule_bn": [
            "জমি প্রস্তুতিতে: গোবর, টিএসপি, জিপসাম, দস্তা, বোরন এবং অর্ধেক ইউরিয়া ও অর্ধেক এমওপি শেষ চাষের সময় মাটিতে মিশিয়ে দিন।",
            "উপরিপ্রয়োগ (৩০-৩৫ দিন পর): চারা বের হওয়ার ৩০-৩৫ দিন পর গাছের গোড়ায় মাটি তোলার (Earthing up) সময় বাকি অর্ধেক ইউরিয়া ও অর্ধেক এমওপি ছিটিয়ে মাটি তুলে সেচ দিন।"
        ],
        "schedule_en": [
            "Basal dose: Incorporate all Cowdung, TSP, Gypsum, Zinc, Boron, half of Urea, and half of MOP during final soil prep.",
            "Top-dressing (30-35 days): Apply remaining half Urea and MOP alongside furrows during earthing-up, followed by light irrigation."
        ]
    },
    "wheat": {
        "name_bn": "গম (Wheat)",
        "name_en": "Wheat",
        "urea": 1.05,
        "tsp": 0.60,
        "mop": 0.45,
        "gypsum": 0.45,
        "zinc": 0.035,
        "boron": 0.035,
        "cowdung": 20.0,
        "schedule_bn": [
            "শেষ চাষে: দুই-তৃতীয়াংশ ইউরিয়া এবং সমুদয় টিএসপি, এমওপি, জিপসাম ও বোরন মাটিতে দিন।",
            "১ম সেচের সময়: বীজ বপনের ২০-২১ দিন পর ১ম সেচের (মুকুট শিকড় পর্যায়) সময় বাকি এক-তৃতীয়াংশ ইউরিয়া উপরিপ্রয়োগ করুন।"
        ],
        "schedule_en": [
            "Basal: 2/3rd of Urea, and all TSP, MOP, Gypsum, and Boron at final land preparation.",
            "Top-dress: Remaining 1/3rd Urea at first irrigation (CRI stage, 20-21 days after sowing)."
        ]
    },
    "maize": {
        "name_bn": "ভুট্টা (Maize / Corn)",
        "name_en": "Maize / Corn",
        "urea": 2.00,
        "tsp": 1.05,
        "mop": 1.05,
        "gypsum": 0.90,
        "zinc": 0.08,
        "boron": 0.05,
        "cowdung": 35.0,
        "schedule_bn": [
            "শেষ চাষে: এক-তৃতীয়াংশ ইউরিয়া এবং সমুদয় টিএসপি, এমওপি, জিপসাম, জিংক ও বোরন প্রয়োগ করুন।",
            "১ম উপরিপ্রয়োগ: চারা গজানোর ২৫-৩০ দিন পর (৮-১০ পাতা অবস্থা) ১/৩ অংশ ইউরিয়া।",
            "২য় উপরিপ্রয়োগ: চারা গজানোর ৫০-৫৫ দিন পর (পুরুষ ফুল বা টাসেল আসার আগে) বাকি ১/৩ অংশ ইউরিয়া ও সেচ দিন।"
        ],
        "schedule_en": [
            "Basal: 1/3rd Urea and full dose of TSP, MOP, Gypsum, Zinc, Boron during final land preparation.",
            "1st Top-dress: 1/3rd Urea at knee-high stage (25-30 days).",
            "2nd Top-dress: Remaining 1/3rd Urea before tasseling (50-55 days) followed by watering."
        ]
    },
    "tomato": {
        "name_bn": "টমেটো (Tomato)",
        "name_en": "Tomato",
        "urea": 0.95,
        "tsp": 0.80,
        "mop": 0.80,
        "gypsum": 0.45,
        "zinc": 0.045,
        "boron": 0.045,
        "cowdung": 35.0,
        "schedule_bn": [
            "মাদায়/শেষ চাষে: সমস্ত গোবর, টিএসপি, জিপসাম, জিংক ও বোরন শেষ চাষে দিন।",
            "উপরিপ্রয়োগ: ইউরিয়া ও এমওপি সমান ৩ কিস্তিতে চারা রোপণের ১৫, ৩০ এবং ৪৫ দিন পর উপরিপ্রয়োগ করে সেচ দিন।"
        ],
        "schedule_en": [
            "Basal: All cowdung, TSP, Gypsum, Zinc, and Boron during pit/land preparation.",
            "Top-dressing: Split Urea and MOP into 3 equal doses at 15, 30, and 45 days after transplanting."
        ]
    },
    "mustard": {
        "name_bn": "সরিষা (Mustard)",
        "name_en": "Mustard",
        "urea": 1.05,
        "tsp": 0.75,
        "mop": 0.45,
        "gypsum": 0.60,
        "zinc": 0.03,
        "boron": 0.03,
        "cowdung": 20.0,
        "schedule_bn": [
            "শেষ চাষে: অর্ধেক ইউরিয়া এবং বাকি সব সার মাটিতে ভালোভাবে মিশিয়ে দিন।",
            "উপরিপ্রয়োগ: ফুল আসার আগে (বীজ বোনার ২৫-৩০ দিন পর) বাকি অর্ধেক ইউরিয়া উপরিপ্রয়োগ করে হালকা সেচ দিন।"
        ],
        "schedule_en": [
            "Basal: Half Urea and full dose of all other fertilizers at final plowing.",
            "Top-dress: Remaining half Urea before flowering (25-30 days after sowing) followed by light irrigation."
        ]
    },
    "eggplant": {
        "name_bn": "বেগুন (Brinjal)",
        "name_en": "Brinjal",
        "urea": 1.10,
        "tsp": 0.90,
        "mop": 0.75,
        "gypsum": 0.30,
        "zinc": 0.03,
        "boron": 0.03,
        "cowdung": 45.0,
        "schedule_bn": [
            "শেষ চাষে: গোবর, টিএসপি, জিপসাম ও জিংক মিশিয়ে দিন।",
            "উপরিপ্রয়োগ: ইউরিয়া ও এমওপি ৪টি সমান কিস্তিতে রোপণের ২০, ৪০, ৬০ ও ৮০ দিন পর গাছের গোড়া থেকে ৫-৬ ইঞ্চি দূরে প্রয়োগ করুন।"
        ],
        "schedule_en": [
            "Basal: All cowdung, TSP, gypsum, and zinc at bed preparation.",
            "Top-dress: Urea and MOP split into 4 equal doses at 20, 40, 60, and 80 days after transplanting (5-6 inches away from stem)."
        ]
    }
}


def calculate_fertilizer(crop_key: str, area: float, unit: str) -> dict:
    """
    Calculate fertilizer quantities for a given crop, land area, and unit.
    """
    if crop_key not in FERTILIZER_RATES_PER_DECIMAL:
        crop_key = "boro_rice"
        
    conversion_factor = UNIT_CONVERSION_TO_DECIMAL.get(unit, 1.0)
    total_decimals = area * conversion_factor
    
    rate = FERTILIZER_RATES_PER_DECIMAL[crop_key]
    
    results = {
        "crop_key": crop_key,
        "name_bn": rate["name_bn"],
        "name_en": rate["name_en"],
        "area": area,
        "unit": unit,
        "total_decimals": round(total_decimals, 2),
        "urea_kg": round(rate["urea"] * total_decimals, 2),
        "tsp_kg": round(rate["tsp"] * total_decimals, 2),
        "mop_kg": round(rate["mop"] * total_decimals, 2),
        "gypsum_kg": round(rate["gypsum"] * total_decimals, 2),
        "zinc_kg": round(rate["zinc"] * total_decimals, 2),
        "boron_kg": round(rate["boron"] * total_decimals, 2),
        "cowdung_kg": round(rate["cowdung"] * total_decimals, 1),
        "schedule_bn": rate["schedule_bn"],
        "schedule_en": rate["schedule_en"]
    }
    
    return results
