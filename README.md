🚀 Task Tracker CLI
A lightweight, efficient Command Line Interface (CLI) application built with Python to manage your daily productivity. This tool uses local JSON storage to track tasks through their entire lifecycle without the need for a complex database.

✨ Key Features
- Show All Tasks: Display every task in your collection using Show_Task.
- Filter by Status: View only tasks with spesific status.
- Add New Tasks: Create tasks with specific descriptions and initial statuses using Add_Task ("task name") ("status").
- Update Task Content: Edit the description of an existing task via Update_Task ("task id") ("new task").
- Update Task Status: Transition tasks between todo, in-progress, or done using Update_Status ("task id") ("new status").
- Delete with Re-indexing: Remove tasks by ID using Delete_Task ("task id"). The system automatically re-sequences remaining IDs to maintain a clean list.
- Persistent Storage: All data is saved in a local task_tracker.json file, ensuring your data remains even after closing the app.

🛠️ Technical Stack
Language: Python 3.x
Data Format: JSON (JavaScript Object Notation)
Modules: json for data persistence, os/sys for CLI arguments.
