# AI Enquiry Triage

## Objective

Use AI to support faster and more consistent classification of incoming customer enquiries before they enter the wider workflow.

The AI component acts as a decision-support layer. It does not replace human oversight for high-risk, ambiguous or commercially sensitive cases.

## Input

The model receives the text of a customer enquiry.

Example:

> "Hi, we are interested in your enterprise service for 40 users and would like pricing and implementation details."

## Proposed AI Outputs

The model returns structured fields such as:

* Enquiry Type
* Customer Intent
* Priority
* Recommended Department
* Suggested Next Action
* Confidence Score
* Human Review Required

## Example Classification

```json
{
  "enquiry_type": "Sales",
  "customer_intent": "Pricing and implementation enquiry",
  "priority": "High",
  "recommended_department": "Sales",
  "suggested_next_action": "Assign to account executive and create follow-up task",
  "confidence_score": 0.94,
  "human_review_required": false
}
```

## Example Categories

### Enquiry Type

* Sales
* Customer Support
* Billing
* Complaint
* Partnership
* General Enquiry
* Technical Support

### Priority

* Low
* Medium
* High
* Urgent

## Routing Logic

```text
Incoming Enquiry
      ↓
AI Classification
      ↓
Confidence Check
      ↓
High Confidence → Automated Routing
      ↓
Low Confidence → Human Review
```

## Human-in-the-Loop Control

AI should not automatically make all routing decisions.

Human review should be triggered when:

* Confidence is below an agreed threshold
* The enquiry contains sensitive information
* The request is commercially significant
* The model identifies conflicting categories
* The enquiry is classified as a complaint
* The request falls outside known categories

## Prompt Design

A production prompt should instruct the model to:

1. Analyse only the information contained in the enquiry
2. Select from predefined categories
3. Return a structured response
4. Avoid inventing missing information
5. Flag uncertainty
6. Request human review where confidence is low

## Model Evaluation

The AI component should be tested using a labelled enquiry dataset.

Potential evaluation measures include:

* Classification accuracy
* Routing accuracy
* False escalation rate
* Human override rate
* Average response time
* Percentage of enquiries processed automatically

## Governance Considerations

The design should consider:

* Data privacy
* Access controls
* Model logging
* Prompt versioning
* Human override capability
* Error monitoring
* Bias testing
* Data retention
* Model performance over time

## Business Value

If implemented effectively, AI-assisted triage could support:

* Faster enquiry routing
* Reduced manual classification
* More consistent prioritisation
* Improved response times
* Better workload distribution
* Earlier identification of urgent enquiries

## Prototype Opportunity

The next stage will create a small working prototype using synthetic enquiry data.

The prototype will classify customer enquiries and return structured outputs that can later feed an automated workflow.
