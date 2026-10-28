"""
Agri Knowledge Base (কৃষি তথ্যভাণ্ডার)
Comprehensive knowledge base for Bangladesh & Global Agriculture
Supports both Bengali and English.
"""

CROPS_DATA = {
    "rice": {
        "name_bn": "ধান (Rice/Paddy)",
        "name_en": "Rice / Paddy",
        "category_bn": "দানা জাতীয় ফসল",
        "category_en": "Cereal Crop",
        "seasons_bn": "আউশ (মার্চ-আগস্ট), আমন (জুন-ডিসেম্বর), বোরো (নভেম্বর-মে)",
        "seasons_en": "Aus (Mar-Aug), Aman (Jun-Dec), Boro (Nov-May)",
        "soil_bn": "উর্বর এঁটেল ও দোআঁশ মাটি, যেখানে পানি ধারণক্ষমতা ভালো। মাটির পিএইচ (pH) ৫.৫ থেকে ৬.৫ উত্তম।",
        "soil_en": "Fertile clay loam to loam soils with good water retention. Optimal soil pH is 5.5 to 6.5.",
        "fertilizer_guide_bn": (
            "বোরো ধানের জন্য বিঘা প্রতি (৩৩ শতক): "
            "ইউরিয়া ৩৫-৩৮ কেজি (৩ কিস্তিতে), টিএসপি/ডিএপি ১২-১৫ কেজি, "
            "এমওপি (পটাশ) ১৮-২০ কেজি, জিপসাম ১৫ কেজি এবং জিংক সালফেট ১.৫ কেজি। "
            "ইউরিয়া বাদে সব সার শেষ চাষের সময় দিতে হবে।"
        ),
        "fertilizer_guide_en": (
            "For Boro Rice per Bigha (33 decimals): "
            "Urea 35-38 kg (in 3 split applications), TSP/DAP 12-15 kg, "
            "MOP (Potash) 18-20 kg, Gypsum 15 kg, and Zinc Sulphate 1.5 kg. "
            "Apply all fertilizers except urea during final land preparation."
        ),
        "diseases": [
            {
                "id": "rice_blast",
                "name_bn": "ধানের ব্লাস্ট রোগ (Rice Blast)",
                "name_en": "Rice Blast Disease",
                "symptoms_bn": "পাতায় চোখের মতো বা নৌকার আকৃতির দাগ পড়ে। মাঝের অংশ ছাই রঙের এবং কিনারা বাদামি হয়। শীষ আক্রমণ করলে শীষ ভেঙে যায় (গলা পচা)।",
                "symptoms_en": "Eye-shaped or spindle-shaped lesions on leaves with gray centers and brownish margins. Attack on panicle neck causes neck blast and empty grains.",
                "chemical_cure_bn": "ট্রাইসাইক্লাজোল (যেমন: ট্রুপার ৭৫ ডব্লিউপি বা ট্রপার) প্রতি লিটার পানিতে ০.৭৫ গ্রাম অথবা অ্যাজোক্সিস্ট্রবিন + ডাইফেনোকোনাজোল (যেমন: অ্যামিস্টার টপ) ১ মিলি/লিটার পানিতে মিশিয়ে বিকেলে স্প্রে করুন।",
                "chemical_cure_en": "Spray Tricyclazole 75 WP (e.g. Trooper) @ 0.75 g/L or Azoxystrobin + Difenoconazole (Amistar Top) @ 1 ml/L in the late afternoon.",
                "organic_cure_bn": "জমিতে পরিমিত পটাশ দিন, নাইট্রোজেন (ইউরিয়া) অতিরিক্ত দেওয়া বন্ধ করুন। সুষম সেচ নিশ্চিত করুন। আক্রান্ত জমিতে ছাই বা ট্রাইকোডার্মা ছিটানো যায়।",
                "organic_cure_en": "Avoid excessive nitrogen (urea). Maintain balanced potash. Ensure proper irrigation. Apply Trichoderma or wood ash in initial stage."
            },
            {
                "id": "bacterial_leaf_blight",
                "name_bn": "পাতাপোড়া রোগ (Bacterial Leaf Blight)",
                "name_en": "Bacterial Leaf Blight (BLB)",
                "symptoms_bn": "পাতার ডগা থেকে নিচের দিকে কিনার বরাবর ঢেউ খেলানো হলুদ বা ধূসর বাদামি দাগ নিচের দিকে নামতে থাকে। পাতা শুকিয়ে খড়ের মতো হয়।",
                "symptoms_en": "Starts as water-soaked lesions from leaf tip along margins, turning yellow to grayish-white, wavy margins, and drying like straw.",
                "chemical_cure_bn": "বিঘাপ্রতি ৫ কেজি পটাশ ও ১ কেজি জিংক সার উপরিপ্রয়োগ করুন। কপার হাইড্রোক্সাইড (যেমন: কুপ্রোফিক্স/চ্যাম্পিয়ন) ২ গ্রাম/লিটার অথবা থায়োফেনেট মিথাইল স্প্রে করুন।",
                "chemical_cure_en": "Top-dress 5 kg MOP and 1 kg Zinc per bigha. Spray Copper Hydroxide (Champion/Cuproxat) @ 2 g/L water.",
                "organic_cure_bn": "ইউরিয়া সারের উপরিপ্রয়োগ সাময়িক বন্ধ রাখুন। জমির পানি শুকিয়ে ২-৩ দিন পর আবার সেচ দিন।",
                "organic_cure_en": "Halt urea top-dressing immediately. Drain field water for 2-3 days, then re-irrigate fresh water."
            },
            {
                "id": "sheath_blight",
                "name_bn": "ধানের খোলপোড়া রোগ (Sheath Blight)",
                "name_en": "Sheath Blight",
                "symptoms_bn": "পানির ওপর গাছের খোলে প্রথমে ডিম্বাকার ধূসর সবুজ দাগ হয়, পরে সাপের খোলসের মতো চারদিকে বাদামি বলয় তৈরি হয়।",
                "symptoms_en": "Oval, water-soaked grayish-green spots on leaf sheaths near water level, spreading upward into snake-skin patterns.",
                "chemical_cure_bn": "ভ্যালিডামাইসিন (যেমন: ভ্যালিডা ৫ এল) ২ মিলি/লিটার অথবা হেক্সাকোনাজোল (যেমন: কনটাফ ৫ ইসি) ১ মিলি/লিটার পানিতে মিশিয়ে গোড়ায় স্প্রে করুন।",
                "chemical_cure_en": "Spray Validamycin (Validacin) @ 2 ml/L or Hexaconazole (Contaf) @ 1 ml/L targeting the plant base.",
                "organic_cure_bn": "গাছের ঘনত্ব কম রাখুন, যাতে আলো-বাতাস চলাচল করতে পারে। অতিরিক্ত ইউরিয়া পরিহার করুন।",
                "organic_cure_en": "Maintain proper plant spacing for sunlight and air flow. Avoid excessive urea."
            }
        ],
        "pests": [
            {
                "name_bn": "মাজরা পোকা (Stem Borer)",
                "name_en": "Stem Borer",
                "remedy_bn": "কুশি অবস্থায় আক্রমণ হলে 'মরা ডিগ' এবং থোড় অবস্থায় 'সাদা শীষ' দেখা যায়। প্রতি বিঘায় ৩-৪টি আলোর ফাঁদ এবং ডালপালা পুঁতে পার্চিং করুন। বেশি হলে কার্বোফিউরান (যেমন: ফুরাডান ৫জি) বা ক্লোরপায়রিফস প্রয়োগ করুন।",
                "remedy_en": "Causes 'dead heart' at vegetative stage and 'white head' at flowering. Use bird perching (T-stakes) and light traps. If severe, apply Chlorantraniliprole (Virtako/Coragen) or Carbofuran."
            },
            {
                "name_bn": "বাদামি গাছফড়িং / কারেন্ট পোকা (BPH - Brown Planthopper)",
                "name_en": "Brown Planthopper (BPH)",
                "remedy_bn": "গাছের গোড়া থেকে রস চুষে খায়, ফলে ধান গাছ পুড়ে যাওয়ার মতো শুকিয়ে যায় (হপার বার্ন)। পিম্যাট্রোজাইন (যেমন: চেস ৫০ ডব্লিউজি) ০.৫ গ্রাম/লিটার অথবা আইসোপ্রোকার্ব গোড়ায় স্প্রে করুন। জমিতে 'বিলি কাটা' (বাতাস চলাচলের নালা তৈরি) করুন।",
                "remedy_en": "Sucks sap from stem base causing 'hopper burn'. Create alleys in the field for sunlight. Spray Pymetrozine (Chess 50 WG) @ 0.5 g/L directly at the base."
            }
        ]
    },
    "potato": {
        "name_bn": "আলু (Potato)",
        "name_en": "Potato",
        "category_bn": "কন্দ জাতীয় ফসল",
        "category_en": "Tuber Crop",
        "seasons_bn": "রবি মৌসুম (কার্তিক-অগ্রহায়ণ / অক্টোবর-ডিসেম্বর রোপণ)",
        "seasons_en": "Rabi Season (October to December planting)",
        "soil_bn": "বেলে দোআঁশ থেকে দোআঁশ মাটি আলু চাষের জন্য আদর্শ। মাটির অম্লমান বা pH ৬.০-৭.০ থাকা ভালো।",
        "soil_en": "Sandy loam to loam soils rich in organic matter. Ideal pH is 5.5 to 6.5.",
        "fertilizer_guide_bn": (
            "বিঘাপ্রতি (৩৩ শতক): গোবর/কম্পোস্ট ৬০০-৮০০ কেজি, "
            "ইউরিয়া ৩৫ কেজি, টিএসপি ২৫ কেজি, এমওপি ৩৫ কেজি, "
            "জিপসাম ১৫ কেজি, ম্যাগনেসিয়াম সালফেট ৫ কেজি এবং বোরন ১.৫ কেজি।"
        ),
        "fertilizer_guide_en": (
            "Per Bigha (33 decimals): Well-decomposed cowdung/compost 600-800 kg, "
            "Urea 35 kg, TSP 25 kg, MOP 35 kg, Gypsum 15 kg, "
            "Magnesium Sulphate 5 kg, Boron 1.5 kg."
        ),
        "diseases": [
            {
                "id": "potato_late_blight",
                "name_bn": "আলুর নাবি ধসা / লেইট ব্লাইট (Late Blight)",
                "name_en": "Late Blight of Potato",
                "symptoms_bn": "মেঘলা ও কুয়াশাচ্ছন্ন আবহাওয়ায় পাতায় ভেজা ভেজা কালচে ছোপ ছোপ দাগ দেখা যায়। ভোরে পাতার উল্টো পিঠে সাদা তুলার মতো ছত্রাক দেখা যায়। দ্রুত পুরো গাছ পচে যায়।",
                "symptoms_en": "Dark, water-soaked lesions on leaves during foggy/humid weather. White fungal mildew appears on undersides of leaves early morning. Plants quickly collapse and rot.",
                "chemical_cure_bn": "রোগ দেখা দিলে অবিলম্বে সাইমোক্সানিল + ম্যানকোজেব (যেমন: কার্জেট এম-৮ বা ডায়থেন এম-৪৫) ২.৫ গ্রাম/লিটার অথবা ডাইমেথোমর্ফ + ম্যানকোজেব (অ্যাক্রোবেট এমজেড) ২ গ্রাম/লিটার হারে প্রতি ৭-১০ দিন পরপর স্প্রে করুন।",
                "chemical_cure_en": "Immediately spray Mancozeb + Cymoxanil (Curzate M-8) @ 2.5 g/L or Dimethomorph + Mancozeb (Acrobat MZ) @ 2 g/L every 7-10 days.",
                "organic_cure_bn": "সুষম সার ব্যবহার, কুয়াশা শুরু হওয়ার আগে প্রতিরোধক হিসেবে বোর্দো মিশ্রণ বা কপার অক্সিক্লোরাইড স্প্রে করা। আক্রান্ত ডালপালা পুড়িয়ে ফেলা।",
                "organic_cure_en": "Ensure proper earthing up, spray Bordeaux mixture preventively before fog season, destroy infected plant debris."
            },
            {
                "id": "potato_scab",
                "name_bn": "আলুর দাদ রোগ (Common Scab)",
                "name_en": "Common Scab",
                "symptoms_bn": "আলুর চামড়ায় খসখসে, উঁচু বা গর্তযুক্ত ক্ষত বা খোসপাঁচড়ার মতো দাগ হয়।",
                "symptoms_en": "Rough, corky, pitted lesions on the potato tuber skin.",
                "chemical_cure_bn": "বীজ শোধন: বীজ রোপণের আগে কার্বেনডাজিম (যেমন: অটোস্টিন) ২ গ্রাম/লিটার পানিতে মিশিয়ে বীজ শোধন করে শুকিয়ে নিন।",
                "chemical_cure_en": "Treat seed tubers with Carbendazim (Autostin) @ 2 g/L before sowing. Ensure balanced soil moisture during tuber formation.",
                "organic_cure_bn": "জমির মাটির পিএইচ সামান্য অম্লীয় রাখা এবং জৈব সার প্রয়োগ বৃদ্ধি করা।",
                "organic_cure_en": "Apply green manure, avoid high liming, keep soil moist during early tuber initiation."
            }
        ],
        "pests": [
            {
                "name_bn": "কাটুই পোকা (Cutworm)",
                "name_en": "Cutworm",
                "remedy_bn": "রাতের বেলা মাটির উপর থেকে চারা গাছ কেটে ফেলে। দিনের বেলা গাছের গোড়ায় মাটি খুঁড়লে পোকা পাওয়া যায়। ক্লোরপায়রিফস (যেমন: ডারসবান) বা ডার্বিন মাটির গোড়ায় স্প্রে বা প্রয়োগ করুন।",
                "remedy_en": "Cuts young seedlings at ground level during night. Hand-pick larvae from soil around damaged stems. Apply Chlorpyrifos around root zone in late afternoon."
            }
        ]
    },
    "tomato": {
        "name_bn": "টমেটো (Tomato)",
        "name_en": "Tomato",
        "category_bn": "সবজি ফসল",
        "category_en": "Vegetable Crop",
        "seasons_bn": "শীতকালীন (সেপ্টেম্বর-নভেম্বর বীজ বপন) এবং গ্রীষ্মকালীন (মে-জুলাই)",
        "seasons_en": "Winter (Sep-Nov) and Summer/Rainy (May-Jul)",
        "soil_bn": "জৈব পদার্থ সমৃদ্ধ উর্বর দোআঁশ বা বেলে দোআঁশ মাটি। পিএইচ ৬.০-৬.৮ সবচেয়ে উপযুক্ত।",
        "soil_en": "Fertile loam or sandy loam with good drainage and organic matter. pH 6.0-6.8.",
        "fertilizer_guide_bn": "বিঘাপ্রতি: গোবর ১ টন, ইউরিয়া ৩০ কেজি, টিএসপি ২৫ কেজি, এমওপি ২৫ কেজি, জিপসাম ১৫ কেজি, বোরন ১.৫ কেজি। ফুল আসার সময় বোরন ও ক্যালসিয়াম স্প্রে ফল ফাটা রোধ করে।",
        "fertilizer_guide_en": "Per Bigha: Cowdung 1 ton, Urea 30 kg, TSP 25 kg, MOP 25 kg, Gypsum 15 kg, Boron 1.5 kg. Foliar spray of Boron & Calcium at flowering prevents fruit cracking.",
        "diseases": [
            {
                "id": "tomato_leaf_curl",
                "name_bn": "টমেটোর পাতা কোঁকড়ানো রোগ (Tomato Leaf Curl Virus)",
                "name_en": "Tomato Leaf Curl Virus (TLCV)",
                "symptoms_bn": "গাছের নতুন পাতা ছোট, পুরু এবং উপরের দিকে কুঁকড়ে বাটি বা নৌকার মতো হয়ে যায়। গাছ খাটো হয়ে যায় ও ফুল-ফল কমে যায়। সাদা মাছি এ রোগ ছড়ায়।",
                "symptoms_en": "Upward curling and puckering of leaves, stunted plant growth, thickened brittle leaves, poor fruit set. Spread by Whiteflies.",
                "chemical_cure_bn": "বাহক পোকা (সাদা মাছি) দমন করতে ইমিডাক্লোプリড (যেমন: এডমায়ার/টিডো) ০.৫ মিলি/লিটার অথবা অ্যাসিটামিপ্রিড ০.৫ গ্রাম/লিটার পানিতে স্প্রে করুন।",
                "chemical_cure_en": "Control the whitefly vector using Imidacloprid (Admire) @ 0.5 ml/L or Acetamiprid @ 0.5 g/L alternating with Thiamethoxam.",
                "organic_cure_bn": "জমিতে হলুদ আঠালো ফাঁদ (Yellow Sticky Trap) ব্যবহার করুন। নিম তেলের দ্রবণ (৫ মিলি/লিটার পানিতে সামান্য ডিটারজেন্ট মিশিয়ে) স্প্রে করুন।",
                "organic_cure_en": "Install yellow sticky traps (15-20 per acre). Spray neem oil (5 ml/L with soap water) weekly."
            },
            {
                "id": "blossom_end_rot",
                "name_bn": "টমেটোর ব্লসম এন্ড রট / নিচের অংশ পচা",
                "name_en": "Blossom End Rot",
                "symptoms_bn": "টমেটোর নিচের অংশে কালো বা কালচে বাদামি চ্যাপ্টা দাগ পড়ে এবং শক্ত হয়ে যায়। এটি মূলত ক্যালসিয়ামের অভাব এবং অনিয়মিত সেচের কারণে ঘটে।",
                "symptoms_en": "Water-soaked spot at blossom end of fruit turning dark brown, leathery, and sunken. Caused by Calcium deficiency and erratic watering.",
                "chemical_cure_bn": "চিলেটেড ক্যালসিয়াম বা ক্যালসিয়াম নাইট্রেট ৫ গ্রাম/লিটার পানিতে গুলে গাছের পাতায় ও ফলে স্প্রে করুন।",
                "chemical_cure_en": "Foliar spray of Chelated Calcium or Calcium Nitrate @ 4-5 g/L. Maintain even soil moisture.",
                "organic_cure_bn": "মাটিতে ডিমের খোসার গুঁড়া অথবা ডলোমাইট চুন ব্যবহার করুন। নিয়মিত সুষম সেচ দিন।",
                "organic_cure_en": "Add crushed eggshells or dolomite lime to soil. Avoid water stress with consistent drip or furrows."
            }
        ],
        "pests": [
            {
                "name_bn": "ফল ছিদ্রকারী পোকা (Fruit Borer)",
                "name_en": "Fruit Borer (Helicoverpa armigera)",
                "remedy_bn": "পোকা ফল ছিদ্র করে ভেতরে ঢুকে শাঁস খায়। আক্রান্ত ফল নষ্ট হয়। ফেরোমোন ফাঁদ লাগান। দমনে স্পিনোস্যাড (যেমন: ট্রেসার) ০.৪ মিলি/লিটার অথবা এমামেকটিন বেনজোয়েট (যেমন: প্রোক্লেম) ১ গ্রাম/লিটার স্প্রে করুন।",
                "remedy_en": "Larvae bore into fruit. Set up sex pheromone traps. Spray Spinosad (Tracer) @ 0.4 ml/L or Emamectin Benzoate (Proclaim) @ 1 g/L."
            }
        ]
    },
    "wheat": {
        "name_bn": "গম (Wheat)",
        "name_en": "Wheat",
        "category_bn": "দানা ফসল",
        "category_en": "Cereal Crop",
        "seasons_bn": "রবি মৌসুম (১৫ নভেম্বর - ৩০ নভেম্বর বপনের সেরা সময়)",
        "seasons_en": "Rabi Season (Nov 15 - Nov 30 optimal sowing window)",
        "soil_bn": "উর্বর দোআঁশ ও বেলে দোআঁশ মাটি গম চাষের জন্য সবচেয়ে উপযোগী।",
        "soil_en": "Fertile loam and sandy-loam soils with good drainage.",
        "fertilizer_guide_bn": "বিঘাপ্রতি: ইউরিয়া ৩৫ কেজি (২ কিস্তিতে), টিএসপি ২০ কেজি, এমওপি ১৫ কেজি, জিপসাম ১৫ কেজি, বোরন ১ কেজি। প্রথম সেচ ২০-২১ দিন পর মুকুট শিকড় (CRI) পর্যায়ে দেওয়া আবশ্যক।",
        "fertilizer_guide_en": "Per Bigha: Urea 35 kg, TSP 20 kg, MOP 15 kg, Gypsum 15 kg, Borax 1 kg. First irrigation at Crown Root Initiation (CRI) stage (20-21 days) is vital.",
        "diseases": [
            {
                "id": "wheat_blast",
                "name_bn": "গমের ব্লাস্ট রোগ (Wheat Blast)",
                "name_en": "Wheat Blast",
                "symptoms_bn": "শীষের আক্রান্ত অংশের উপরের অংশ সাদা ও শুষ্ক হয়ে যায়। দানাপুষ্টি হয় না, চিটা হয়ে যায়।",
                "symptoms_en": "Panicle neck or base bleaches white while lower stem stays green. Grain does not fill, turns shriveled.",
                "chemical_cure_bn": "শীষ বের হওয়ার মুখে ট্রাইসাইক্লাজোল + হেক্সাকোনাজোল অথবা নেটিভো (টেবুকোনাজোল + ট্রাইফ্লক্সিস্ট্রবিন) ০.৬ গ্রাম/লিটার পানিতে মিশিয়ে বিকেলে স্প্রে করুন।",
                "chemical_cure_en": "Spray Nativo (Tebuconazole + Trifloxystrobin) @ 0.6 g/L or Amistar Top @ 1 ml/L at heading stage.",
                "organic_cure_bn": "ব্লাস্ট প্রতিরোধী জাত যেমন বারি গম ৩৩ (WMRI 33) চাষ করুন। বীজ শোধন করে বপন করুন।",
                "organic_cure_en": "Sow resistant varieties like BARI Gom 33. Treat seeds with Vitavax or Trichoderma."
            }
        ],
        "pests": [
            {
                "name_bn": "জাবপোকা (Aphids)",
                "name_en": "Aphids",
                "remedy_bn": "পাতা ও শীষ থেকে রস চুষে খায়। আক্রমণের শুরুতে নিম পাতার নির্যাস বা ডিটারজেন্ট মিশ্রিত পানি স্প্রে করুন। তীব্র হলে ইমিডাক্লোপ্রিড ০.৫ মিলি/লিটার স্প্রে করুন।",
                "remedy_en": "Sucks sap from leaves and young ears. Spray soapy water or neem extract; if severe use Imidacloprid @ 0.5 ml/L."
            }
        ]
    },
    "eggplant": {
        "name_bn": "বেগুন (Brinjal / Eggplant)",
        "name_en": "Brinjal / Eggplant",
        "category_bn": "সবজি ফসল",
        "category_en": "Vegetable Crop",
        "seasons_bn": "সারা বছরই চাষ করা যায়। শীতকালীন ও বর্ষাকালীন জাত রয়েছে।",
        "seasons_en": "Grown year-round with specific winter and summer/rainy season cultivars.",
        "soil_bn": "উর্বর দোআঁশ ও পলি দোআঁশ মাটি যেখানে পানি জমে থাকে না।",
        "soil_en": "Well-drained fertile loam and sandy loam.",
        "fertilizer_guide_bn": "বিঘাপ্রতি: গোবর ১.৫ টন, ইউরিয়া ৩৫ কেজি, টিএসপি ৩০ কেজি, এমওপি ২৫ কেজি, জিপসাম ১০ কেজি, জিংক ১ কেজি।",
        "fertilizer_guide_en": "Per Bigha: Cowdung 1.5 tons, Urea 35 kg, TSP 30 kg, MOP 25 kg, Gypsum 10 kg, Zinc 1 kg.",
        "diseases": [
            {
                "id": "bacterial_wilt",
                "name_bn": "বেগুনের ব্যাকটেরিয়াজনিত ঢলে পড়া রোগ (Bacterial Wilt)",
                "name_en": "Bacterial Wilt",
                "symptoms_bn": "সবুজ অবস্থাতেই পুরো গাছ দুপুরের রোদে ঝিমিয়ে পড়ে, রাতে সতেজ হয়, এবং কয়েকদিনের মধ্যে পুরো গাছ শুকিয়ে মারা যায়। ডাল কেটে পরিষ্কার পানিতে রাখলে সুতার মতো সাদা ব্যাকটেরিয়াল উজিং দেখা যায়।",
                "symptoms_en": "Rapid wilting of entire green plant during hot day, slight recovery at night, followed by death. Stem cut dipped in water shows white bacterial streaming.",
                "chemical_cure_bn": "গাছের গোড়ায় ব্লিচিং পাউডার বা কপার অক্সিক্লোরাইড ৪ গ্রাম/লিটার পানিতে মিশিয়ে গোড়া ভিজিয়ে দিন। আক্রান্ত গাছ তুলে ধ্বংস করুন।",
                "chemical_cure_en": "Drench soil with Copper Oxychloride @ 4 g/L or Bleaching powder @ 10-15 kg/ha. Uproot and burn severely infected plants.",
                "organic_cure_bn": "বুনো বেগুনের (Solanum torvum) সাথে জোড় কলম (Grafting) করে চারা তৈরি করলে এ রোগ হয় না। ট্রাইকোডার্মা ব্যবহার করুন।",
                "organic_cure_en": "Grafting on wild brinjal rootstock (Solanum torvum) confers total resistance. Use Trichoderma harzianum."
            }
        ],
        "pests": [
            {
                "name_bn": "ডগা ও ফল ছিদ্রকারী পোকা (Shoot and Fruit Borer)",
                "name_en": "Brinjal Shoot and Fruit Borer (BSFB)",
                "remedy_bn": "কচি ডগায় ও ফলের ভেতর ছিদ্র করে মল ত্যাগ করে, ডগা নুয়ে পড়ে ও ফল পচে যায়। আক্রান্ত ডগা হাত দিয়ে ছিঁড়ে নষ্ট করুন। সেক্স ফেরোমোন ফাঁদ ব্যবহার করুন। প্রয়োজনে এমামেকটিন বেনজোয়েট বা ক্লোরানট্রানিলিপ্রোল স্প্রে করুন।",
                "remedy_en": "Bores into shoots and fruits causing shoot wilting and fruit damage. Hand-prune infected shoots weekly. Deploy pheromone traps (BSFB lure). Spray Emamectin Benzoate 5 SG or Chlorantraniliprole."
            }
        ]
    },
    "mustard": {
        "name_bn": "সরিষা (Mustard)",
        "name_en": "Mustard",
        "category_bn": "তৈলবীজ ফসল",
        "category_en": "Oilseed Crop",
        "seasons_bn": "রবি মৌসুম (অক্টোবর থেকে নভেম্বর বপন)",
        "seasons_en": "Rabi Season (Mid Oct to Nov sowing)",
        "soil_bn": "উর্বর দোআঁশ ও পলি দোআঁশ মাটি উত্তম।",
        "soil_en": "Fertile loamy and silt-loamy soils.",
        "fertilizer_guide_bn": "বিঘাপ্রতি: ইউরিয়া ৩৫ কেজি, টিএসপি ২৫ কেজি, এমওপি ১৫ কেজি, জিপসাম ২০ কেজি, জিংক সালফেট ১ কেজি, বোরিক এসিড ১ কেজি। সালফার ও বোরন তেলের পরিমাণ ও দানা বৃদ্ধি করে।",
        "fertilizer_guide_en": "Per Bigha: Urea 35 kg, TSP 25 kg, MOP 15 kg, Gypsum 20 kg, Zinc 1 kg, Borax 1 kg. Sulphur and Boron directly enhance oil content and seed filling.",
        "diseases": [
            {
                "id": "mustard_alternaria_blight",
                "name_bn": "সরিষার অল্টারনারিয়া পাতা ঝলসানো রোগ (Alternaria Blight)",
                "name_en": "Alternaria Leaf Blight",
                "symptoms_bn": "পাতায় ও শুঁটিতে গোলাকার বাদামি রঙের বলয়যুক্ত দাগ দেখা যায়।",
                "symptoms_en": "Concentric circular brown spots with target-board appearance on leaves, stems, and pods.",
                "chemical_cure_bn": "রোভরাল ৫০ ডব্লিউপি (আইপ্রোডিওন) অথবা ডাইথেন এম-৪৫ (ম্যানকোজেব) ২ গ্রাম/লিটার পানিতে মিশিয়ে স্প্রে করুন।",
                "chemical_cure_en": "Spray Rovral 50 WP (Iprodione) or Mancozeb @ 2 g/L at 10-12 day intervals.",
                "organic_cure_bn": "বীজ শোধন করুন এবং ফসলের অবশিষ্টাংশ পুড়িয়ে ফেলুন।",
                "organic_cure_en": "Seed treatment and destruction of infected crop residues."
            }
        ],
        "pests": [
            {
                "name_bn": "জাবপোকা (Mustard Aphid)",
                "name_en": "Mustard Aphid",
                "remedy_bn": "ফুল ও শুঁটি থেকে রস চুষে নেয়। লেডিবার্ড বিটল (বন্ধু পোকা) থাকলে এটি প্রাকৃতিকভাবেই দমন হয়। বেশি হলে ম্যালাথিয়ন ২ মিলি/লিটার বা ইমিডাক্লোপ্রিড স্প্রে করুন।",
                "remedy_en": "Colonies cluster on inflorescences and pods sucking sap. Conserve ladybird beetles. If above ETL, spray Malathion 57 EC @ 2 ml/L or Imidacloprid."
            }
        ]
    },
    "maize": {
        "name_bn": "ভুট্টা (Maize / Corn)",
        "name_en": "Maize / Corn",
        "category_bn": "দানা ফসল",
        "category_en": "Cereal Crop",
        "seasons_bn": "রবি (অক্টোবর-ডিসেম্বর) এবং খরিফ (ফেব্রুয়ারি-এপ্রিল)",
        "seasons_en": "Rabi (Oct-Dec) and Kharif (Feb-Apr)",
        "soil_bn": "গভীর, সুনিষ্কাশিত বেলে দোআঁশ বা দোআঁশ মাটি।",
        "soil_en": "Deep, well-drained sandy loam or silt loam.",
        "fertilizer_guide_bn": "ভুট্টা প্রচুর খাদ্য গ্রহণ করে। বিঘাপ্রতি: ইউরিয়া ৬৫ কেজি, টিএসপি ৩৫ কেজি, এমওপি ৩৫ কেজি, জিপসাম ৩০ কেজি, জিংক ২.৫ কেজি, বোরন ১.৫ কেজি।",
        "fertilizer_guide_en": "Maize is a heavy feeder. Per Bigha: Urea 65 kg, TSP 35 kg, MOP 35 kg, Gypsum 30 kg, Zinc 2.5 kg, Borax 1.5 kg.",
        "diseases": [
            {
                "id": "maize_leaf_blight",
                "name_bn": "ভুট্টার পাতা ঝলসানো রোগ (Maydis Leaf Blight)",
                "name_en": "Maydis Leaf Blight",
                "symptoms_bn": "পাতায় লম্বাটে বাদামি দাগ দেখা যায়। বেশি হলে পাতা শুকিয়ে যায়।",
                "symptoms_en": "Long, elliptical grayish-brown lesions on leaves parallel to veins.",
                "chemical_cure_bn": "টিল্ট ২৫০ ইসি (প্রপিকোনাজোল) ০.৫ মিলি/লিটার পানিতে স্প্রে করুন।",
                "chemical_cure_en": "Spray Tilt 250 EC (Propiconazole) @ 0.5 ml/L or Mancozeb @ 2 g/L.",
                "organic_cure_bn": "সুষম সার ও নিষ্কাশন ব্যবস্থা নিশ্চিত করুন।",
                "organic_cure_en": "Ensure balanced nutrition and good soil drainage."
            }
        ],
        "pests": [
            {
                "name_bn": "ফল আর্মিওয়ার্ম (Fall Armyworm - FAW)",
                "name_en": "Fall Armyworm (FAW)",
                "remedy_bn": "গাছের মোচার ভেতর ও পাতার ভেতরের কুঁড়ি খেয়ে ঝাঁজরা করে ফেলে। লক্ষণ দেখা দিলে গাছের মাথায় ভিরটাকো (থায়ামেথোক্সাম + ক্লোরানট্রানিলিপ্রোল) বা স্পিনোস্যাড সরাসরি কুঁড়িতে স্প্রে করুন। আক্রমণ শুরুতে ছাই বা বালি কুঁড়িতে দেওয়া যায়।",
                "remedy_en": "Attacks whorls creating ragged holes and sawdust-like frass. Apply Spinosad, Emamectin Benzoate, or Coragen directly into whorls. Fine sand or wood ash can be poured into whorls for physical suppression."
            }
        ]
    }
}

ORGANIC_PESTICIDES = {
    "neem_spray": {
        "title_bn": "নিম পাতার দ্রবণ ও নিম তেল",
        "title_en": "Neem Oil & Leaf Extract",
        "usage_bn": "১ কেজি নিমপাতা ১০ লিটার পানিতে ফুটিয়ে ছেঁকে নিন। অথবা ৫ মিলি নিম তেল ও ১ গ্রাম ডিটারজেন্ট ১ লিটার পানিতে মিশিয়ে স্প্রে করলে জাবপোকা, সাদা মাছি, লেদা পোকা দমন হয়।",
        "usage_en": "Boil 1 kg crushed neem leaves in 10L water or mix 5 ml pure cold-pressed neem oil with 1 g mild liquid soap per 1 L water. Highly effective against aphids, whiteflies, thrips, and caterpillars."
    },
    "garlic_chili": {
        "title_bn": "রসুন ও মরিচের জৈব বালাইনাশক",
        "title_en": "Garlic & Chili Organic Spray",
        "usage_bn": "৫০ গ্রাম রসুন ও ৫০ গ্রাম কাঁচা মরিচ পেস্ট করে ১ লিটার পানিতে ২৪ ঘণ্টা ভিজিয়ে রাখুন। এরপর ছেঁকে আরও ৪ লিটার পানি ও সামান্য সাবানের ফেনা মিশিয়ে স্প্রে করলে পোকা দূর হয়।",
        "usage_en": "Blend 50g garlic cloves and 50g hot chili with 1L water, soak 24 hours, strain, dilute with 4L water, and spray as a natural insect deterrent."
    },
    "trichoderma": {
        "title_bn": "ট্রাইকোডার্মা জৈব ছত্রাকনাশক",
        "title_en": "Trichoderma Bio-Fungicide",
        "usage_bn": "মাটির ক্ষতিকর ছত্রাক দমন, শিকড় পচা, ঢলে পড়া রোগ প্রতিরোধে গোবর সারের সাথে মিশিয়ে জমিতে প্রয়োগ অথবা বীজ শোধনে অত্যন্ত কার্যকর।",
        "usage_en": "Antagonistic beneficial fungus highly effective against root rot, damping-off, wilt, and soil-borne fungal pathogens."
    }
}

SEASONAL_CALENDAR = {
    "rabi": {
        "season_bn": "রবি মৌসুম (শীতকাল: আশ্বিন-ফাল্গুন / অক্টোবর-মার্চ)",
        "season_en": "Rabi Season (Winter: October - March)",
        "weather_bn": "শুষ্ক, রৌদ্রোজ্জ্বল, মৃদু থেকে তীব্র শীত, বৃষ্টিপাত কম। সেচ ব্যবস্থাপনা অত্যন্ত গুরুত্বপূর্ণ।",
        "weather_en": "Dry, sunny, mild to cold, low rainfall. Irrigation management is critical.",
        "major_crops_bn": ["বোরো ধান", "গম", "ভুট্টা", "আলু", "সরিষা", "টমেটো", "ফুলকপি", "বাঁধাকপি", "পেঁয়াজ", "রসুন", "মরিচ", "ডাল (মসুর, ছোলা)"],
        "major_crops_en": ["Boro Rice", "Wheat", "Maize", "Potato", "Mustard", "Tomato", "Cauliflower", "Cabbage", "Onion", "Garlic", "Chilli", "Lentil"]
    },
    "kharif_1": {
        "season_bn": "খরিফ-১ মৌসুম (গ্রীষ্মকাল: চৈত্র-জ্যৈষ্ঠ / মার্চ-জুন)",
        "season_en": "Kharif-1 Season (Summer / Pre-Monsoon: March - June)",
        "weather_bn": "উচ্চ তাপমাত্রা, আর্দ্রতা বৃদ্ধি, কালবৈশাখী ঝড় ও আকস্মিক শিলাবৃষ্টির সম্ভাবনা।",
        "weather_en": "High temperatures, increasing humidity, pre-monsoon showers and thunderstorm risk.",
        "major_crops_bn": ["আউশ ধান", "পাট", "তিল", "গ্রীষ্মকালীন শাকসবজি (ঝিঙে, চিচিঙ্গা, করলা, ঢ্যাঁড়শ)", "তরমুজ", "বাঙ্গি"],
        "major_crops_en": ["Aus Rice", "Jute", "Sesame", "Summer Cucurbits (Ridge Gourd, Bitter Gourd, Okra)", "Watermelon", "Muskmelon"]
    },
    "kharif_2": {
        "season_bn": "খরিফ-২ মৌসুম (বর্ষাকাল: আষাঢ়-ভাদ্র / জুন-অক্টোবর)",
        "season_en": "Kharif-2 Season (Monsoon: June - October)",
        "weather_bn": "প্রচুর বৃষ্টিপাত, উচ্চ আর্দ্রতা, জলাবদ্ধতা ও বন্যার ঝুঁকি। রোগবালাই আক্রমণের সম্ভাবনা বেশি।",
        "weather_en": "Heavy precipitation, high humidity, waterlogging and flood risk. Fungal/bacterial disease pressure is elevated.",
        "major_crops_bn": ["রোপা আমন ধান", "নাবি পাট", "বর্ষাকালীন বেগুন", "লাউ", "পুঁইশাক", "মিষ্টি কুমড়া"],
        "major_crops_en": ["Transplanted Aman Rice", "Late Jute", "Rainy Brinjal", "Bottle Gourd", "Indian Spinach", "Sweet Pumpkin"]
    }
}
