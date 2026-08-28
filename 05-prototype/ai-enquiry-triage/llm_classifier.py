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

Return only valid JSON in this format:

{
  "enquiry_type": "",
  "priority": "",
  "department": ""
}

Classify based on meaning rather than individual keywords.
"""


def classify_enquiry_llm(text):
    prompt = f"""
{SYSTEM_PROMPT}

Customer enquiry:

{text}
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    output = interaction.output_text.strip()

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
