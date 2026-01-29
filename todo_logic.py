#backend receives data from forntend and stores it 
task=[]
def add_task(task_list,task):
    
    task_list.append(task)
    return
task_list=[]
add_task(task_list, task) 

#function to display task
#what will u do if frontend ask for task
def get_task(task_list):
    return task_list
task_list=[]
get_task(task_list)

#backend recieves index which it needs to delete from the exisiting task_list
index = 0
def delete_task(task_list, index):
    task_list.pop(index)
    return task_list
task_list=[]
delete_task(task_list, index)


index = 0
task = []
def update_task(task_list, task, index):
    if index < 0 or index >= len(task_list):
        return "invalid index" 
    task_list[index] = task
    return task_list
task_list = []
update_task(task_list, task, index)


    
       