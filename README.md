# smart-file-organizer
the smart file organizer arranges files accordingly...ie.separates file according to the type of file and in addition; according to the size of the item in the file.

   
   START
   │
   ▼
 [Welcome Message & User Choice]
   │
   ├─ Input: Basic Folder → set source_folder & log_folder
   │
   └─ Input: Advanced Folder → set source_folder & log_folder
   │
   ▼
 [Create Log File]
   │
   └─ log_folder/log_YYYYMMDD_HHMMSS.txt
   │
   ▼
 [Scan Source Folder]
   │
   ├─ Loop through all items in source_folder
   │
   └─ Ignore:
       - Hidden files
       - Subfolders
   │
   ▼
 [Get File Info]
   │
   ├─ file name
   ├─ extension → classify type (Images, Documents, Videos, etc.)
   └─ size → classify size (Small / Medium / Large)
   │
   ▼
 [Determine Target Folder]
   │
   ├─ Path: source_folder / FileType / SizeCategory
   └─ Example: "Downloads/Images/Large/"
   │
   ▼
 [Create Target Folder if Not Exists]
   │
   └─ os.makedirs(target_path, exist_ok=True)
   │
   ▼
 [Handle Duplicates]
   │
   ├─ final_path = target_path / item
   ├─ while os.path.exists(final_path):
   │      rename: name_counter.ext
   │
   ▼
 [Move File]
   │
   ├─ shutil.move(item_path, final_path)
   │
   ▼
 [Log Action]
   │
   ├─ log: "{datetime} - Moved {item} ({size_MB:.2f} MB) → {final_path}"
   │
   ▼
 [Repeat for All Files]
   │
   ▼
 [Summary]
   │
   ├─ Total files processed
   ├─ Files per category & size
   ├─ Errors encountered
   │
   ▼
 END
