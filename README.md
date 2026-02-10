## EXIF Metadata Viewer & Remover

Author: **Neehaar C**\
GitHub: <https://github.com/hyprblaze>

* * * * *

### Project Overview

The EXIF Metadata Viewer & Remover is a web-based application built using Python and Streamlit that allows users to view, analyze, export, and remove metadata from image files.

Digital images often contain hidden metadata known as EXIF (Exchangeable Image File Format) data. This may include GPS location coordinates, camera model, date and time, device information, and image settings such as ISO and aperture.

This project helps users understand hidden metadata, export metadata for analysis, and protect privacy by removing metadata from images.

* * * * *

### Deployment Status Notice

The Streamlit Cloud version of the application is currently under maintenance.

Some features such as:

- Opening GPS location directly in Google Maps\
- Removing metadata and downloading the cleaned image

may not function fully in the deployed Streamlit version due to cloud environment limitations.

However, the full version of the application with all features working correctly is available in the source code and can be run locally without any limitations.

Users are recommended to run the application locally to access all features.

* * * * *

### Features

Image Upload\
Supports JPG, JPEG, and PNG image formats. The uploaded image is displayed instantly in the web interface.

Metadata Viewer\
Displays complete EXIF metadata in a readable format. All available metadata fields are shown clearly.

GPS Location Detection\
Extracts GPS coordinates from image metadata if available and converts them into readable decimal format.

Metadata Export Options\
Allows exporting metadata in TXT, CSV, and JSON formats for analysis and storage.

Metadata Removal\
Removes all metadata from the image while preserving the image content. Users can download a clean image without metadata (fully functional in local version).

Google Maps Integration\
Allows opening the exact GPS location in Google Maps (fully functional in local version).

Web-based Interface\
Provides a simple, clean, and user-friendly interface built using Streamlit.

* * * * *

### Technologies Used

Python\
Used as the core programming language.

Streamlit\
Used for building the web application interface.

Pillow (PIL)\
Used for image processing and EXIF metadata extraction.

JSON and CSV\
Used for exporting metadata in structured formats.

GitHub\
Used for version control and source code hosting.

Streamlit Cloud\
Used for online deployment.

* * * * *

### Project Structure

exif-metadata-viewer folder contains:

app.py\
Main application file containing application logic.

requirements.txt\
Contains required Python libraries.

README file\
Contains project documentation.

sample_images folder\
Contains images for testing metadata extraction and removal.

* * * * *

### Live Demo

Streamlit Cloud App Link: https://exif-metadata-viewer.streamlit.app/


Note: For full functionality, run the application locally using the source code.



* * * * *

### Privacy Importance

EXIF metadata may contain sensitive information such as GPS location, device information, and timestamps. This tool helps users detect and remove such metadata to protect privacy.

* * * * *

### Project Purpose

This project was developed as part of an academic submission. It demonstrates image metadata extraction, metadata removal, privacy protection, and Python web application development using Streamlit.

* * * * *

**Author**

*Neehaar C*\
GitHub: <https://github.com/hyprblaze>

* * * * *

### License

This project is intended for educational and academic purposes.
