from pathlib import Path

extension_to_folder = {
    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",

    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".doc": "Documents",
    ".xlsx": "Documents",
    ".json": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".csv": "Documents",
    ".jsonl": "Documents",
    ".html": "Documents",
    ".pptx": "Documents",

    # Applications
    ".exe": "Applications",
    ".msi": "Applications",

    # Pictures
    ".jpeg": "Pictures",
    ".jpg": "Pictures",
    ".png": "Pictures",
    ".svg": "Pictures",

    # Archives
    ".zip": "zip files",
}


def create_folder(folder_name: str) -> Path:
    path = Path.home() / 'Downloads' / 'Organized' / folder_name
    new_path = path.mkdir(parents=True,exist_ok=True)
    print('new_path',new_path)
    # print(new_path)
    return path

def final(folder_name: str, filename: str):
    new_path = create_folder(folder_name)
    target_path = Path(new_path / filename)
    # print('target_path',target_path)
    return target_path

def move_file(source_folder_path: str):
    folder_path = Path(source_folder_path)
    if not folder_path.is_dir():
        print('Please provide a valid folder link')
    try:
        for path in folder_path.iterdir():
            if not path.is_file():
                print('Not a file, skipping')
                continue
            name = path.name
            ext = path.suffix.lower()
            folder = extension_to_folder.get(ext)
            target_path = final(folder,name)
            print('folder',target_path)
            # Path.rename(path, target_path)
            # if ext == '.mp4' or ext == '.MOV':
            #     target_path = final('Videos', name)
            #     Path.rename(path, target_path)
            # elif ext == '.pdf' or ext == '.docx' or ext == '.doc' or ext == '.xlsx' or ext == '.json' or ext == '.txt' or ext == '.md' or ext == '.csv' or ext == '.jsonl' or ext == '.html' or ext == '.pptx':
            # # elif ext == extension_to_folder.get()    
            #     target_path = final('Documents', name)
            #     Path.rename(path, target_path)
            # elif ext == '.exe' or ext == '.msi' or ext == '.xz' or ext == '.msix':
            #     target_path = final('Applications', name)
            #     Path.rename(path, target_path)
            # elif ext == '.jpeg' or ext == '.jpg' or ext == '.png' or ext == '.svg':
            #     target_path = final('Pictures', name)
            #     Path.rename(path, target_path)
            # elif ext == '.zip':
            #     target_path = final('zip files', name)
            #     Path.rename(path, target_path)
    except Exception as e:
        print(e)
    # return target_path
    
download_folder = r"C:\Users\pc\Downloads"
move_file(download_folder)

