import json
import os
import sys

Task_tracker="task_tracker.json"

if not os.path.exists(Task_tracker):
    with open(Task_tracker,"w") as f:
        json.dump([],f)

def add_task(new_task,status="todo"):
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    new_data={
        "id" : len(task)+1,
        "description" : new_task,
        "status" : status
    }
    task.append(new_data)

    with open(Task_tracker,"w") as f:
        json.dump(task,f,indent=4)
    print(f"The {new_task} Task Has Been Successfully Added With {status} Status!")

def update(id,task_update):
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    id_update=task[int(id)-1]
    id_update["description"]=task_update
    
    with open(Task_tracker,"w") as f:
        json.dump(task,f,indent=4)
    print(f"The Task Has Been Successfully Updated!")

def update_status(id,status_update):
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    id_update=task[int(id)-1]
    id_update["status"]=status_update

    with open(Task_tracker,"w") as f:
        json.dump(task,f,indent=4)
    print(f"The Task Status Has Been Successfully Updated!")


def delete(id):
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    if not task:
        print("No Tasks Found!")
    elif 0 < int(id) <= len(task):
        task.pop(int(id)-1)
        for j in task:
            other_id=int(j["id"])
            if other_id+1 > int(id):
                j["id"]=other_id-1
        print(f"The Task Has Been Successfully Deleted!")
    else:
        print("Error! ID is out of range.")

    with open(Task_tracker,"w") as f:
        json.dump(task,f,indent=4)

def show_task():
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    if not task:
        print("No Tasks Found!")
    else:
        print("My Tasks : ")
        for k in task:
            id=k["id"]
            description=k["description"]
            status=k["status"]
            print(f"ID :{id} | Description : {description} | Status : {status}")

def show_todo():
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    print("List Todo Task")
    if task:
        for i in task :
            ID=i["id"]
            description=i["description"]
            if i["status"]=="todo":
                print(f"ID : {ID} | Description : {description}")
    else:
        print("There are no tasks with todo status!")

def show_in_progress():
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    print("List In Progress Task")
    if task:
        for i in task :
            ID=i["id"]
            description=i["description"]
            if i["status"]=="in progress":
                print(f"ID : {ID} | Description : {description}")
    else:
        print("There are no tasks with in progress status!")

def show_done():
    with open(Task_tracker,"r") as f:
        task=json.load(f)
    print("List Done Task")
    if task:
        for i in task :
            ID=i["id"]
            description=i["description"]
            if i["status"]=="done":
                print(f"ID : {ID} | Description : {description}")
    else:
        print("There are no tasks with in progress status!")

print("""INSTRUCTION:
1. Show Task      --> "Show_Task"
2. Show Todo Task --> "Show_Todo_Task"
3. Add Task       --> "Add_Task ("new task") ("status <todo, in progress, done>")"
4. Update Task    --> "Update_Task ("task id") ("new task")"
5. Update Status  --> "Update_Status ("task id") ("new status")"
6. Delete Task    --> "Delete_Task ("task id")"
""")

if len(sys.argv)>1:
    order = sys.argv[1]

    if order == "Add_Task":
        new=sys.argv[2]
        if len(sys.argv)>3:
            current_status=sys.argv[3]
            add_task(new,current_status)
            show_task()
        else:
            add_task(new)
            show_task()
    elif order == "Update_Task":
        if len(sys.argv)>=4:
            id=sys.argv[2]
            task_update=sys.argv[3]
            update(id,task_update)
            show_task()
        else:
            print("Order invalid!")
    elif order == "Update_Status":
        if len(sys.argv)>=4:
            id=sys.argv[2]
            status_update=sys.argv[3]
            update_status(id,status_update)
            show_task()
        else:
            print("Order invalid!")
    elif order == "Show_Task":
        show_task()
    elif order == "Show_Todo_Task":
        show_todo()
    elif order == "Show_In_Progress_Task":
        show_in_progress()
    elif order == "Show_Done_Task":
        show_done()
    elif order == "Delete_Task":
        id=sys.argv[2]
        delete(id)
        show_task()
    else:
        print("Your order is not valid! Please follow the instruction!")