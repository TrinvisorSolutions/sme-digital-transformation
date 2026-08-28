# Model Comparison

## Objective

Compare a deterministic rules-based enquiry classifier with an LLM-based classifier using the same unseen test dataset.

## Evaluation Dataset

The unseen test set contains 40 labelled enquiries using wording that was not used when tuning the rules-based classifier.

Each enquiry includes an expected:

- Enquiry type
- Priority
- Department

## Results

| Model | Type Accuracy | Priority Accuracy | Department Accuracy | Fully Correct |
|---|---:|---:|---:|---:|
| Initial Rules Baseline | 83.0% | 61.0% | 85.0% | 61.0% |
| Tuned Rules on Development Data | 100% | 100% | 100% | 100% |
| Tuned Rules on Unseen Data | 47.5% | 42.5% | 55.0% | 37.5% |
| OpenAI LLM on Unseen Data | 92.5% | 77.5% | 92.5% | 72.5% |

## Key Findings

The tuned rules engine achieved perfect performance on the development dataset but performed poorly when exposed to new wording.

This demonstrated that the rules had become overfitted to known phrases rather than learning the underlying meaning of the enquiries.

The LLM performed substantially better on the unseen test set.

Compared with the tuned rules engine on unseen data:

- Type accuracy improved from 47.5% to 92.5%
- Priority accuracy improved from 42.5% to 77.5%
- Department routing accuracy improved from 55.0% to 92.5%
- Fully correct classifications improved from 37.5% to 72.5%

## Interpretation

The results suggest that rules-based classification is suitable for simple and predictable workflows, but becomes fragile when customer language varies.

The LLM demonstrated stronger generalisation because it classified enquiries based on semantic meaning rather than predefined keyword matches.

Priority classification remained the weakest area for the LLM, indicating that urgency definitions may require further calibration.

## Recommended Architecture

A production solution should use a hybrid approach:

1. Deterministic rules for high-confidence, low-risk cases
2. LLM classification for ambiguous or language-heavy enquiries
3. Confidence thresholds
4. Human review for uncertain or sensitive cases
5. Continuous monitoring of classification quality

This balances accuracy, cost, control and operational resilience.
