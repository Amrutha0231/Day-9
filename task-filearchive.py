import shutil

source_directory = input("Enter the directory to archive: ")

destination_zip = input("Enter the destination zip file: ")

try:
    shutil.make_archive(destination_zip, 'zip', source_directory)
    print(f"Directory archived successfully to {destination_zip}.zip")
except Exception as e:
    print(f"An error occurred: {str(e)}")
