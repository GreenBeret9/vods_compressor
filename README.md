# Vods Compressor

This script compresses videos recursively within folders. For each folder, the compressed videos are placed in a "compressed/" subfolder. If a video has already been compressed, it will be skipped to avoid recompression.

## Prerequisites

### 1. Download HandBrakeCLI
- HandBrakeCLI is the command-line version of HandBrake, a popular video transcoding tool. 
- You can download it from the official website: [HandBrakeCLI Downloads](https://handbrake.fr/downloads2.php) (look for the "Command Line Tool" version).

### 2. Download the Repository Files
- Download both the **PowerShell script** (`.ps1` file) and the **HandBrake preset** (`.json` file) from this repository.

## Setup Instructions

### 1. Edit the Script
After downloading the `.ps1` and `.json` files:

1. Open the `.ps1` script (the PowerShell script) in a text editor like Notepad.
2. Modify the two key variables in the script:

```powershell
# Set the root directory to scan for videos
$directory = "C:\path\to\vods"

# Path to your exported HandBrakeCLI preset file
$presetPath = "C:\path\to\handbrake_preset.json"


