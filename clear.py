import os
import glob
import shutil
import winshell

def getDownloadsFolder() -> str:
    """Gets path to Downloads folder."""

    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    return download_folder

def clearDownloadsFolder(downloads_folder : str):
    """For every item in the downloads folder, check if item is a folder.\n
    If it is, delete recursively all content inside of it. Otherwise, delete the file."""

    for item in glob.glob(os.path.join(downloads_folder, '*')):
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.remove(item)

def clearBin():
    """Clears Bin using winshell pre-made function \"empty\".\n
    If Bin is already empty, instead of returning an error, prints \"Already empty\"."""
    
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print("Bin cleared successfully!")
    except:
        print("Bin is already Empty.")

def main():
    # Downloads section
    print("Program is starting.")
    print("Looking for Downloads folder...")
    downloads_folder = getDownloadsFolder()
    print("Downloads folder found!")
    clearDownloadsFolder(downloads_folder=downloads_folder)
    print("Downloads folder cleared successfully!")

    # Bin section
    print("Clearing Bin...")
    clearBin()

    print("Done. Press ENTER to exit program.")
    input("> ")

if __name__ == "__main__":
    main()