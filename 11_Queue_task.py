from collections import deque

def add_task(queue):
    task = input("Enter tasks to add: ").strip()
    if task:
        queue.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def process_task(queue):
    if queue:
        task = queue.popleft()
        print(f"Processing task: {task}")
    else:
        print("Queue is empty.")

def show_queue(queue):
    if queue:
        print("\n--- Current Queue ---")
        for i, task in enumerate(queue, start=1):
            print(f"{i}. {task}")
    else:
        print("Queue is empty.")

def main():
    queue = deque()

    while True:
        print("\n1. Add Task")
        print("2. Process Task")
        print("3. Show Queue")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(queue)
        elif choice == "2":
            process_task(queue)
        elif choice == "3":
            show_queue(queue)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
