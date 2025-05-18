# Converts a sequence of bytes into an integer using little-endian byte order.
# For example, le(b'\x01\x00') returns 1, and le(b'\x01\x02') returns 513.
def le(bs):
    n = 0
    for i, b in enumerate(bs):
        # Shift each byte to its correct position based on little-endian order
        n += b << (i * 8)
    return n


# Read the entire binary content of the BMP file
with open("teapot.bmp", "rb") as f:
    data = f.read()

# Parse BMP metadata:
# - 'offset' is where the pixel data begins in the file (usually 54 bytes for standard BMPs)
# - 'width' and 'height' are the dimensions of the image in pixels
offset = le(data[10:14])
width = le(data[18:22])
height = le(data[22:26])  # height is unused but parsed anyway

# Prepare a list to hold rotated pixel data
pixels = []

# Perform a 90-degree clockwise rotation of the image
# Traverse each pixel in the rotated image (target_x, target_y)
for target_y in range(width):
    for target_x in range(width):
        # Map each (target_x, target_y) to its original source location
        source_y = target_x
        source_x = width - target_y - 1

        # Calculate the byte index of the source pixel in the original data
        # Each pixel takes 3 bytes (RGB), and pixels are stored in row-major order
        n = offset + 3 * (source_y * width + source_x)

        # Extract the RGB values for that pixel and append to the new pixel list
        pixels.append(data[n : n + 3])

# Write the rotated image to a new BMP file
with open("rotate.bmp", "wb") as f:
    # Copy the original BMP header up to the start of pixel data
    f.write(data[:offset])
    # Write the rotated pixel data
    f.write(b"".join(pixels))
