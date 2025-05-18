import struct

# def read_bmp(filename):
with open("teapot.bmp", "rb") as f:
    header = f.read(14)  # File header (14 bytes)
    info = f.read(40)  # Info header (40 bytes)

    # Unpack width, height, and bit depth
    width, height, planes, bpp = struct.unpack("<iiHH", info[4:16])
    pixel_offset = struct.unpack("<I", header[10:14])[0]

    f.seek(pixel_offset)
    row_size = (width * 3 + 3) & ~3
    pixels = []

    for y in range(height):
        row = f.read(row_size)
        pixels.append([row[i : i + 3] for i in range(0, width * 3, 3)])

rotated_pixels = []
for x in range(width):
    new_row = []
    for y in reversed(range(height)):
        new_row.append(pixels[y][x])
    rotated_pixels.append(new_row)


print(rotated_pixels)
