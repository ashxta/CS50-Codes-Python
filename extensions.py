file_name = input("Enter the file name: ")
file_name = file_name.lower()
file_name = file_name.strip()
media_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}
for suffix, media_type in media_types.items():
    if file_name.endswith(suffix):
        print(f"{media_type}")
        break
else:
    print("application/octet-stream")
