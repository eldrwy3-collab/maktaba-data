import json
import os

input_file = "ultimate_multi_platform_database/ultimate_6_platforms_database_enriched.json"
if not os.path.exists(input_file):
    input_file = "ultimate_multi_platform_database/ultimate_6_platforms_database.json"

print("📂 جاري قراءة قاعدة البيانات لتوزيعها ذكياً على جميع النيتشات...")
with open(input_file, "r", encoding="utf-8") as f:
    workflows = json.load(f)

print(f"📊 إجمالي العناصر الحالية: {len(workflows)}")

def advanced_domain_and_tags(title, text=""):
    combined = (title + " " + text).lower()
    
    # توزيع وتصنيف دقيق يغطي كافة المجالات والنيتشات الاحترافية
    if any(w in combined for w in ["shop", "shopify", "woocommerce", "store", "order", "product", "cart"]):
        return "E_Commerce_And_Retail", ["ecommerce", "retail", "store"]
    elif any(w in combined for w in ["market", "social", "tiktok", "youtube", "linkedin", "seo", "ads", "instagram", "facebook"]):
        return "Digital_Marketing_And_Social", ["marketing", "social-media", "ads"]
    elif any(w in combined for w in ["crm", "hubspot", "salesforce", "lead", "pipeline", "deal", "pipedrive"]):
        return "CRM_And_Sales_Automation", ["crm", "sales", "leads"]
    elif any(w in combined for w in ["support", "ticket", "zendesk", "customer", "helpdesk", "intercom"]):
        return "Customer_Support_And_Helpdesk", ["support", "helpdesk", "tickets"]
    elif any(w in combined for w in ["pdf", "invoice", "doc", "sheet", "excel", "billing", "accounting", "parse"]):
        return "Document_And_Financial_Ops", ["documents", "finance", "accounting"]
    elif any(w in combined for w in ["iot", "sensor", "arduino", "raspberry", "mqtt"]):
        return "IoT_And_Smart_Devices", ["iot", "hardware", "sensors"]
    elif any(w in combined for w in ["devops", "deploy", "docker", "kubernetes", "github", "server", "monitor"]):
        return "DevOps_And_Cloud_Ops", ["devops", "cloud", "monitoring"]
    elif any(w in combined for w in ["ai", "chatgpt", "openai", "llm", "bot", "voice", "gemini", "rag"]):
        return "AI_And_Machine_Learning", ["ai", "llm", "automation"]
    else:
        return "General_Business_Automation", ["general", "workflow"]

def generate_platform_blueprint(platform_name):
    p = platform_name.lower()
    if p == "n8n":
        return {"platform": "n8n", "interface": "Visual Nodes", "flow": ["Webhook Trigger", "Advanced Logic", "Router", "API Action"]}
    elif p == "make.com":
        return {"platform": "Make.com", "interface": "Visual Modules", "flow": ["Watch/Trigger Module", "Router", "Filter", "Action Module"]}
    elif p == "zapier":
        return {"platform": "Zapier", "interface": "Linear Steps", "flow": ["Trigger Step", "Filter/Formatter", "Action Step"]}
    elif p == "pipedream":
        return {"platform": "Pipedream", "interface": "Serverless Code", "flow": ["HTTP Trigger", "Custom Node.js/Python", "API Request"]}
    elif p == "node-red":
        return {"platform": "Node-RED", "interface": "IoT Flows", "flow": ["Inject/Input Node", "Function Logic", "Output Node"]}
    elif p == "power automate":
        return {"platform": "Power Automate", "interface": "Cloud Flows", "flow": ["Automated Trigger", "Condition Check", "Microsoft 365 Action"]}
    else:
        return {"platform": platform_name, "flow": "Standard Pipeline"}

updated_workflows = []
platforms_list = ["n8n", "Make.com", "Zapier", "Pipedream", "Node-RED", "Power Automate"]

for item in workflows:
    title = item.get("title", "Advanced Automation Template")
    text = item.get("description", "")
    url = item.get("url", "")
    
    # إعادة تصنيف ذكية بناءً على محتوى العنوان والوصف لتغطية كافة النيتشات
    domain, tags = advanced_domain_and_tags(title, text)
    
    blueprints_dict = {plat: generate_platform_blueprint(plat) for plat in platforms_list}

    item["domain"] = domain
    item["sub_domain"] = domain
    item["tags"] = tags
    item["blueprints"] = blueprints_dict
    
    updated_workflows.append(item)

output_file = "ultimate_multi_platform_database/ultimate_6_platforms_database_enriched.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(updated_workflows, f, ensure_ascii=False, indent=4)

print(f"\n✨ تمت عملية إعادة التوزيع والتصنيف الشامل لكافة الـ {len(updated_workflows)} عنصر بنجاح تام!")
print(f"🎯 تم تصنيف العناصر عبر النيتشات المختلفة (التجارة الإلكترونية، التسويق، الـ CRM، الدعم، الذكاء الاصطناعي، وغيرها).")
print(f"📁 الملف جاهز ومحدث في: '{output_file}'")