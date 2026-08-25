import json
import os

file_path = "ultimate_multi_platform_database/ultimate_6_platforms_database.json"

if os.path.exists(file_path):
    print("📂 جاري قراءة الملف وتحديث تصنيفاته...")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        title = item.get("title", "")
        # تحديث التصنيفات والوسوم مباشرة
        if "shop" in title.lower():
            item["domain"] = "E_Commerce_And_Retail"
        elif "market" in title.lower():
            item["domain"] = "Digital_Marketing_And_Social"
        else:
            item["domain"] = "AI_And_Machine_Learning"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✨ تم تحديث الملف بنجاح تام!")
else:
    print("❌ الملف غير موجود.")