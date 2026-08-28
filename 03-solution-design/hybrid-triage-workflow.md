# Hybrid AI Triage Workflow

## Proposed Flow

```text
Incoming Enquiry
       ↓
Basic Validation
       ↓
Deterministic Rules
       ↓
High-confidence match?
   ↙              ↘
 Yes              No
 ↓                 ↓
Route          LLM Classification
                  ↓
             Confidence Check
              ↙        ↘
           High        Low
            ↓           ↓
          Route      Human Review
             \         /
              \       /
               ↓     ↓
            CRM Update
               ↓
        Task / Notification
               ↓
        Dashboard & Audit Log
