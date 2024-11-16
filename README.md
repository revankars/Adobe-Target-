# README: Automating the File Upload Process to Adobe Target: A Simplified Script for Efficient Data Management
 

In continuous data flow projects, automation is key to improving efficiency and reducing errors. One of the most repetitive and error-prone tasks is ensuring that product data is uploaded to Adobe Target's recommendation system in a timely and accurate manner. To address this, we’ve developed a modular script that automates the entire process—from file processing to FTP upload—and is flexible enough to adapt to changing requirements as needed. In this post, we’ll explain how the script works, its modular design, and how it can be easily customized to meet specific needs.

## The Need for Automation

When managing large datasets like product catalogs, keeping data updated in Adobe Target is crucial for delivering personalized experiences. However, doing this manually can be time-consuming and error-prone. Our solution was to automate the process with a script that ensures product data is always in the right format for Adobe Target’s recommendation system.

What makes this script especially powerful is its modular design. Each function is designed to handle specific tasks in the process, and these modules can be easily repurposed or extended to fit different requirements as the project evolves. This flexibility makes it an ideal tool for both current needs and future enhancements.


## How the Script Helps

The modular script automates several key tasks to streamline the process of preparing and uploading product data to an FTP server:

- **Processing:** Extracts relevant information from source files.
- **Uploading:** Uploads the processed file to an FTP server.
- **Archiving:** Moves the processed files to an archive directory to prevent reprocessing.

## Modular Structure for Flexibility
The script is structured in a way that each module (or function) can be independently adjusted, modified, or reused as required. Whether you need to change the data processing logic, adapt the file upload process, or integrate new features, the modular design allows for easy customization without disrupting the entire workflow.

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

## Example of Script Flexibility
Let’s say you need to add a new field to the product data, such as price, and include it in the feed. With the modular design, you can simply modify the data processing module to extract the new field and add it to the target file without impacting the rest of the process. This flexibility allows the script to evolve with your changing needs.

## In Summary

This modular automation script significantly reduces the manual effort involved in updating product data on Adobe Target. By automating the processing, uploading, and archiving steps, the script ensures that your data is always current and synchronized without requiring constant manual intervention. Its flexible, modular design makes it easy to repurpose and adapt for future needs—whether you're adding new data fields, integrating with a different system, or adjusting file upload methods.


