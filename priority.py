# priority.py

def assign_priority(text):
    """
    Assigns priority based on keywords in the ticket text.
    High: urgent issues like crashes or downtime
    Medium: billing / login / payment issues
    Low: general inquiries
    """
    text_lower = text.lower()

    # High priority keywords
    if "crash" in text_lower or "not working" in text_lower or "down" in text_lower:
        priority = "High"
    # Medium priority keywords (billing, login issues)
    elif ("unable" in text_lower or "can't" in text_lower or "cannot" in text_lower
          or "payment" in text_lower or "charged" in text_lower 
          or "subscription" in text_lower or "deducted" in text_lower
          or "refund" in text_lower):
        priority = "Medium"
    else:
        priority = "Low"

    return priority


def correct_category(text, predicted_category):
    """
    Overrides ML predicted category for Billing and Technical tickets
    based on rule-based keywords
    """
    text_lower = text.lower()

    # Billing keywords
    billing_keywords = ["payment", "charged", "subscription", "deducted", "refund", "money"]
    if any(word in text_lower for word in billing_keywords):
        return "Billing"

    # Technical keywords
    technical_keywords = ["crash", "not working", "down", "network", "issue", "error", "problem", "setup"]
    if any(word in text_lower for word in technical_keywords):
        return "Technical"

    # Otherwise, keep ML prediction
    return predicted_category
