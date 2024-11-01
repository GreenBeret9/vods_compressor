import os
import subprocess
import argparse
import shutil

# Path to your exported HandBrakeCLI preset file
PRESET_PATH = r"C:\path\to\handbrake_preset.json"  # Update with your preset path

def compress_videos(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory {directory} does not exist.")
        return

    # Recursively find .mkv, .mp4, and .m4v files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mkv', '.mp4', '.m4v')):
                file_path = os.path.join(root, file)
                file_dir = os.path.dirname(file_path)
                compressed_dir = os.path.join(file_dir, "compressed")

                # Skip if the file is already in the "compressed" folder
                if "compressed" in file_dir:
                    print(f"Skipping: {file_path} is in a 'compressed' folder.")
                    continue

                # Create the compressed directory if it doesn't exist
                os.makedirs(compressed_dir, exist_ok=True)

                # Generate the output file path in the compressed directory
                filename, _ = os.path.splitext(file)
                output_file = os.path.join(compressed_dir, f"{filename}.mp4")

                # Check if the file already exists in the compressed folder
                if os.path.exists(output_file):
                    print(f"Skipping: {output_file} already exists.")
                else:
                    # Run HandBrakeCLI to compress the video
                    print(f"Processing: {file_path} -> {output_file}")
                    subprocess.run([
                        "HandBrakeCLI",
                        "-i", file_path,
                        "-o", output_file,
                        "--preset-import-file", PRESET_PATH
                    ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compress video files in a directory.")
    parser.add_argument("directory", type=str, help="Directory path must be provided")
    args = parser.parse_args()

    compress_videos(args.directory)
