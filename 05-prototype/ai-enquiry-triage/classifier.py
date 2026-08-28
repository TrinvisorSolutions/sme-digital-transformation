import csv

from classifier import classify_enquiry


def load_enquiries(file_path):
    enquiries = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            enquiries.append(row)

    return enquiries


def evaluate(enquiries):
    total = len(enquiries)

    type_correct = 0
    priority_correct = 0
    department_correct = 0
    fully_correct = 0

    for enquiry in enquiries:
        result = classify_enquiry(enquiry["enquiry_text"])

        type_match = result["enquiry_type"] == enquiry["expected_type"]
        priority_match = result["priority"] == enquiry["expected_priority"]
        department_match = result["department"] == enquiry["expected_department"]

        if type_match:
            type_correct += 1

        if priority_match:
            priority_correct += 1

        if department_match:
            department_correct += 1

        if type_match and priority_match and department_match:
            fully_correct += 1

    print("Baseline Classifier Evaluation")
    print("------------------------------")
    print(f"Total enquiries: {total}")
    print(f"Type accuracy: {(type_correct / total) * 100:.2f}%")
    print(f"Priority accuracy: {(priority_correct / total) * 100:.2f}%")
    print(f"Department accuracy: {(department_correct / total) * 100:.2f}%")
    print(f"Fully correct classifications: {(fully_correct / total) * 100:.2f}%")


if __name__ == "__main__":
    dataset_path = "../../04-data-and-analytics/sample-enquiries.csv"

    enquiries = load_enquiries(dataset_path)
    evaluate(enquiries)
