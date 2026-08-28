import json
import os

from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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

Return only valid JSON in this format:

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
    response = client.responses.create(
        model="gpt-5.4-nano",
        instructions=SYSTEM_PROMPT,
        input=text
    )

    return json.loads(response.output_text)


if __name__ == "__main__":
    sample = (
        "Our users are locked out of the platform "
        "and work has stopped."
    )

    result = classify_enquiry_llm(sample)

    print(result)
