import os
import shutil

folder_path = input("Enter Folder Path: ")

if os.path.exists(folder_path):

    
    categories = ["Images", "Videos", "Audio", "Documents", "Spreadsheets", "Presentations", "Archives", "Code", "Others"]
    for category in categories:
        os.makedirs(os.path.join(folder_path, category), exist_ok=True)

  
    extension_map = {
        # Images
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
        ".gif": "Images", ".bmp": "Images", ".svg": "Images",
        ".webp": "Images", ".ico": "Images", ".tiff": "Images",

        # Videos
        ".mp4": "Videos", ".avi": "Videos", ".mov": "Videos",
        ".mkv": "Videos", ".wmv": "Videos", ".flv": "Videos",
        ".webm": "Videos", ".m4v": "Videos",

        # Audio
        ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio",
        ".aac": "Audio", ".ogg": "Audio", ".m4a": "Audio",
        ".wma": "Audio",

        # Documents
        ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
        ".txt": "Documents", ".rtf": "Documents", ".odt": "Documents",
        ".md": "Documents",

        # Spreadsheets
        ".xls": "Spreadsheets", ".xlsx": "Spreadsheets",
        ".csv": "Spreadsheets", ".ods": "Spreadsheets",

        # Presentations
        ".ppt": "Presentations", ".pptx": "Presentations",
        ".odp": "Presentations",

        # Archives
        ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
        ".tar": "Archives", ".gz": "Archives", ".iso": "Archives",

        # Code
        ".py": "Code", ".js": "Code", ".html": "Code",
        ".css": "Code", ".java": "Code", ".cpp": "Code",
        ".c": "Code", ".ts": "Code", ".json": "Code",
        ".xml": "Code", ".sql": "Code", ".php": "Code",
        ".go": "Code", ".rs": "Code", ".sh": "Code",
    }


    counts = {category: 0 for category in categories}


    files = os.listdir(folder_path)
    for file in files:
        source = os.path.join(folder_path, file)

        if not os.path.isfile(source):
            continue

        name, extension = os.path.splitext(file)
        extension = extension.lower()

        category = extension_map.get(extension, "Others")

        destination = os.path.join(folder_path, category, file)
        shutil.move(source, destination)

        counts[category] += 1
        print(f"Moved: {file}  →  {category}")

    print("\n" + "=" * 35)
    print("         ORGANIZER SUMMARY")
    print("=" * 35)
    total = 0
    for category, count in counts.items():
        if count > 0:
            print(f"  {category:<18} {count} file(s)")
            total += count
    print("-" * 35)
    print(f"  {'Total':<18} {total} file(s)")
    print("=" * 35)

else:
    print("Folder does not exist!")