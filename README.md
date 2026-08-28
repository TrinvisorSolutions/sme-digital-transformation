# SME Digital Transformation Case Study

## Overview

A simulated consulting engagement for a growing organisation with approximately **500 employees and 1,500+ active customers**.

The project demonstrates how business analysis, data, automation and AI can be combined to improve customer onboarding, enquiry handling, operational visibility and management reporting.

## Business Challenge

Rapid growth created:

* Fragmented customer information
* Duplicate records
* Manual reporting
* Email-based hand-offs
* Inconsistent onboarding
* Repetitive administration
* Limited management visibility
* Poor workflow traceability

## Proposed Solution

The target operating model combines:

**CRM + Data Validation + AI-Assisted Triage + Workflow Automation + Central Data + Management Analytics**

## Future-State Architecture

![Future-State Architecture](assets/future-state-architecture.png)

## Hybrid AI Triage Workflow

A hybrid model combines deterministic rules for predictable cases with LLM classification for more complex or ambiguous enquiries.

![Hybrid AI Triage Workflow](assets/hybrid-ai-triage-workflow.png)

## Project Results Dashboard

Performance results from testing the AI triage solution against unseen enquiries.

![Project Results Dashboard](assets/project-results-dashboard.png)

## Model Evaluation

![Rules vs LLM Classification Performance](assets/model-comparison.png)

### Key Result

On the unseen test dataset:

| Approach               | Fully Correct |
| ---------------------- | ------------: |
| Rules-Based Classifier |         37.5% |
| OpenAI LLM Classifier  |     **72.5%** |

The LLM also achieved:

* **92.5%** enquiry type accuracy
* **92.5%** routing accuracy
* **77.5%** priority accuracy

The experiment demonstrated that a rules engine could perform extremely well on familiar data while generalising poorly to new language patterns.

## Solution Components

### Business Analysis

* Stakeholder analysis
* As-Is process assessment
* Pain-point analysis
* Business and functional requirements
* User stories and acceptance criteria
* Requirements traceability

### Data & Systems

* CRM data model
* Central customer record
* Data validation
* Workflow status tracking
* Role-based access
* Reporting architecture

### AI & Automation

* Rules-based baseline classifier
* LLM enquiry classification
* Unseen test dataset
* Error analysis
* Model comparison
* Human-in-the-loop workflow
* Automated routing and task creation

## Technology

**Python | CSV | OpenAI API | CRM Design | Data Modelling | Workflow Automation | AI Classification | Git | GitHub Codespaces**

## Repository Structure

```text
01-discovery/
02-requirements/
03-solution-design/
04-data-and-analytics/
05-prototype/
assets/
```

Each folder contains supporting artefacts from discovery through solution design and prototype evaluation.

## Key Learning

The project reinforced several principles:

* Technology should address a defined business problem.
* Automation should follow process standardisation.
* Development accuracy alone is not enough to prove model quality.
* Unseen data is essential when assessing generalisation.
* Human review remains important for ambiguous or higher-risk cases.
* AI, rules and workflow automation can complement each other rather than being treated as competing approaches.

## Portfolio Note

This is a simulated consulting engagement using fictional organisational details and synthetic data.

The project was created to demonstrate practical capability across business analysis, digital transformation, data, automation, AI and solution delivery.


