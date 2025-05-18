A program that can rotate an image by 90 degrees from scratch.

# Purpose

Trying to expose myself to some basic concepts in working with binary data - things like integer encoding, binary ordering, basic opening and working with a sequence of butes instead of some kind of text format.

# Note

Function le handles little-endian byte decoding, which is how integers are stored in BMP headers.\\

Assumption: The BMP image is square (width == height). If it's not, rotation would distort or truncate the image.\\

This code does not update the BMP width/height fields after rotation, which is acceptable only if the image is square.
