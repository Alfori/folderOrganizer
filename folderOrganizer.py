import os
import shutil
import time

def PicsDocsVid(path):

    categories = {      # jot down all the categories (folders) and their values will be the types
        "Images": [".jpg", ".png", ".jpeg", ".gif", ".bmp"],
        "Videos": [".mkv", ".mp4", ".mp5", ".avi", ".mov"],
        "Documents": [".pdf", ".pptx", ".wrd", ".docx", ".txt"],
        "ZipFiles": [".rar", ".zip", ".7z"]
    }

    for category in categories:     ## create all the folders
        os.makedirs(os.path.join(path, category), exist_ok=True)

    os.makedirs(os.path.join(path, "Others"), exist_ok=True) #exist_ok closes the popup that it already exists

    def getCategory(fileExtension):     # deciper which category it falls under (images, documents, etc)
        for category, extensions in categories.items():
            if fileExtension.lower() in extensions:
                return category
        return "Others"
    
    def is_file_downloaded(file_path, check_interval=2, check_times=5): # keeps checking the size, if its constant for longer than it sleeps for 5 more seconds
        """Check if a file is still being written to by verifying if its size remains constant."""
        initial_size = os.path.getsize(file_path)
        for _ in range(check_times):
            time.sleep(check_interval)
            new_size = os.path.getsize(file_path)
            if new_size != initial_size:
                return False
            initial_size = new_size
        return True

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            _, fileExtension = os.path.splitext(filename) #skips the first part o the split, store the extension
            category = getCategory(fileExtension)
            fileDestination = os.path.join(path, category, filename) # gets the file destination

            if is_file_downloaded(file_path):
                shutil.move(file_path, fileDestination)         # shutil gets higher commands to move
                print(f"Moved {filename} to {fileDestination}")     # moved message in terminal
            else:
                print(f"Skipping {filename}, still being downloaded.")


if __name__ == "__main__":
    folderPath = input ("Enter your file path that you want to organize:)  # JUST ENTER YOUR FILE PATH HERE
    while True:
        PicsDocsVid(folderPath)
        time.sleep(10)

# USEFUL OS FUNCTIONS
# ========================================================
# os.path.getsize(filepath)
# os.path.isfile(filepath)
# os.path.join(path, "Under 50MB", filename)
# shutil.move(filePath, destination)
# os.makedirs(os.path.join(path,category), exist_ok=True)
