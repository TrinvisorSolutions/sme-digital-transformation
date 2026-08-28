def classify_enquiry(text):
    text = text.lower()

    if any(word in text for word in [
        "invoice", "billing", "charged", "purchase order",
        "payment", "outstanding balance"
    ]):
        return {
            "enquiry_type": "Billing",
            "priority": "Medium",
            "department": "Finance"
        }

    if any(word in text for word in [
        "cannot log in", "system error", "not loading",
        "api", "technical", "unable to access",
        "stopped working"
    ]):
        return {
            "enquiry_type": "Technical Support",
            "priority": "High",
            "department": "Technical Support"
        }

    if any(word in text for word in [
        "complaint", "cancel", "not resolved",
        "escalate", "unhappy", "not received a response"
    ]):
        return {
            "enquiry_type": "Complaint",
            "priority": "High",
            "department": "Customer Service"
        }

    if any(word in text for word in [
        "pricing", "quotation", "proposal",
        "enterprise package", "demo",
        "moving our team", "interested in"
    ]):
        return {
            "enquiry_type": "Sales",
            "priority": "High",
            "department": "Sales"
        }

    if any(word in text for word in [
        "partnership", "sponsoring",
        "sponsorship", "joint initiative",
        "referral partner", "technology partners"
    ]):
        return {
            "enquiry_type": "Partnership",
            "priority": "Medium",
            "department": "Management"
        }

    return {
        "enquiry_type": "General Enquiry",
        "priority": "Low",
        "department": "Customer Service"
    }


if __name__ == "__main__":
    sample = "We are interested in pricing for 120 users and would like a proposal."
    result = classify_enquiry(sample)
    print(result)
