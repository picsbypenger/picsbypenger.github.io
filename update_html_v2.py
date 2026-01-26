import os
import re

# Dimensions map
dims = {
    '1.jpg': (2048, 1152), '10.jpg': (2048, 1366), '11.jpg': (2048, 1365), '12.jpg': (2048, 1366),
    '13.jpg': (2048, 1366), '14.jpg': (2048, 1365), '15.jpg': (1366, 2048), '16.jpg': (2048, 1366),
    '17.jpg': (2048, 1366), '18.jpg': (2048, 1366), '19.jpg': (2048, 1366), '2.jpg': (2048, 1366),
    '20.jpg': (2048, 1366), '21.jpg': (1365, 2048), '22.jpg': (1536, 2048), '23.jpg': (2048, 1366),
    '24.jpg': (2048, 1152), '25.jpg': (2048, 1366), '26.jpg': (2048, 1366), '27.jpg': (2048, 1366),
    '28.jpg': (2048, 1365), '29.jpg': (2048, 1365), '3.jpg': (2048, 1366), '30.jpg': (2048, 1366),
    '4.jpg': (2048, 1365), '5.jpg': (2048, 1365), '6.jpg': (2048, 1366), '7.jpg': (1320, 1650),
    '8.jpg': (1320, 1650), '9.jpg': (2048, 1366),
    'port1.jpg': (1639, 2048), 'port10.jpg': (1365, 2048), 'port11.jpg': (5154, 3436), 'port12.jpg': (3530, 5295),
    'port13.jpg': (2893, 3857), 'port14.jpg': (3461, 5192), 'port15.jpg': (4917, 3278), 'port2.jpg': (1366, 2048),
    'port3.jpg': (1536, 2048), 'port4.jpg': (1366, 2048), 'port5.jpg': (1366, 2048), 'port6.jpg': (1366, 2048),
    'port7.jpg': (1366, 2048), 'port8.jpg': (2048, 1366), 'port9.jpg': (2048, 1366),
    'katz1.jpg': (1365, 2048), 'katz2.jpg': (2048, 1536), 'ellis2.jpg': (1365, 2048), 'ellis3.jpg': (1365, 2048),
    'dth3.jpg': (2048, 1366), 'dth4.jpg': (2048, 1366), 'stam.jpg': (1365, 2048), 'spence.JPG': (1365, 2048),
    'm1.jpg': (4096, 2731), 'm10.jpg': (2731, 4096), 'm11.jpg': (3562, 2375), 'm12.jpg': (4096, 2730),
    'm13.jpg': (4096, 2730), 'm14.jpg': (2731, 4096), 'm15.jpg': (2731, 4096), 'm16.jpg': (4096, 2731),
    'm17.jpg': (2048, 1152), 'm18.jpg': (4032, 2688), 'm19.jpg': (3182, 2386), 'm2.jpg': (2731, 4096),
    'm20.jpg': (2731, 4096), 'm21.jpg': (3379, 2253), 'm22.jpg': (4096, 2731), 'm23.jpg': (2731, 4096),
    'm24.jpg': (4096, 2731), 'm25.jpg': (1361, 2042), 'm26.jpg': (2870, 3826), 'm27.jpg': (4096, 2731),
    'm28.jpg': (3601, 2401), 'm29.jpg': (2731, 4096), 'm3.jpg': (2731, 4096), 'm30.jpg': (4096, 2730),
    'm31.jpg': (4096, 2731), 'm32.jpg': (3904, 2603), 'm33.jpg': (3179, 2119), 'm34.jpg': (3455, 2303),
    'm35.jpg': (4096, 2731), 'm36.jpg': (2048, 1366), 'm37.jpg': (5410, 3607), 'm38.jpg': (3609, 5413),
    'm39.jpg': (4832, 3221), 'm4.jpg': (2731, 4096), 'm5.jpg': (4096, 1797), 'm6.jpg': (4096, 2731),
    'm7.jpg': (2731, 4096), 'm8.jpg': (4096, 2731), 'm9.jpg': (4096, 2731)
}

def get_ratio(path):
    filename = os.path.basename(path)
    if filename in dims:
        return dims[filename][0] / dims[filename][1]
    for k, v in dims.items():
        if k.lower() == filename.lower():
            return v[0] / v[1]
    return 1.0

files = ['sports/index.html', 'people/index.html', 'life/index.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    def replacer(match):
        ratio_str = match.group(1)
        src = match.group(2)
        ratio = get_ratio(src)
        return f'<figure style="aspect-ratio: {ratio}"><img class="lazy" style="aspect-ratio: {ratio}" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="{src}" alt="."></figure>'

    # Match <figure style="aspect-ratio: ..."><img ... data-src="..." ...></figure>
    new_content = re.sub(r'<figure style="aspect-ratio: ([^"]+)"><img class="lazy" src="[^"]+" data-src="([^"]+)" alt="."></figure>', replacer, content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {filepath}")
