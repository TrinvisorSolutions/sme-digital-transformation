def classify_enquiry(text):
    text = text.lower()

    # Partnership should be checked before Sales because
    # partnership messages may also contain phrases such as "interested in".
    if any(phrase in text for phrase in [
        "partnership",
        "strategic partnership",
        "commercial partnership",
        "joint initiative",
        "technology partner",
        "technology partners",
        "referral partner",
        "sponsoring",
        "sponsorship",
        "industry event"
    ]):
        return {
            "enquiry_type": "Partnership",
            "priority": "Medium",
            "department": "Management"
        }

    # Complaints and escalations
    if any(phrase in text for phrase in [
        "complaint",
        "cancel",
        "cancelling",
        "not resolved",
        "unresolved",
        "not received a response",
        "have still not received",
        "escalate",
        "escalated",
        "unhappy",
        "affecting our customers"
    ]):
        priority = "Urgent" if any(phrase in text for phrase in [
            "affecting our customers",
            "critical",
            "severe"
        ]) else "High"

        return {
            "enquiry_type": "Complaint",
            "priority": priority,
            "department": "Customer Service"
        }

    # Billing
    if any(phrase in text for phrase in [
        "invoice",
        "billing",
        "charged",
        "purchase order",
        "payment",
        "outstanding balance"
    ]):
        if any(phrase in text for phrase in [
            "charged twice",
            "outstanding balance"
        ]):
            priority = "High"
        elif any(phrase in text for phrase in [
            "copy of our latest invoice",
            "send us a copy"
        ]):
            priority = "Low"
        else:
            priority = "Medium"

        return {
            "enquiry_type": "Billing",
            "priority": priority,
            "department": "Finance"
        }

    # Technical Support
    if any(phrase in text for phrase in [
        "cannot log in",
        "unable to access",
        "system error",
        "showing an error",
        "not loading",
        "api",
        "technical",
        "stopped working",
        "system has stopped",
        "cannot process",
        "unable to process"
    ]):
        if any(phrase in text for phrase in [
            "cannot log in",
            "unable to access",
            "affecting operations",
            "cannot process",
            "system has stopped",
            "several users"
        ]):
            priority = "Urgent"
        elif "api" in text:
            priority = "Medium"
        else:
            priority = "High"

        return {
            "enquiry_type": "Technical Support",
            "priority": priority,
            "department": "Technical Support"
        }

    # Sales
    if any(phrase in text for phrase in [
        "pricing",
        "quotation",
        "proposal",
        "enterprise package",
        "demo",
        "moving our team",
        "services for organisations",
        "services for organizations",
        "business solution",
        "interested in your enterprise",
        "interested in pricing"
    ]):
        if any(phrase in text for phrase in [
            "quotation",
            "proposal",
            "implementation proposal",
            "moving our team"
        ]):
            priority = "High"
        else:
            priority = "Medium"

        return {
            "enquiry_type": "Sales",
            "priority": priority,
            "department": "Sales"
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
