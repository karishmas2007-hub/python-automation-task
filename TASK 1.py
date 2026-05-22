import os

try:
    folder_name = input("Enter folder name: ")

    # Create folder
    os.mkdir(folder_name)
    print("Folder created")

    # Create file
    file_path = os.path.join(folder_name, "sample.txt")

    with open(file_path, "w") as file:
        file.write("This is internship task")

    print("File created")

    # Rename file
    new_file_path = os.path.join(folder_name, "renamed.txt")
    os.rename(file_path, new_file_path)

    print("File renamed")

    # Log file
    with open("log.txt", "a") as log:
        log.write("Operation completed successfully\n")

except Exception as e:
    print("Error:", e)
