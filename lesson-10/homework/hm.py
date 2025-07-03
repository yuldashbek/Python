class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for i, task in enumerate(self.tasks, 1):
            print(f"\nTask #{i}")
            print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status != "Complete"]
        if not incomplete:
            print("No incomplete tasks.")
        for i, task in enumerate(incomplete, 1):
            print(f"\nIncomplete Task #{i}")
            print(task)

    def mark_task_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Incomplete Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (e.g. 2025-07-05): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            todo_list.list_all_tasks()

        elif choice == "3":
            todo_list.list_incomplete_tasks()

        elif choice == "4":
            todo_list.list_all_tasks()
            try:
                task_num = int(input("Enter task number to mark as complete: "))
                todo_list.mark_task_complete(task_num)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting ToDo List. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()

--- ToDo List Menu ---
1. Add Task
2. List All Tasks
3. List Incomplete Tasks
4. Mark Task as Complete
5. Exit
Choose an option (1-5): 1
Enter task title: Buy groceries
Enter task description: Milk, Bread, Eggs
Enter due date (e.g. 2025-07-05): 2025-07-04
Task added successfully.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("No posts found.")
        for i, post in enumerate(self.posts, 1):
            print(f"\nPost #{i}")
            print(post)

    def display_by_author(self, author_name):
        found = False
        for i, post in enumerate(self.posts, 1):
            if post.author.lower() == author_name.lower():
                print(f"\nPost #{i}")
                print(post)
                found = True
        if not found:
            print("No posts found by that author.")

    def delete_post(self, index):
        if 1 <= index <= len(self.posts):
            removed = self.posts.pop(index - 1)
            print(f"Post '{removed.title}' deleted.")
        else:
            print("Invalid post number.")

    def edit_post(self, index, new_title, new_content):
        if 1 <= index <= len(self.posts):
            self.posts[index - 1].title = new_title
            self.posts[index - 1].content = new_content
            print("Post updated.")
        else:
            print("Invalid post number.")

    def latest_posts(self, count=3):
        if not self.posts:
            print("No posts available.")
        else:
            print(f"\n--- Latest {min(count, len(self.posts))} Posts ---")
            for i, post in enumerate(self.posts[-count:], 1):
                print(f"\nPost #{len(self.posts) - count + i}")
                print(post)

def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Edit a Post")
        print("5. Delete a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(Post(title, content, author))
            print("Post added.")

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.display_by_author(author)

        elif choice == "4":
            blog.list_all_posts()
            try:
                idx = int(input("Enter post number to edit: "))
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                blog.edit_post(idx, new_title, new_content)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            blog.list_all_posts()
            try:
                idx = int(input("Enter post number to delete: "))
                blog.delete_post(idx)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            blog.latest_posts()

        elif choice == "7":
            print("Exiting Blog. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()

--- Blog Menu ---
1. Add Post
2. List All Posts
3. Display Posts by Author
4. Edit a Post
5. Delete a Post
6. Show Latest Posts
7. Exit
Choose an option (1-7): 1
Enter post title: My First Blog
Enter post content: This is a simple blog post.
Enter author name: John
Post added.

class Account:
    def __init__(self, acc_number, holder_name, balance=0.0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient balance. Withdrawal denied.")

    def __str__(self):
        return f"Account Number: {self.acc_number}\nHolder: {self.holder_name}\nBalance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc_number, holder_name, initial_balance=0.0):
        if acc_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[acc_number] = Account(acc_number, holder_name, initial_balance)
            print("Account created successfully.")

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def check_balance(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if not sender:
            print("Sender account not found.")
        elif not receiver:
            print("Receiver account not found.")
        elif amount > sender.balance:
            print("Insufficient funds for transfer.")
        else:
            sender.withdraw(amount)
            receiver.deposit(amount)
            print(f"Transferred ${amount:.2f} from {from_acc} to {to_acc}.")

    def show_details(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            print(account)
        else:
            print("Account not found.")
