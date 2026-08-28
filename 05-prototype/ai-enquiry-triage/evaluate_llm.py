import csv
import time
from pathlib import Path

from llm_classifier import classify_enquiry_llm


def load_enquiries(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def evaluate(enquiries):
    total = len(enquiries)

    type_correct = 0
    priority_correct = 0
    department_correct = 0
    fully_correct = 0

    for index, enquiry in enumerate(enquiries, start=1):

        while True:
            try:
                result = classify_enquiry_llm(
                    enquiry["enquiry_text"]
                )
                break

            except Exception as error:
                if "429" in str(error):
                    print(
                        f"\nRate limit reached at "
                        f"{index}/{total}."
                    )
                    print("Waiting 25 seconds before retrying...\n")

                    time.sleep(25)

                else:
                    raise error

        type_match = (
            result["enquiry_type"]
            == enquiry["expected_type"]
        )

        priority_match = (
            result["priority"]
            == enquiry["expected_priority"]
        )

        department_match = (
            result["department"]
            == enquiry["expected_department"]
        )

        if type_match:
            type_correct += 1

        if priority_match:
            priority_correct += 1

        if department_match:
            department_correct += 1

        if (
            type_match
            and priority_match
            and department_match
        ):
            fully_correct += 1

        print(
            f"{index}/{total} processed: "
            f"{enquiry['enquiry_id']} -> "
            f"{result['enquiry_type']} | "
            f"{result['priority']} | "
            f"{result['department']}"
        )

        # Small delay to avoid sending requests too quickly
        time.sleep(2)

    print("\nGemini Unseen Test Evaluation")
    print("--------------------------------")
    print(f"Total enquiries: {total}")

    print(
        f"Type accuracy: "
        f"{(type_correct / total) * 100:.2f}%"
    )

    print(
        f"Priority accuracy: "
        f"{(priority_correct / total) * 100:.2f}%"
    )

    print(
        f"Department accuracy: "
        f"{(department_correct / total) * 100:.2f}%"
    )

    print(
        f"Fully correct classifications: "
        f"{(fully_correct / total) * 100:.2f}%"
    )


if __name__ == "__main__":
    current_file = Path(__file__).resolve()
    project_root = current_file.parents[2]

    dataset_path = (
        project_root
        / "04-data-and-analytics"
        / "unseen-test-enquiries.csv"
    )

    enquiries = load_enquiries(dataset_path)

    evaluate(enquiries)
