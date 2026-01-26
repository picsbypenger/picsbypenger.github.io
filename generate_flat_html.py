import os

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
    'katz1.jpg': (1365, 2048), 'katz2.jpg': (1365, 2048), 'ellis2.jpg': (1365, 2048), 'ellis3.jpg': (1365, 2048),
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

def get_ratio(filename):
    wh = dims.get(filename)
    if not wh:
        for k, v in dims.items():
            if k.lower() == filename.lower():
                return v[0]/v[1]
        return 1.0
    return wh[0]/wh[1]

def generate_flat_html(image_paths):
    html = ''
    for path in image_paths:
        filename = os.path.basename(path)
        ratio = get_ratio(filename)
        html += f'        <figure style="aspect-ratio: {ratio}"><img class="lazy" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" data-src="{path}" alt="."></figure>\n'
    return html

sports_imgs = ["../images/s/3.jpg", "../images/s/21.jpg", "../images/s/10.jpg", "../images/s/14.jpg", "../images/s/7.jpg", "../images/s/26.jpg", "../images/s/1.jpg", "../images/s/20.jpg", "../images/s/13.jpg", "../images/s/11.jpg", "../images/s/29.jpg", "../images/s/27.jpg", "../images/s/28.jpg", "../images/s/19.jpg", "../images/s/16.jpg", "../images/s/9.jpg", "../images/s/6.jpg", "../images/s/30.jpg", "../images/s/4.jpg", "../images/s/2.jpg", "../images/s/5.jpg", "../images/s/8.jpg", "../images/s/12.jpg", "../images/s/18.jpg", "../images/s/23.jpg", "../images/s/22.jpg"]
people_imgs = ["../images/port3.jpg", "../images/katz1.jpg", "../images/ellis2.jpg", "../images/port2.jpg", "../images/dth3.jpg", "../images/port6.jpg", "../images/dth4.jpg", "../images/port14.jpg", "../images/port11.jpg", "../images/port9.jpg", "../images/stam.jpg", "../images/spence.JPG", "../images/port5.jpg", "../images/port12.jpg", "../images/port13.jpg", "../images/port15.jpg", "../images/port7.jpg", "../images/katz2.jpg", "../images/port1.jpg"]
life_imgs = ["../images/m/m1.jpg", "../images/m/m3.jpg", "../images/m/m5.jpg", "../images/m/m2.jpg", "../images/m/m7.jpg", "../images/m/m4.jpg", "../images/m/m6.jpg", "../images/m/m8.jpg", "../images/m/m9.jpg", "../images/m/m11.jpg", "../images/m/m13.jpg", "../images/m/m15.jpg", "../images/m/m17.jpg", "../images/m/m19.jpg", "../images/m/m21.jpg", "../images/m/m23.jpg", "../images/m/m25.jpg", "../images/m/m27.jpg", "../images/m/m29.jpg", "../images/m/m31.jpg", "../images/m/m33.jpg", "../images/m/m35.jpg", "../images/m/m10.jpg", "../images/m/m12.jpg", "../images/m/m14.jpg", "../images/m/m16.jpg", "../images/m/m18.jpg", "../images/m/m20.jpg", "../images/m/m22.jpg", "../images/m/m24.jpg", "../images/m/m26.jpg", "../images/m/m28.jpg", "../images/m/m30.jpg", "../images/m/m32.jpg", "../images/m/m34.jpg", "../images/m/m36.jpg", "../images/m/m37.jpg", "../images/m/m39.jpg"]

print("--- SPORTS ---")
print(generate_flat_html(sports_imgs))
print("\n--- PEOPLE ---")
print(generate_flat_html(people_imgs))
print("\n--- LIFE ---")
print(generate_flat_html(life_imgs))
