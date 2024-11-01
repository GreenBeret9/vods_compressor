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
2. Modify the key variable in the script:

```powershell
# Path to your exported HandBrakeCLI preset file
$presetPath = "C:\path\to\handbrake_preset.json"
```

- **$presetPath**: The full path to the HandBrake preset file (`.json`) you downloaded.
  
## 2. Run the Script

1. Open **PowerShell** or a terminal.
2. Navigate to the folder where you installed **HandBrakeCLI** using the following command:

```powershell
cd path\to\HandBrakeCLI-1.8.2-win-x86_64
```
Once you're in the correct directory, run the PowerShell script:

```powershell
.\vods_compressor.ps1 -directory "C:\path\to\videos"
```
The script will then begin processing videos, compressing them and placing the compressed versions into a compressed/ subfolder.
 If a compressed version of the video already exists, it will skip that file.


 ## Python Instructions

### 1. Edit the Python Script
After downloading the `compress_vods.py` script and the HandBrake preset file (`.json`):

1. Open the `compress_vods.py` file in a text editor.
2. Update the `PRESET_PATH` variable to specify the full path to the HandBrake preset file:

   ```python
   # Path to your exported HandBrakeCLI preset file
   PRESET_PATH = r"C:\path\to\handbrake_preset.json"
   ```

3. Save the changes to the script.

### 2. Run the Python Script

1. Open **Command Prompt** or **Terminal**.
2. Navigate to the directory where the **HandBrakeCLI** executable is located:

   ```bash
   cd C:\path\to\HandBrakeCLI-1.8.2-win-x86_64
   ```

3. Run the Python script by passing the path of the directory containing your videos:

   ```bash
   python compress_vods.py "C:/path/to/videos"
   ```

The Python script will then start processing videos. For each video, it will compress it and place the output in a `compressed/` subfolder. If the compressed file already exists, it will skip that file.


