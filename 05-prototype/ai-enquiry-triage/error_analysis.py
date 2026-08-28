import csv
from pathlib import Path

from classifier import classify_enquiry


def load_enquiries(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def analyse_errors(enquiries):
    errors = []

    for enquiry in enquiries:
        result = classify_enquiry(enquiry["enquiry_text"])

        type_match = result["enquiry_type"] == enquiry["expected_type"]
        priority_match = result["priority"] == enquiry["expected_priority"]
        department_match = result["department"] == enquiry["expected_department"]

        if not (type_match and priority_match and department_match):
            errors.append({
                "enquiry_id": enquiry["enquiry_id"],
                "text": enquiry["enquiry_text"],
                "expected_type": enquiry["expected_type"],
                "predicted_type": result["enquiry_type"],
                "expected_priority": enquiry["expected_priority"],
                "predicted_priority": result["priority"],
                "expected_department": enquiry["expected_department"],
                "predicted_department": result["department"]
            })

    return errors


if __name__ == "__main__":
    current_file = Path(__file__).resolve()
    project_root = current_file.parents[2]

    dataset_path = (
        project_root
        / "04-data-and-analytics"
        / "sample-enquiries.csv"
    )

    enquiries = load_enquiries(dataset_path)
    errors = analyse_errors(enquiries)

    print(f"\nTotal misclassified enquiries: {len(errors)}")
    print("=" * 70)

    for error in errors:
        print(f"\n{error['enquiry_id']}: {error['text']}")
        print(
            f"Type: {error['expected_type']} → {error['predicted_type']}"
        )
        print(
            f"Priority: {error['expected_priority']} → "
            f"{error['predicted_priority']}"
        )
        print(
            f"Department: {error['expected_department']} → "
            f"{error['predicted_department']}"
        )
