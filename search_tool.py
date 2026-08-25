import json
import os

master_file = "ultimate_multi_platform_database/ultimate_6_platforms_database_master.json"

if not os.path.exists(master_file):
    print("❌ قاعدة البيانات الرئيسية غير موجودة!")
    exit()

print("📂 جاري تحميل قاعدة البيانات الرئيسية...")
with open(master_file, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"✅ تم تحميل {len(data)} قالب بنجاح.")
print("=" * 50)
print("🔍 أداة البحث الذكية في قوالب الأتمتة (اكتب كلمة مفتاحية مثل: ai, shopify, ذكاء-اصطناعي، تسويق)")
print("=" * 50)

while True:
    query = input("\n🔎 ابحث (أو اكتب 'exit' للخروج): ").strip().lower()
    
    if query == 'exit':
        print("👋 إلى اللقاء!")
        break
        
    if not query:
        continue
        
    results = []
    for item in data:
        title = item.get("title", "").lower()
        desc = item.get("description", "").lower()
        tags = [t.lower() for t in item.get("tags", [])]
        
        # البحث في العنوان، الوصف، أو الوسوم
        if query in title or query in desc or any(query in t for t in tags):
            results.append(item)
            
    print(f"\n📊 نتائج البحث عن ('{query}'): وجدنا {len(results)} قالب متطابق:")
    print("-" * 50)
    
    for i, res in enumerate(results[:5], 1): # عرض أول 5 نتائج تطابقاً لتجنب الإطالة
        print(f"{i}. العنوان: {res.get('title')}")
        print(f"   📂 التصنيف: {res.get('domain')}")
        print(f"   🏷️ الوسوم: {', '.join(res.get('tags', []))}")
        print(f"   🔗 الرابط: {res.get('url', 'غير متوفر')}")
        print("-" * 30)
        
    if len(results) > 5:
        print(f"... وهناك {len(results) - 5} نتائج أخرى مطابقة.")