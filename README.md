# Vods Compressor

This script compresses videos recursively within folders. For each folder, the compressed videos are placed in a "compressed/" subfolder. If a video has already been compressed, it will be skipped to avoid recompression.

## Prerequisites

### 1. Download HandBrakeCLI
- HandBrakeCLI is the command-line version of HandBrake, a popular video transcoding tool. 
- You can download it from the official website: [HandBrakeCLI Downloads](https://handbrake.fr/downloads2.php).

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

- **$directory**: The absolute path where your videos are stored. This directory can also contain subdirectories with videos.
- **$presetPath**: The full path to the HandBrake preset file (`.json`) you downloaded.
```
## 2. Run the Script

1. Open **PowerShell** or a terminal.
2. Navigate to the folder where you installed **HandBrakeCLI** using the following command:

```bash
cd path\to\HandBrakeCLI-1.8.2-win-x86_64

Once you're in the correct directory, run the PowerShell script:

```
.\vods_compressor.ps1

The script will then begin processing videos, compressing them and placing the compressed versions into a compressed/ subfolder.
 If a compressed version of the video already exists, it will skip that file.

