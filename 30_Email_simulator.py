import time
import random


def send_email(recipient):
    if random.random() < 0.9:
        return True
    return False


def batch_send(emails):
    success_count = 0
    failure_count = 0

    print("Starting batch email send...\n")

    for index, email in enumerate(emails, start=1):
        print(f"[{index}/{len(emails)}] Sending to {email}...")

        if send_email(email):
            print("Sent successfully")
            success_count += 1
        else:
            print("Failed to send")
            failure_count += 1

    print("\n===== Batch Summary =====")
    print(f"Total Emails : {len(emails)}")
    print(f"Successful   : {success_count}")
    print(f"Failed       : {failure_count}")
    print("=========================")


def main():
    email_list = [
        "user1@example.com",
        "user2@example.com",
        "user3@example.com",
        "user4@example.com",
    ]

    batch_send(email_list)

if __name__ == "__main__":
    main()