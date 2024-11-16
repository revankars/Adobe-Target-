# README: Automation Script for File Processing, Uploading, and Archiving

# Automating the File Upload Process to Adobe Target: A Simplified Script for Efficient Data Management

In the world of continuous data flow projects, automation plays a crucial role in streamlining workflows and reducing errors. One task that can be easily automated is the upload of product data to Adobe Target’s recommendation system. To simplify this process, we’ve developed a script that automates everything from file processing to uploading the data to the FTP server. This guide explains how the script works and how it can help save time and reduce manual effort.

## The Need for Automation

When managing large datasets like product catalogs, it’s essential to keep the data up-to-date in systems like Adobe Target. In our project, we recognized that manually handling the data upload would be time-consuming and prone to errors. To solve this challenge, we created a script that automates the conversion of product information into Adobe Target’s required recommendation file format. This ensures that data is accurate, up-to-date, and uploaded in a timely manner, without the risk of duplication.


## How the Script Helps

The script automates several key tasks to streamline the process of preparing and uploading product data to an FTP server:

- **Processing:** Extracts relevant information from source files.
- **Uploading:** Uploads the processed file to an FTP server.
- **Archiving:** Moves the processed files to an archive directory to prevent reprocessing.

## Key Features of the Script

The script leverages several functions to manage the file upload process efficiently. Here’s an overview of the core steps involved:

### 1. Configuration Settings

Before running the script, you’ll need to configure a few key variables:

- `FTP_SERVER`: The address of the FTP server where the file will be uploaded.
- `FTP_USER`: Your FTP username.
- `FTP_PASS`: Your FTP password.
- `FILE_TO_UPLOAD`: The name of the target file, typically `feed.csv`.
- `ARCHIVE_DIR`: The directory where processed files will be archived.
- `SRC_PATH`: The path to the source file being processed.
- `TGT_PATH`: The target file name for saving the processed output (e.g., `feed.csv`).

### 2. Processing the Source File

The script processes the source file to ensure it is in the correct format for Adobe Target recommendations. Key actions include:

- **Check for previous processing:** By comparing the file’s date with a log file, the script prevents duplicate uploads.
- **Extract relevant data:** Important product details such as `ITEM_CD`, `ITEM_DESC`, `EQP_CTGRY_DESC`, and `MFG_NM` are pulled from the source file.
- **Add custom data:** Additional fields like `thumbnailUrl`, `URL`, and `value` are included, which are required for Adobe Target recommendations.
- **Save processed output:** After processing, the script saves the data to the target file (e.g., `feed.csv`).

### 3. Uploading and Archiving

After the file is processed, the following steps are executed:

- The processed file (`feed.csv`) is uploaded to the designated FTP server.
- The source file is moved to an archive directory to avoid reprocessing in future runs.

### 4. Execution Flow

The script runs through these key steps:

1. **Check if the target file exists:** If the target file (`feed.csv`) is already present, it skips processing and uploading.
2. **File processing:** The script extracts data from the source file, adds necessary fields, and saves the processed output as `feed.csv`.
3. **Upload:** The processed `feed.csv` is uploaded to the FTP server.
4. **Archive:** The source file is moved to the archive directory after successful upload to prevent reprocessing.

If the target file does not exist or has already been processed, the script will automatically skip the processing and uploading steps.

## How to Use the Script

Follow these steps to use the script:

1. **Prepare the Source File:** Ensure the source file is named according to the convention based on the date (e.g., `Product_Catalog_YYYY_MM_DD.txt`).
2. **Run the Script:** Execute the script to process the source file, upload it to the FTP server, and archive the processed files.
3. **Skip Processed Files:** The script will automatically skip files that have already been processed, ensuring no duplicates are uploaded.

## In Summary

This automation script significantly reduces the manual effort involved in updating product data on Adobe Target. By automating the processing, uploading, and archiving steps, the script ensures that your data is always current and synchronized without requiring constant manual intervention.

> **Visual Guide:**  
> Below is a quick infographic that visualizes how the Adobe Target recommendations process is executed by this automation script.
