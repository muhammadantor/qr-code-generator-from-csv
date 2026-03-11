# QR Code Generator From CSV (Python)

A simple Python automation project that generates **QR codes for multiple websites automatically** using a CSV file.

This script reads website names and links from a CSV file and creates QR code images for each website.

Each QR code is saved using the **website name as the image file name**.

This project demonstrates **Python automation, file handling, and batch processing**.

---

# Project Overview

Many times we need QR codes for multiple links.
Creating them manually takes time.

This script solves that problem by **automatically generating QR codes from a CSV dataset**.

The script will:

1. Read website data from a CSV file
2. Extract website name and link
3. Generate a QR code for the link
4. Save the QR code as an image file

All of this happens automatically with a single script.

---

# Project Screenshot

Click the image below to view the workflow screenshot.

[View Screenshot](qr_code_script_ss.png)

---

# Python Script

You can view the Python script directly here:

[Open Python Script](qr_code_create.py)

---

# CSV Dataset

The CSV file contains website names and links.

Example format:

```
site_name,link
Google,https://google.com
YouTube,https://youtube.com
Facebook,https://facebook.com
```

Dataset File:

[Open CSV File](top_500_websites.csv)

---

# Features

• Automatically generates QR codes
• Supports batch processing from CSV
• Saves each QR code with website name
• Beginner-friendly Python script
• Simple and lightweight automation project

---

# Technologies Used

Python
qrcode library
CSV file handling

---

# Installation

Install the required Python library.

```
pip install qrcode[pil]
```

---

# Run the Script

Run the Python script:

```
python qr_code_create.py
```

After running the script, QR code images will be generated automatically.

Example output files:

```
Google.jpg
YouTube.jpg
Facebook.jpg
```

---

# How the Script Works

The script follows these steps:

1. Opens the CSV file
2. Skips the header row
3. Reads each line of data
4. Extracts the website name and link
5. Generates a QR code
6. Saves the QR code image

This allows bulk QR code generation with minimal effort.

---

# Example Use Cases

Generating QR codes for:

• Website collections
• Marketing campaigns
• Product links
• Event pages
• Business contact links

---

# Author

Muhammad Antor
AI Automation Builder
Bangladesh

GitHub Profile:
https://github.com/muhammadantor

---

# License

This project is open source and free to use.
