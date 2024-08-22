# Set the root directory to scan for videos
$directory = "C:\path\to\vods"

# Path to your exported HandBrakeCLI preset file
$presetPath = "C:\path\to\handbrake_preset.json"

# Recursively find .mkv, .mp4, and .m4v files
Get-ChildItem -Path $directory -Recurse -Include *.mkv, *.mp4, *.m4v | ForEach-Object {
    $file = $_.FullName
    $fileDir = $_.Directory.FullName
    $compressedDir = Join-Path $fileDir "compressed"

    # Skip if the file is already in the "compressed" folder
    if ($fileDir -like "*\compressed") {
        Write-Host "Skipping: $file is in a 'compressed' folder."
        return
    }

    # Create the compressed directory if it doesn't exist
    if (!(Test-Path $compressedDir)) {
        New-Item -Path $compressedDir -ItemType Directory
    }

    # Generate the output file path in the compressed directory
    $filename = [System.IO.Path]::GetFileNameWithoutExtension($file)
    $outputFile = Join-Path $compressedDir "${filename}.mp4"

    # Check if the file already exists in the compressed folder
    if (Test-Path $outputFile) {
        Write-Host "Skipping: $outputFile already exists."
    } else {
        # Run HandBrakeCLI to compress the video
        Write-Host "Processing: $file -> $outputFile"
        & .\HandBrakeCLI -i $file -o $outputFile --preset-import-file $presetPath
    }
}

