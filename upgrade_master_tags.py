import json
import os

input_file = "ultimate_multi_platform_database/ultimate_6_platforms_database_master.json"

if not os.path.exists(input_file):
    input_file = "ultimate_multi_platform_database/ultimate_6_platforms_database_pro.json"

print("📂 جاري قراءة قاعدة البيانات لتطبيق التوصيات المتقدمة للوسوم...")
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

def generate_expert_master_tags(title, description, domain):
    combined = (title + " " + description + " " + domain).lower()
    
    tags = ["automation", "سير-عمل", "أتمتة", "intermediate", "business"]
    
    # 1. وسوم الأدوات والخدمات ونماذج الذكاء الاصطناعي
    if "openai" in combined or "gpt" in combined or "chatgpt" in combined:
        tags.extend(["openai", "gpt", "chatgpt"])
    if "gemini" in combined:
        tags.extend(["gemini", "google-ai"])
    if "claude" in combined:
        tags.extend(["claude", "anthropic"])
    if "ollama" in combined or "llama" in combined:
        tags.extend(["ollama", "llama", "local-ai"])
        
    # قنوات التواصل والتكامل
    if "slack" in combined: tags.append("slack")
    if "telegram" in combined: tags.extend(["telegram", "تيليجرام"])
    if "whatsapp" in combined: tags.extend(["whatsapp", "واتساب"])
    if "gmail" in combined or "email" in combined: tags.extend(["gmail", "email", "إيميل"])
    if "google-sheets" in combined or "sheets" in combined or "excel" in combined:
        tags.extend(["google-sheets", "جداول-بيانات"])
    if "apify" in combined: tags.append("apify")
    if "airtable" in combined: tags.append("airtable")
    if "notion" in combined: tags.append("notion")
    if "hubspot" in combined or "salesforce" in combined:
        tags.extend(["hubspot", "salesforce", "crm"])

    # 2. وسوم المهام والوظائف (مثل RAG واستخراج البيانات)
    if "rag" in combined or "retrieval" in combined or "vector" in combined:
        tags.extend(["rag", "retrieval", "vector-db", "استرجاع-معرفي"])
    if "scraping" in combined or "crawl" in combined or "extract" in combined:
        tags.extend(["scraping", "extraction", "استخراج-بيانات"])
    if "summariz" in combined:
        tags.extend(["summarization", "تلخيص"])
    if "translat" in combined:
        tags.extend(["translation", "ترجمة"])
    if "lead" in combined or "prospect" in combined:
        tags.extend(["lead-generation", "توليد-عملاء"])

    # 3. وسوم القطاعات والمجالات (Legal, HR, Finance, etc.)
    if "legal" in combined or "law" in combined or "contract" in combined:
        tags.extend(["legal", "قانونية", "عقود"])
    if "finance" in combined or "etf" in combined or "stock" in combined or "invoice" in combined:
        tags.extend(["finance", "مالية", "فواتير"])
    if "hr" in combined or "cv" in combined or "resume" in combined or "hire" in combined:
        tags.extend(["hr", "recruitment", "موارد-بشرية", "توظيف"])
    if "shop" in combined or "store" in combined or "ecommerce" in combined:
        tags.extend(["ecommerce", "تجارة-إلكترونية"])

    return list(set(tags))

updated_count = 0
for item in data:
    title = item.get("title", "")
    desc = item.get("description", "")
    domain = item.get("domain", "")
    
    # تحديث وتطوير حقل الـ tags بالوسوم الاحترافية الشاملة
    item["tags"] = generate_expert_master_tags(title, desc, domain)
    updated_count += 1

output_file = "ultimate_multi_platform_database/ultimate_6_platforms_database_ultimate.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"\n✨ تمت عملية ترقية الوسوم التخصصية بنجاح تام!")
print(f"🎯 تم تحديث {updated_count} قالب بأحدث وسوم الأدوات والـ RAG والقطاعات.")
print(f"📁 النسخة النهائية المطلقة أصبحت في الملف: '{output_file}'")