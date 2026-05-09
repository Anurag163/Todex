import sys
import json
import datetime
import os
import pandas as pd


pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr',False)

filename = "to_do.json" 
def add_todo():
    task_to_add = sys.argv[2]
    current_time = str(datetime.datetime.now())


    new_id=1

    # 1. Initialize an empty list
    tasks = []

    # 2. READ: If the file has data, let json.load handle the structure natively (NO BRACKETS!)
    if os.path.exists(filename) and os.stat(filename).st_size > 0:

        df=pd.read_json(filename)
        new_id=int(df['id'].max())+1

        with open(filename, "r") as f:
            tasks = json.load(f) 
    data_to_add = {
        "id":  new_id,
        "decription": task_to_add,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time
    }      
    # 3. MODIFY: Append the new dictionary to the list
    tasks.append(data_to_add)

    # 4. WRITE: Dump the entire list back to the file
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)


def list_all_items():
    if os.path.exists(filename) and os.stat(filename).st_size>0:
        df=pd.read_json(filename)
        print(df)
    else:
        print("table data not present or file itself not present")

def list_done():
    if os.path.exists(filename) and os.stat(filename).st_size>0:
        df=pd.read_json(filename)
        df_done=df[df['status']=='done']
        print(df_done)
    else:
        print("table data not present or file itself not present")

def list_todo():
    if os.path.exists(filename) and os.stat(filename).st_size>0:
        df=pd.read_json(filename)
        df_done=df[df['status']=='todo']
        print(df_done)
    else:
        print("table data not present or file itself not present")

def delete_list_item():
    if os.path.exists(filename) and os.stat(filename).st_size>0:
        with open(filename,"r") as f:
            tasks=json.load(f)
            for i,j in enumerate(tasks):
                if int(j['id'])==int(sys.argv[2]):
                    del tasks[i]
                    print(f"deleted task with id  {sys.argv[2]}")

        if len(tasks)==0:
            os.remove(filename)
        else:        
            with open(filename,'w') as f:
                json.dump(tasks,f, indent=2) 

def update_list_items():
    if os.path.exists(filename) and os.stat(filename).st_size>0:
        with open(filename,"r") as f:
            tasks=json.load(f)
            for i,j in enumerate(tasks):
                if int(j['id'])==int(sys.argv[2]):
                    tasks[i]['decription']=str(sys.argv[3])
                    tasks[i]['updatedAt']=str(datetime.datetime.now())
                    break
        with open(filename,"w") as f:
            json.dump(tasks,f,indent=2)

def mark_in_progress_item():

    if os.path.exists(filename) and os.stat(filename).st_size>0:
        with open(filename,"r") as f:
            tasks=json.load(f)
            for i,j in enumerate(tasks):
                if int(j['id'])==int(sys.argv[2]):
                    tasks[i]['status']='in-progress'
                    tasks[i]['updatedAt']=str(datetime.datetime.now())
                    break
        with open(filename,"w") as f:
            json.dump(tasks,f,indent=2)

def mark_done_item():

    if os.path.exists(filename) and os.stat(filename).st_size>0:
        with open(filename,"r") as f:
            tasks=json.load(f)
            for i,j in enumerate(tasks):
                if int(j['id'])==int(sys.argv[2]):
                    tasks[i]['status']='done'
                    tasks[i]['updatedAt']=str(datetime.datetime.now())
                    break

        with open(filename,"w") as f:
            json.dump(tasks,f,indent=2)

def main():
    if sys.argv[1].lower() == "add":
        add_todo()
    elif sys.argv[1].lower()=="list" and len(sys.argv)<=2:
        list_all_items()

    elif sys.argv[1].lower()=="list" and  len(sys.argv)>2 and sys.argv[2].lower()=="done":
        list_done()

    elif sys.argv[1].lower()=="list" and  len(sys.argv)>2 and sys.argv[2].lower()=="todo"  :
        list_todo()

    elif sys.argv[1].lower()=="delete" and len(sys.argv)<=3:
        delete_list_item()
    elif sys.argv[1].lower()=="update" and len(sys.argv)<=4:
        update_list_items()
    elif sys.argv[1].lower()=="mark-in-progress" and  len(sys.argv)<=3:
        mark_in_progress_item()
    elif sys.argv[1].lower()=="mark-done" and  len(sys.argv)<=3:
        mark_done_item()
    else :
        print("Wrong option used")

if __name__ == "__main__":
    main()