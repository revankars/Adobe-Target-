import os
import pandas as pd
import ftplib
import shutil
from datetime import datetime

# Configuration
FTP_SERVER = ''  # Your FTP server address
FTP_USER = ''            # Your FTP username
FTP_PASS = ''            # Your FTP password
FILE_TO_UPLOAD = 'feed.csv'  # The file you want to upload
ARCHIVE_DIR = './archive/'  # Directory to archive the file
SRC_PATH = "Product_Catalog_2024_10_03.txt"  
#TGT_PATH = "template.csv"
TPLT_FILE_PATH = "feed.csv"
DIR_PATH = './' 

# Path to the file that stores processed file dates
PROCESSED_FILES_LOG = "processed_files.txt"

def list_txt_files(directory):
    prefix = "Product_Catalog_"
    files = os.listdir(directory)
    # Only return files that start with 'Product_Catalog_' and have a .txt extension
    return [f for f in files if f.endswith('.txt') and f.startswith(prefix) and os.path.isfile(os.path.join(directory, f))]

def load_processed_files():
    """Load the list of processed file dates from a log file."""
    if not os.path.exists(PROCESSED_FILES_LOG):
        return set()  # Return an empty set if the log file doesn't exist

    with open(PROCESSED_FILES_LOG, 'r') as file:
        processed_files = {line.strip() for line in file.readlines()}
    return processed_files

def save_processed_file(date_str):
    """Save the processed file date to the log file."""
    with open(PROCESSED_FILES_LOG, 'a') as file:
        file.write(f"{date_str}\n")

def extract_date_from_filename(filename):
    """Extract the date from the filename (e.g., 'file_2024_10_03.txt' -> '2024_10_03')."""
    return filename.split('_')[-3:]  # Assuming the date is the last 3 parts of the filename

def is_file_processed(date_str):
    """Check if the file with the given date has already been processed."""
    processed_files = load_processed_files()
    return date_str in processed_files    

# Function to copy the template file and append a date suffix to the new file
def copy_template_with_date(template_file, destination_dir):
    # Get current date in MM-DD-YYYY format
    current_date = datetime.now().strftime('%m-%d-%Y')
  
    # Get the file name and extension of the template file
    file_name, file_ext = os.path.splitext(os.path.basename(template_file))
    print(f"Template file copied to: {file_name} : {file_ext}")
    # Create a new file name with the date suffix
    new_file_name = f"{file_name}_{current_date}{file_ext}"
    new_file_path = os.path.join(destination_dir, new_file_name)
    
    # Copy the template file to the new file
    shutil.copy(template_file, new_file_path)
    
    print(f"Template file copied to: {new_file_path}")
    return new_file_path

def process_file(source_path,target_path):
    
    """Process the file if it hasn't been processed already."""
    filename = os.path.basename(source_path)
    global date_str 
    date_str = '_'.join(extract_date_from_filename(filename))
    # Create a new file name with the date suffix
    # Get the file name and extension of the template file
    targetfile = os.path.basename(target_path)
    if is_file_processed(date_str):
        print(f"File with date {date_str} has already been processed. Skipping.")
        return "skip"
    else:
        print(f"Processing file {source_path} with date {date_str}...")

        # Add your file processing logic here
        """These are dummy values for thumbnailUrl,value,URL"""
        thumbnailUrl = 'https://www.example.com/is/image/samsung'
        Url = 'https://www.example.com/?query=null'
        value=999
        """ Read the file and store in the data frame"""
        df = pd.read_csv(source_path, usecols=['ITEM_CD','ITEM_DESC','EQP_CTGRY_DESC','MFG_NM'], delimiter='|')
        df['thumbnailUrl'] = thumbnailUrl
        df['value'] = value
        df['URL'] = Url
        df = df[['ITEM_CD','ITEM_DESC','EQP_CTGRY_DESC','MFG_NM','thumbnailUrl','value','URL']]
        with open(targetfile, 'a') as f:
            f.write('\n')
        df.to_csv(targetfile, mode='a', header = False, index = False)

        #import time
        #time.sleep(1)  # Simulate some processing
        print(f"Finished updating the file: {target_path}")
        print(f"Finished processing the file: {source_path}")
        archive_file(source_path, ARCHIVE_DIR)
        # Mark the file as processed
        save_processed_file(date_str)
        return "cont"

def archive_file(file_path, archive_dir):
    try:
        # Ensure the archive directory exists
        os.makedirs(archive_dir, exist_ok=True)
        # Move the file to the archive directory
        shutil.move(file_path, os.path.join(archive_dir, os.path.basename(file_path)))
        print(f"Archived {file_path} to {archive_dir}")

    except Exception as e:
        print(f"Error archiving file: {e}")


def upload_file_to_ftp(file_path):
    try:
        # Connect to the FTP server
        with ftplib.FTP(FTP_SERVER) as ftp:
            ftp.login(FTP_USER, FTP_PASS)
            print(f"Logged in to FTP server: {FTP_SERVER}")

            # Open the file in binary mode and upload
            with open(file_path, 'rb') as file:
                ftp.storbinary(f'STOR {os.path.basename(file_path)}', file)
                print(f"Uploaded {file_path} to {FTP_SERVER}")

    except Exception as e:
        print(f"Error uploading file: {e}")

def main():
    files = list_txt_files(DIR_PATH)
    if len(files) > 1:
        print(f"Multiple .txt files with the prefix 'Product_Catalog_' detected ({len(files)}). Skipping file processing, upload and archive. Please ensure there is only one file before processing.")
        print(f"Skipping file processing, upload and archive. Please ensure there is only one file before processing.")
        # Stop further execution
    elif len(files) == 1:
        #Check if the file exists
        print(f"One .txt file with the prefix 'Product_Catalog_' detected. Continue to process, upload and archive the file: {files[0]}")
        #if os.path.exists(FILE_TO_UPLOAD):
        # Step 1: Copy the template and create a new file with the date suffix
        TGT_PATH = copy_template_with_date(TPLT_FILE_PATH, DIR_PATH)
        prc_val = process_file(files[0],TGT_PATH)
        print("value of prc_value:",prc_val)
        if prc_val != "skip":
            upload_file_to_ftp(TGT_PATH)
            archive_file(TGT_PATH, ARCHIVE_DIR)
        else:
            print(f"File with date {date_str} is processed already. Skipping {TGT_PATH} file upload and archive.")

if __name__ == "__main__":
    main()