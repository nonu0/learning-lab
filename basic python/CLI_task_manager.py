tasks = []

def show_menu():
    print('Task Menu List')
    print('Type 1 to add task')
    print('Type 2 to view tasks')
    print('Type 3 to update task status')
    print('Type 4 to delete tasks')
    print('Type 5 to exit application')
    

def add_task():
    task = input("Enter a task: ")   
    tasks.append({'task': {task}, 'done':{False}})
    print(f"Task '{task}' added successfully!")
    
def view_tasks():
    if not tasks:
        print('No tasks found!')
        return
    for task in enumerate(tasks, start=1):
        print(task)
        
def mark_done():
    if not tasks:
        print('No tasks found!')
        return
    index = int(input('Please enter task number to mark as done: ')) - 1
    if 0 <= index < len(tasks):
        task = tasks[index]['done'] = True
        print(tasks)
    else:
        print('Please provide a valid number')
        

def delete():
    if not tasks:
        print('No tasks found!')
        return 
    index = int(input('Please enter number of task to be deleted: ')) - 1
    print(index)
    if 0 <= index < len(tasks):
        task = tasks.pop(index)
        print(f"{task['task']} deleted successfully!")
        print(tasks)
    else:
        print('Please provide a valid number')
        

while True:
    try:
        show_menu()
        user_value = int(input('> '))
        print(user_value)
        if user_value == 1:
            add_task()
        elif user_value == 2:
            view_tasks()
        elif user_value == 3:
            mark_done()
        elif user_value == 4:
            delete()
        elif user_value == 5:
            print('Goodbye!')
            break
    except:
        print('Please provide a valid number')