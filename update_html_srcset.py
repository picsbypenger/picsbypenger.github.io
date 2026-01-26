import os
import re

def add_srcset(match):
    full_tag = match.group(0)
    data_src = match.group(1)
    
    base, ext = os.path.splitext(data_src)
    small_src = f"{base}_small{ext}"
    medium_src = f"{base}_medium{ext}"
    
    # Construct srcset string
    # We include small (600w), medium (1000w), and original (2048w approx)
    srcset = f"{small_src} 600w, {medium_src} 1000w, {data_src} 2048w"
    
    # Sizes attribute:
    # 1 column (mobile) -> 100vw
    # 2 columns (tablet) -> 50vw
    # 3 columns (desktop) -> 33vw
    sizes = "(max-width: 576px) 100vw, (max-width: 992px) 50vw, 33vw"
    
    # Check if we already have data-srcset
    if 'data-srcset' in full_tag:
        # Update existing
        full_tag = re.sub(r'data-srcset="[^"]+"', f'data-srcset="{srcset}"', full_tag)
        full_tag = re.sub(r'sizes="[^"]+"', f'sizes="{sizes}"', full_tag)
        return full_tag
        
    # Inject attributes
    # We replace the whole tag logic or just insert
    return full_tag.replace(f'data-src="{data_src}"', f'data-srcset="{srcset}" sizes="{sizes}" data-src="{data_src}"')

files = ['sports/index.html', 'people/index.html', 'life/index.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Update all img tags with data-src
    new_content = re.sub(r'<img[^>]+data-src="([^"]+)"[^>]*>', add_srcset, content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {filepath}")