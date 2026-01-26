import os
import subprocess

# Max dimension for longest side
MAX_DIM = 2048

dirs = [
    'images',
    'images/s',
    'images/m'
]

def get_dimensions(path):
    try:
        output = subprocess.check_output(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', path], text=True)
        w_match = [line for line in output.split('\n') if 'pixelWidth' in line]
        h_match = [line for line in output.split('\n') if 'pixelHeight' in line]
        
        if w_match and h_match:
            w = int(w_match[0].split(':')[1].strip())
            h = int(h_match[0].split(':')[1].strip())
            return w, h
    except:
        pass
    return 0, 0

def resize_image(path):
    w, h = get_dimensions(path)
    if w == 0: return

    longest = max(w, h)
    
    if longest > MAX_DIM:
        print(f"Resizing {path} ({w}x{h}) -> {MAX_DIM}px...")
        try:
            subprocess.run(
                ['sips', '--resampleHeightWidthMax', str(MAX_DIM), path],
                check=True,
                stdout=subprocess.DEVNULL
            )
        except subprocess.CalledProcessError as e:
            print(f"Error resizing {path}: {e}")

for d in dirs:
    if not os.path.exists(d):
        continue
        
    for f in os.listdir(d):
        path = os.path.join(d, f)
        name, ext = os.path.splitext(f)
        
        # Process only jpgs and SKIP generated thumbnails (_small, _medium)
        if os.path.isfile(path) and ext.lower() in ['.jpg', '.jpeg']:
            if not (name.endswith('_small') or name.endswith('_medium')):
                resize_image(path)

print("Resize complete.")