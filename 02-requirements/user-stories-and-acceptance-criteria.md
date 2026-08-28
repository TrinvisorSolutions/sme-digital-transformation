# User Stories and Acceptance Criteria

## Purpose

User stories translate requirements into practical statements from the perspective of the people who will use or depend on the solution.

A common structure is:

**As a [user], I want [capability], so that [business value].**

Acceptance criteria define the conditions that must be met for the requirement to be considered complete.

## User Story 01: Create a Customer Record

**As a Sales user, I want to create a customer record so that customer information is captured in a consistent and accessible location.**

### Acceptance Criteria

* The user can create a new customer record.
* Mandatory fields must be completed before the record can be saved.
* The system records the date the customer record was created.
* The system records the user who created the record.
* The customer is assigned a defined status.
* The customer can be assigned to an owner.

**Linked Requirements:** BR-01, FR-01, FR-03

---

## User Story 02: Prevent Duplicate Records

**As a Sales user, I want the system to identify possible duplicate customers so that multiple records are not created for the same customer.**

### Acceptance Criteria

* The system checks defined fields before a new customer record is created.
* Email address is included in duplicate checking.
* Telephone number is included in duplicate checking where available.
* Potential duplicates are displayed to the user.
* The user can review the existing record before creating a new one.
* The system does not automatically merge records without authorised review.

**Linked Requirements:** BR-01, BR-07, FR-02

---

## User Story 03: Track Customer Progress

**As a Sales Manager, I want to see the current status of each customer so that I can monitor progress and identify delays.**

### Acceptance Criteria

* Each customer has a defined status.
* Authorised users can update the status.
* The date of the status change is recorded.
* The previous status is retained within the audit history.
* Users can filter customers by status.
* Management can view the number of customers within each stage.

**Linked Requirements:** BR-02, BR-04, FR-04, FR-15

---

## User Story 04: Assign Process Ownership

**As an Operations Manager, I want each customer or task to have a named owner so that responsibility is clear.**

### Acceptance Criteria

* A customer or task can be assigned to an authorised user.
* The assigned owner is visible to relevant users.
* Ownership changes are recorded.
* Users can filter records by assigned owner.
* Unassigned records can be identified through reporting.

**Linked Requirements:** BR-04, FR-05

---

## User Story 05: Automate Follow-Up Tasks

**As a Sales user, I want follow-up tasks to be created automatically so that important customer activities are not missed.**

### Acceptance Criteria

* A follow-up task is created when a defined trigger occurs.
* The task includes a due date.
* The task is assigned to the appropriate user.
* The task can be marked as complete.
* Overdue tasks can be identified.
* Automation rules can only be changed by authorised users.

**Linked Requirements:** BR-03, BR-08, FR-06

---

## User Story 06: Receive Workflow Notifications

**As a Customer Service user, I want to receive notifications when action is required so that I can respond without relying on manual email follow-up.**

### Acceptance Criteria

* Notifications are generated for defined workflow events.
* The notification identifies the relevant customer or task.
* Notifications are sent only to appropriate users.
* Users can identify overdue actions.
* Duplicate notifications are avoided where possible.

**Linked Requirements:** BR-04, BR-08, FR-07

---

## User Story 07: View Customer Interaction History

**As a Customer Service user, I want to view previous customer interactions so that I can understand the customer's history before responding.**

### Acceptance Criteria

* Authorised users can view recorded customer interactions.
* Interaction records include date and type.
* Notes can be added to customer records.
* Historical interactions are retained.
* Access is controlled according to user permissions.

**Linked Requirements:** BR-01, BR-02, FR-08, FR-10

---

## User Story 08: Access Management KPIs

**As a Senior Manager, I want access to agreed performance indicators so that I can make timely and informed decisions.**

### Acceptance Criteria

* The dashboard displays agreed KPIs.
* KPI definitions are consistent across the organisation.
* Data is refreshed according to an agreed schedule.
* Users can view relevant reporting periods.
* Access to management reporting is role controlled.
* The source of reported data can be identified.

**Linked Requirements:** BR-05, BR-06, FR-11, FR-12

---

## User Story 09: Monitor Data Quality

**As a Data Owner, I want to identify incomplete or inconsistent records so that data quality issues can be corrected.**

### Acceptance Criteria

* Records with missing mandatory fields can be identified.
* Potential duplicate records can be reported.
* Invalid values can be flagged.
* Data quality exceptions can be reviewed by authorised users.
* Corrected records are retained within the audit trail.

**Linked Requirements:** BR-07, FR-14, FR-15

---

## User Story 10: Control Access

**As an Administrator, I want access to be managed by user role so that employees can only access the information and functions required for their responsibilities.**

### Acceptance Criteria

* Users are assigned a defined role.
* Roles determine access permissions.
* Restricted information cannot be viewed by unauthorised users.
* Administrative changes are recorded.
* Access can be removed when a user no longer requires it.

**Linked Requirements:** BR-09, FR-10, FR-15

## Definition of Ready

Before a user story enters delivery, it should have:

* A clear business objective
* A defined user
* Acceptance criteria
* Linked business and functional requirements
* Known dependencies
* Relevant data requirements
* Stakeholder agreement where required

## Definition of Done

A user story should only be considered complete when:

* Acceptance criteria have been met
* Required testing has been completed
* Relevant defects have been resolved
* Documentation has been updated
* Business stakeholders have accepted the outcome where required
* Required controls and permissions are in place
