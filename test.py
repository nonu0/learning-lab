extension_to_folder = {
    ".mp4": "Videos",
    ".mov": "Videos",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".exe": "Applications",
    ".jpg": "Pictures",
    ".png": "Pictures",
}



print(extension_to_folder.get('Videos'))


# from pathlib import Path

# extension_to_folder = {
#     ".mp4": "Videos",
#     ".mov": "Videos",
#     ".pdf": "Documents",
#     ".docx": "Documents",
#     ".exe": "Applications",
#     ".jpg": "Pictures",
#     ".png": "Pictures",
# }

# filename = input('Enter a file name: ')

# file = Path(filename)

# extensions = file.suffix.lower()

# folder = extension_to_folder.get(extensions)
# print(folder)

# # if folder:
# #     print(f"{filename} should go into {folder}")