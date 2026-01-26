import os
import subprocess

# Directories to process
dirs = [
    'images',
    'images/s',
    'images/m'
]

def generate_thumbnail(path):
    dirname, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)
    
    # Skip if not jpg/jpeg or if already a thumbnail
    if ext.lower() not in ['.jpg', '.jpeg'] or name.endswith('_small') or name.endswith('_medium'):
        return

    # 1. Medium Thumbnail (1000px)
    medium_filename = f"{name}_medium{ext}"
    medium_path = os.path.join(dirname, medium_filename)

    if not os.path.exists(medium_path):
        print(f"Generating medium thumbnail for {path}...")
        try:
            subprocess.run(
                ['sips', '--resampleWidth', '1000', path, '--out', medium_path],
                check=True,
                stdout=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError as e:
            print(f"Error processing {path}: {e}")

for d in dirs:
    if not os.path.exists(d):
        continue
        
    for f in os.listdir(d):
        file_path = os.path.join(d, f)
        if os.path.isfile(file_path):
            generate_thumbnail(file_path)

print("Medium thumbnail generation complete.")
