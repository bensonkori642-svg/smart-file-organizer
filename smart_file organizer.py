import os 
import shutil
from datetime import datetime
print("====WELCOME TO SMART FILE ORGANIZER=====")

def basic_folder():
    global source_folder,log_folder_1
    source_folder=r"c:\\users\\fg\\downloads"
    log_folder_1=os.path.join(source_folder, "organizer_logs_1")
    os.makedirs(log_folder_1,exist_ok=True)
def advanced_folder():
    global source_folder,log_folder_2
    source_folder=r'c:\\users\\fg\\documents'
    log_folder_2=os.path.join(source_folder,"organizer_logs_2")
    os.makedirs(log_folder_2, exist_ok=True)


file_categories= { 
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"], 
    "Audio": [".mp3", ".wav", ".aac"], 
    "Archives": [".zip", ".rar", ".tar", ".gz"], 
    "PythonScripts": [".py"]
}
timestamp=datetime.now().strftime("%Y%M%d_%H%M%S")
global folder_path
folder_path=os.path.join(log_folder, f"log_{timestamp}.txt")

def local_action(message):
    with open(folder_path,"a") as file:
        file.write(f"{datetime.now()} - {message}")
        print(message)

def main():
    global moved_file
    moved_file=0
    for item in os.listdir(source_folder):
        item_path=os.path.join(source_folder,item)
        if os.path.isdir(item_path):
            continue
        size_category=""
        size_in_bytes=os.path.getsize(item_path)
        if size_in_bytes < 1000000:
            size_category="small"
        elif size_in_bytes < 100000000:
            size_category="medium"
        else:
            size_category="large"

        file_ext=os.path.splitext(item)[1].lower()

        target_folder="others"

    for categories,extensions in file_categories.items():
        if file_ext in extensions:
            target_folder=categories
            break
        #make target folder
        target_path=os.path.join(source_folder,target_folder,size_category)
        os.makedirs(target_path,exist_ok=True)

        final_path=os.path.join(target_path,item)
        counter=1

    #handle-duplicates
    while os.path.exists(final_path):
        name,ext =os.path.splitext(item)
        final_path=os.path.join(target_path, f"{name}_{counter}{ext}")
        counter +=1

    #move_files
    shutil.move(item_path,final_path)
    local_action(f"moved {item} to {final_path}")
    moved_file +=1 
    size_mb=size_in_bytes / (1024*1024)
    local_action(f"moved {item} of ({size_mb:.2f}mb) to {final_path}")

category="1.Basic folder\n 2.Advanced folder\n"
print(category)
choice=input("which folder do you wish to organize?")
print(choice)
while True:
    if choice=="1":
        basic_folder()
    elif choice==2:
        advanced_folder()
    else:
        print("Enter a valid input!!")



if __name__ == "__main__":
    local_action("======file_organizer_started======")
    main()
    local_action(f"moved files: {moved_file}")
    local_action("======file-organizer_completed====")





#     START
#   │
#   ▼
# [Welcome Message & User Choice]
#   │
#   ├─ Input: Basic Folder → set source_folder & log_folder
#   │
#   └─ Input: Advanced Folder → set source_folder & log_folder
#   │
#   ▼
# [Create Log File]
#   │
#   └─ log_folder/log_YYYYMMDD_HHMMSS.txt
#   │
#   ▼
# [Scan Source Folder]
#   │
#   ├─ Loop through all items in source_folder
#   │
#   └─ Ignore:
#       - Hidden files
#       - Subfolders
#   │
#   ▼
# [Get File Info]
#   │
#   ├─ file name
#   ├─ extension → classify type (Images, Documents, Videos, etc.)
#   └─ size → classify size (Small / Medium / Large)
#   │
#   ▼
# [Determine Target Folder]
#   │
#   ├─ Path: source_folder / FileType / SizeCategory
#   └─ Example: "Downloads/Images/Large/"
#   │
#   ▼
# [Create Target Folder if Not Exists]
#   │
#   └─ os.makedirs(target_path, exist_ok=True)
#   │
#   ▼
# [Handle Duplicates]
#   │
#   ├─ final_path = target_path / item
#   ├─ while os.path.exists(final_path):
#   │      rename: name_counter.ext
#   │
#   ▼
# [Move File]
#   │
#   ├─ shutil.move(item_path, final_path)
#   │
#   ▼
# [Log Action]
#   │
#   ├─ log: "{datetime} - Moved {item} ({size_MB:.2f} MB) → {final_path}"
#   │
#   ▼
# [Repeat for All Files]
#   │
#   ▼
# [Summary]
#   │
#   ├─ Total files processed
#   ├─ Files per category & size
#   ├─ Errors encountered
#   │
#   ▼
# END













