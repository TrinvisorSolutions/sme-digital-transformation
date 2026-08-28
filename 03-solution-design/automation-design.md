# Automation Design

## Objective

Reduce manual coordination, improve response times and create more consistent customer workflows.

## Priority Automation Use Case

The first automation focuses on **new customer enquiries**.

## Future-State Workflow

```text
New Enquiry Received
        ↓
Capture Customer Details
        ↓
Check for Duplicate Record
        ↓
Validate Required Fields
        ↓
Classify Enquiry
        ↓
Assign Department and Owner
        ↓
Create Follow-Up Task
        ↓
Send Notification
        ↓
Track Progress
        ↓
Escalate if Overdue
```

## Automation Rules

### Rule 1: New Enquiry Capture

When a new enquiry is received:

* Create or update the customer record
* Record the enquiry source
* Record the date received
* Assign an initial status

### Rule 2: Duplicate Check

Before creating a new customer:

* Compare email address
* Compare telephone number
* Compare company name

If a possible duplicate is found, flag it for review.

### Rule 3: Enquiry Routing

Route the enquiry based on defined criteria such as:

* Enquiry type
* Product or service
* Priority
* Customer segment
* Location

### Rule 4: Task Creation

Once the enquiry is assigned:

* Create a follow-up task
* Assign an owner
* Add a due date
* Link the task to the customer record

### Rule 5: Notifications

Notify the assigned user when:

* A new enquiry is assigned
* Required information is missing
* A task is approaching its due date
* A task becomes overdue

### Rule 6: Escalation

If an enquiry remains inactive beyond the defined threshold:

* Flag the record
* Notify the relevant manager
* Create an escalation task

## Automation Principles

Automation should be:

* Rules-based where possible
* Transparent
* Auditable
* Easy to maintain
* Designed around a standardised process
* Supported by appropriate human oversight

## Expected Benefits

* Faster response times
* Reduced manual follow-up
* Clearer ownership
* Fewer missed enquiries
* More consistent customer experience
* Improved management visibility
* Lower administrative effort
