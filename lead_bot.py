import json

def score_lead(lead_data):
    # Mock predictive scoring (real version uses LLM + property API)
    score = 0
    if lead_data.get('years_owned', 0) > 8: score += 35   # Motivated seller signal
    if lead_data.get('equity_estimate', 0) > 150000: score += 30
    if 'urgent' in lead_data.get('notes', '').lower(): score += 20
    # LLM call (Grok API ready): "Analyze this lead for seller intent..."
    return min(score, 100)

def generate_compliant_outreach(lead, channel="sms"):
    # AI-generated, consent-aware template
    prompt = f"Generate {channel} message for {lead['name']} about {lead['property']}. Keep compliant, personal, include STOP opt-out."
    # In real: call Grok/OpenAI
    return "Hi [Name], saw your interest in [Prop]. What's your timeline? Reply STOP to opt out."

# Usage demo
sample_lead = {"name": "Test Seller", "property": "Tulsa 3-bed", "years_owned": 12, "equity_estimate": 180000, "notes": "urgent move"}
print("Lead score:", score_lead(sample_lead))
print("Outreach:", generate_compliant_outreach(sample_lead)) 