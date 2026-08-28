# CRM Data Model

## Objective

Define the core business entities required to support customer management, onboarding, workflow automation and reporting.

## Core Entities

| Entity      | Purpose                                              |
| ----------- | ---------------------------------------------------- |
| Customer    | Stores the main customer or organisation record      |
| Contact     | Stores individual contacts linked to a customer      |
| Enquiry     | Records incoming customer interest or requests       |
| Opportunity | Tracks potential commercial value and sales progress |
| Interaction | Records calls, emails, meetings and notes            |
| Task        | Tracks actions, ownership and due dates              |
| User        | Represents employees using the system                |
| Department  | Supports routing, ownership and reporting            |

## Key Relationships

```text
Customer
   │
   ├── Contact
   │
   ├── Enquiry
   │      └── Opportunity
   │
   ├── Interaction
   │
   └── Task
          │
          └── User
```

## Example Customer Fields

* Customer ID
* Customer Name
* Customer Type
* Industry
* Status
* Account Owner
* Primary Contact
* Email
* Telephone
* Date Created
* Last Updated

## Example Enquiry Fields

* Enquiry ID
* Customer ID
* Enquiry Source
* Enquiry Type
* Priority
* Status
* Assigned Department
* Assigned User
* Date Received
* Next Action

## Example Opportunity Fields

* Opportunity ID
* Customer ID
* Estimated Value
* Stage
* Probability
* Expected Close Date
* Owner
* Status

## Data Design Principles

The model should support:

* One source of customer truth
* Clear record ownership
* Minimal duplicate data
* Consistent identifiers
* Auditability
* Reporting
* Automation
* Future integrations

## Design Consideration

Customer, contact and enquiry records should be separated rather than stored in one large table.

This improves data quality, reduces duplication and makes the model easier to scale and analyse.
