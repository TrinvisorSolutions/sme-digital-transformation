# Requirements Traceability Matrix

## Purpose

The Requirements Traceability Matrix links identified business problems to business requirements, functional requirements and user stories.

This ensures that each proposed capability can be traced back to a genuine business need.

It also helps prevent unnecessary features from being introduced without a clear purpose.

## Traceability Matrix

| Business Problem                    | Business Requirement                   | Functional Requirement             | User Story                              | Priority    |
| ----------------------------------- | -------------------------------------- | ---------------------------------- | --------------------------------------- | ----------- |
| Fragmented customer information     | BR-01 Centralised Customer Information | FR-01 Customer Record Creation     | US-01 Create a Customer Record          | Must Have   |
| Duplicate customer records          | BR-01 Centralised Customer Information | FR-02 Duplicate Record Detection   | US-02 Prevent Duplicate Records         | Must Have   |
| Incomplete and inconsistent records | BR-07 Data Quality Controls            | FR-03 Mandatory Data Validation    | US-01 Create a Customer Record          | Must Have   |
| No consistent onboarding process    | BR-02 Standardised Customer Onboarding | FR-04 Customer Status Tracking     | US-03 Track Customer Progress           | Must Have   |
| Unclear accountability              | BR-04 Improved Workflow Visibility     | FR-05 Process Ownership            | US-04 Assign Process Ownership          | Must Have   |
| Repetitive administrative work      | BR-03 Reduced Manual Data Entry        | FR-06 Automated Task Creation      | US-05 Automate Follow-Up Tasks          | Should Have |
| Heavy reliance on email             | BR-08 Appropriate Workflow Automation  | FR-07 Notifications and Alerts     | US-06 Receive Workflow Notifications    | Should Have |
| Limited customer history visibility | BR-01 Centralised Customer Information | FR-08 Customer Interaction History | US-07 View Customer Interaction History | Must Have   |
| Difficult record retrieval          | BR-01 Centralised Customer Information | FR-09 Search and Filtering         | US-07 View Customer Interaction History | Must Have   |
| Uncontrolled information access     | BR-09 Role-Based Access                | FR-10 Role-Based Permissions       | US-10 Control Access                    | Must Have   |
| Limited management visibility       | BR-05 Reliable Management Reporting    | FR-11 Management Dashboard         | US-08 Access Management KPIs            | Should Have |
| Inconsistent KPI definitions        | BR-06 Consistent KPI Definitions       | FR-12 Standard Reporting           | US-08 Access Management KPIs            | Must Have   |
| Need for approved data extraction   | BR-05 Reliable Management Reporting    | FR-13 Data Export                  | US-08 Access Management KPIs            | Should Have |
| Poor visibility of data issues      | BR-07 Data Quality Controls            | FR-14 Data Quality Monitoring      | US-09 Monitor Data Quality              | Should Have |
| Limited change history              | BR-09 Role-Based Access                | FR-15 Workflow Audit Trail         | US-10 Control Access                    | Must Have   |
| Disconnected systems                | BR-10 Scalable Operating Model         | FR-16 Integration Capability       | Future integration story                | Should Have |

## Why Traceability Matters

Traceability supports:

* Scope control
* Impact assessment
* Testing
* Stakeholder validation
* Change management
* Benefits realisation
* Delivery governance

If a requirement changes, the matrix helps identify which downstream user stories, processes or solution components may also need to change.

## Consulting Observation

A requirement should not exist simply because a stakeholder requests a feature.

The consultant should be able to explain:

1. Which business problem the requirement addresses
2. Why the requirement is necessary
3. Which capability will satisfy it
4. How it will be tested
5. What business benefit it is expected to deliver

This helps maintain alignment between business needs and solution delivery.
