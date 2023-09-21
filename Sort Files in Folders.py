import os
import shutil

path = 'C:\\Users\\ashley\\Downloads\\'

names = os.listdir(path)

folder_name = ['Misc Files', 'Developer Files', 'Disk Image Files', 'Compressed Files', 'Settings Files', 'System Files', 'Plugin Files', 'Web Files', 'Game Files', 'Database', 'Spreadsheet', '3d', 'Images', 'Text Files', 'Executables', 'Videos', 'Music', 'pdf', 'Presentation', 'Data Files']

for x in range(0, 19):
    if not os.path.exists(os.path.join(path, folder_name[x])):
        os.makedirs(os.path.join(path, folder_name[x]))

for file_name in names:
    if os.path.isfile(os.path.join(path, file_name)):
        extension = os.path.splitext(file_name)[1].lower()  # Get the file extension in lowercase

        destination_folder = None

        if ".png" in extension or ".jpg" in extension or ".tif" in extension or ".tiff" in extension or ".bmp" in extension or ".jpeg" in extension or ".gif" in extension or ".eps" in extension or ".raw" in extension or ".cr2" in extension or ".nef" in extension or ".orf" in extension or ".sr2" in extension or ".heic" in extension:
            destination_folder = 'Images'
        elif ".txt" in extension or ".fpt" in extension or ".docx" in extension or ".rtf" in extension or ".log" in extension or ".doc" in extension:
            destination_folder = 'Text Files'
        # Add more conditions for other file extensions as needed
        elif ".ppt" in extension or ".pptx" in extension:
            destination_folder = 'Presentation'
        elif ".csv" in extension or ".key" in extension or ".keychain" in extension or ".dat" in extension or ".sdf" in extension or ".tar" in extension or ".xml" in extension or ".vcf" in extension:
            destination_folder = 'Data Files'
        elif ".aif" in extension or ".iff" in extension or ".m3u" in extension or ".m4a" in extension or ".mid" in extension or ".mp3" in extension or ".mpa" in extension or ".wav" in extension or ".wma" in extension:
            destination_folder = 'Music'
        elif ".3g2" in extension or ".3gp" in extension or ".asf" in extension or ".avi" in extension or ".flv" in extension or ".m4v" in extension or ".mov" in extension or ".mp4" in extension or ".mpg" in extension or ".rm" in extension or ".srt" in extension or ".swf" in extension or ".mkv" in extension or ".vob" in extension or ".wmv" in extension:
            destination_folder = 'Videos'
        elif ".3dm" in extension or ".3ds" in extension or ".max" in extension or ".obj" in extension:
            destination_folder = '3d'
        elif ".xls" in extension or ".xlsx" in extension or ".db" in extension or ".sql" in extension or ".accdb" in extension or ".dbf" in extension or ".mdb" in extension or ".pdb" in extension:
            destination_folder = 'Database'
        elif ".apk" in extension or ".app" in extension or ".bat" in extension or ".cgi" in extension or ".com" in extension or ".exe" in extension or ".gadget" in extension or ".jar" in extension or ".wsf" in extension:
            destination_folder = 'Executables'
        elif ".b" in extension or ".dem" in extension or ".gam" in extension or ".nes" in extension or ".rom" in extension or ".sav" in extension:
            destination_folder = 'Game Files'
        elif ".pdf" in extension:
            destination_folder = 'pdf'
        elif ".asp" in extension or ".aspx" in extension or ".css" in extension or ".htm" in extension or ".html" in extension or ".js" in extension or ".jsp" in extension or ".php" in extension or ".rss" in extension or ".crx" in extension or ".plugin" in extension or ".fnt" in extension or ".fon" in extension or ".otf" in extension or ".ttf" in extension:
            destination_folder = 'Web Files'
        elif ".cab" in extension or ".deskthemepack" in extension or ".dll" in extension or ".ico" in extension or ".sys" in extension or ".lnk" in extension or ".dmp" in extension or ".drv" in extension:
            destination_folder = 'System Files'
        elif ".ini" in extension or ".cfg" in extension or ".prf" in extension:
            destination_folder = 'Settings Files'
        elif ".7z" in extension or ".cbr" in extension or ".deb" in extension or ".gz" in extension or ".pkg" in extension or ".rar" in extension or ".rpm" in extension or ".tar.gz" in extension or ".zip" in extension or ".zipx" in extension:
            destination_folder = 'Compressed Files'
        elif ".bin" in extension or ".dmg" in extension or ".iso" in extension or ".mdf" in extension or ".vcd" in extension:
            destination_folder = 'Disk Image Files'

        if destination_folder is not None:
            source_file_path = os.path.join(path, file_name)
            destination_file_path = os.path.join(path, destination_folder, file_name)

            try:
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved file '{file_name}' to '{destination_folder}' successfully.")
            except FileNotFoundError:
                print(f"File '{file_name}' not found in the source directory. Skipping.")
            except Exception as e:
                print(f"An error occurred while processing '{file_name}': {str(e)}")

print("Processing completed.")
