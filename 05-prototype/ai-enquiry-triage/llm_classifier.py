import json
import os

from google import genai


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


SYSTEM_PROMPT = """
You are an enquiry triage classifier for a business.

Classify each enquiry into exactly one enquiry type:

- Sales
- Technical Support
- Billing
- Complaint
- Partnership
- General Enquiry

Assign exactly one priority:

- Low
- Medium
- High
- Urgent

Assign exactly one department:

- Sales
- Technical Support
- Finance
- Customer Service
- Management

Return ONLY valid JSON in this format:

{
  "enquiry_type": "",
  "priority": "",
  "department": ""
}

Sales:
Pricing, demonstrations, quotations, proposals and buying interest.

Technical Support:
System failures, login issues, API questions, errors and technical problems.

Billing:
Invoices, payments, charges, purchase orders and billing details.

Complaint:
Dissatisfaction, unresolved service issues, escalation requests or cancellation caused by poor service.

Partnership:
Sponsorship, referral relationships, commercial partnerships, joint initiatives and collaboration.

General Enquiry:
General information that does not clearly belong to another category.

Priority guidance:

Urgent:
Business operations are significantly disrupted, customers are being affected or immediate action is clearly required.

High:
Important issue requiring prompt attention.

Medium:
Normal business request requiring follow-up.

Low:
Informational or non-time-sensitive request.

Classify based on meaning rather than individual keywords.
"""


def classify_enquiry_llm(text):
    prompt = f"""
{SYSTEM_PROMPT}

Customer enquiry:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    output = response.text.strip()

    if output.startswith("```json"):
        output = output[7:]

    if output.startswith("```"):
        output = output[3:]

    if output.endswith("```"):
        output = output[:-3]

    return json.loads(output.strip())


if __name__ == "__main__":
    sample = (
        "Our users are locked out of the platform "
        "and work has stopped."
    )

    result = classify_enquiry_llm(sample)

    print(result)
