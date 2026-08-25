import json
import os

master_file = "ultimate_multi_platform_database/ultimate_6_platforms_database_ultimate.json"

if not os.path.exists(master_file):
    print("❌ النسخة النهائية المطلقة غير موجودة!")
    exit()

print("📂 جاري تحميل قاعدة البيانات النهائية وموسوعة البدائل الذكية...")
with open(master_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# موسوعة البدائل المجانية ومفتوحة المصدر الشاملة (لكل أدوات الأتمتة والـ AI)
COMPREHENSIVE_FREE_ALTERNATIVES = {
    "elevenlabs": "✨ [بديل مجاني للصوت]: Coqui TTS (مفتوح المصدر) أو Hugging Face TTS Models أو تشغيل نماذج الصوت محلياً عبر Python.",
    "openai": "✨ [بديل مجاني للذكاء الاصطناعي]: Ollama (لتشغيل نماذج Llama 3 أو Mistral محلياً وبالمجان وبدون حدود).",
    "gemini": "✨ [بديل مجاني للذكاء الاصطناعي]: Google AI Studio (الطبقة المجانية Free Tier الكخيرة) أو نماذج محلية.",
    "quickbooks": "✨ [بديل مجاني للمحاسبة]: Invoice Ninja أو Odoo (Accounting Module) مفتوح المصدر.",
    "xero": "✨ [بديل مجاني للمحاسبة]: Invoice Ninja أو Express Invoice.",
    "docusign": "✨ [بديل مجاني للعقود والتوقيع]: Docuseal (مفتوح المصدر بالكامل ومصمم للربط السهل بـ n8n).",
    "salesforce": "✨ [بديل مجاني للـ CRM]: Twenty CRM أو EspoCRM (أظمة CRM مفتوحة المصدر بالكامل).",
    "hubspot": "✨ [بديل مجاني للـ CRM]: Twenty CRM أو Odoo CRM.",
    "klaviyo": "✨ [بديل مجاني للتسويق البريدي]: Mautic (أقوى نظام بريد وتوثيق تسويقي مفتوح المصدر).",
    "ahrefs": "✨ [بديل مجاني للـ SEO]: Google Search Console API + Ubersuggest (خطة مجانية) أو كشط بيانات عبر Apify.",
    "semrush": "✨ [بديل مجاني للـ SEO]: Google Trends API + Screaming Frog (الإصدار المجاني).",
    "zendesk": "✨ [بديل مجاني للدعم الفني]: Chatwoot (نظام دعم عملاء ومحادثات مفتوح المصدر يدعم Webhooks).",
    "pinecone": "✨ [بديل مجاني لقواعد البيانات المتجهية]: ChromaDB أو FAISS أو Qdrant (نسخة محلية مجانية للـ RAG)."
}

print(f"✅ تم تحميل {len(data)} قالب بنجاح.")
print("=" * 70)
print("🌐 موسوعة الأتمتة الاستراتيجية وبدائل الأدوات المجانية (جاهزة للعمل)")
print("=" * 70)

while True:
    query = input("\n🔎 ابحث عن أداة، دومين، أو تقنية (اكتب 'exit' للخروج): ").strip().lower()
    
    if query == 'exit':
        print("👋 بالتوفيق في بناء منظومة الأتمتة الخاصة بك!")
        break
        
    if not query:
        continue
        
    results = []
    for item in data:
        title = item.get("title", "").lower()
        desc = item.get("description", "").lower()
        tags = [t.lower() for t in item.get("tags", [])]
        
        if query in title or query in desc or any(query in t for t in tags):
            results.append(item)
            
    print(f"\n📊 نتائج البحث عن ('{query}'): وجدنا {len(results)} قالب متطابق:")
    print("-" * 70)
    
    for i, res in enumerate(results[:3], 1):
        print(f"{i}. العنوان: {res.get('title')}")
        print(f"   📂 التصنيف: {res.get('domain')}")
        print(f"   🏷️ الوسوم: {', '.join(res.get('tags', []))}")
        
        # فحص شامل للأدوات المدفوعة المقابلة لبيانات القالب وعرض بدائلها
        res_text = (res.get('title', '') + " " + res.get('description', '')).lower()
        tool_matched = False
        for tool, alternative in COMPREHENSIVE_FREE_ALTERNATIVES.items():
            if tool in res_text or tool in [t.lower() for t in res.get('tags', [])]:
                print(f"   💡 {alternative}")
                tool_matched = True
        
        if not tool_matched:
            print(f"   💡 [دليل البدائل]: يعتمد على أدوات قياسية أو متاحة بالكامل.")
            
        print(f"   🔗 الرابط: {res.get('url', 'غير متوفر')}")
        print("-" * 45)
        
    if len(results) > 3:
        print(f"... وهناك {len(results) - 3} نتائج أخرى مطابقة.")