from load_model.load import summarizer

# Summarize the text
# Now you can use the summarizer as before
ARTICLE = """
A QR code (quick-response code) is a type of two-dimensional matrix barcode,
invented in 1994, by Japanese company Denso Wave for labelling automobile parts
.[1][2] A QR code consists of black squares arranged in a square grid on a white
 background, including some fiducial markers, which can be read by an imaging
 device, such as a camera, and processed using Reed–Solomon error correction
 until the image can be appropriately interpreted. The required data are then
 extracted from patterns that are present in both the horizontal and the vertical
 components of the QR image.[3]
Whereas a barcode is a machine-readable optical image that contains information
specific to the labelled item, the QR code contains the data for a locator, an
identifier, and for web-tracking. To efficiently store data, QR codes use four
standardized modes of encoding: (i) numeric, (ii) alphanumeric, (iii) byte or
 binary, and (iv) kanji.[4] Compared to standard UPC barcodes, the QR labelling
 system was applied beyond the automobile industry because of faster reading of
 the optical image and greater data-storage capacity in applications such as
 product tracking, item identification, time tracking, document management,
 and general marketing.[3]
"""

summary = summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False)
print(summary[0]["summary_text"])