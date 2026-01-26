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
    if ext.lower() not in ['.jpg', '.jpeg'] or name.endswith('_small'):
        return

    small_filename = f"{name}_small{ext}"
    small_path = os.path.join(dirname, small_filename)

    # Don't regenerate if it exists
    if os.path.exists(small_path):
        return

    print(f"Generating thumbnail for {path}...")
    
    # Use sips to resize to 600px width
    try:
        subprocess.run(
            ['sips', '--resampleWidth', '600', path, '--out', small_path],
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

print("Thumbnail generation complete.")
