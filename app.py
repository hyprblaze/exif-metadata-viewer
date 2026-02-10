import streamlit as st
from PIL import Image, ExifTags
import math
import webbrowser
import io
import json
import csv


st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 0px;'>
        EXIF Metadata Viewer & Remover
    </h1>

    <p style='text-align: center; font-size:18px; margin-top: 5px;'>
        Developed by <b>Neehaar C</b>
    </p>

    <p style='text-align: center; font-size:14px; color: gray;'>
        Digital Forensics & Privacy Tool
    </p>

    <p style='text-align: center; font-size:16px;'>
        <a href='https://github.com/hyprblaze' target='_blank'>
            🔗 GitHub Profile
        </a>
    </p>

    <hr>
    """,
    unsafe_allow_html=True
)




uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# Helper function to convert EXIF GPS to decimal format
def dms_to_decimal(dms, ref):
    try:
        # Converts the fraction to float
        def frac_to_float(frac):
            if isinstance(frac, tuple):
                return float(frac[0]) / float(frac[1])
            return float(frac)

        degrees = frac_to_float(dms[0])
        minutes = frac_to_float(dms[1])
        seconds = frac_to_float(dms[2])

        decimal = degrees + (minutes / 60) + (seconds / 3600)

        if ref in ["S", "W"]:
            decimal = -decimal

        return decimal

    except:
        return None



if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    exif_data = image._getexif()
    gps_info = None

    if exif_data:
        for tag_id, value in exif_data.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":
                gps_info = value

    #GPS section
    st.subheader("📍 Location Information")

    if gps_info:
        gps_data = {}
        for key in gps_info:
            decoded = ExifTags.GPSTAGS.get(key, key)
            gps_data[decoded] = gps_info[key]

        lat = dms_to_decimal(
            gps_data.get("GPSLatitude"),
            gps_data.get("GPSLatitudeRef")
        )
        lon = dms_to_decimal(
            gps_data.get("GPSLongitude"),
            gps_data.get("GPSLongitudeRef")
        )

        if lat is not None and lon is not None:
            st.success("Location detected")
            st.write(f"**Latitude:** {lat}")
            st.write(f"**Longitude:** {lon}")

            map_url = f"https://www.google.com/maps?q={lat:.6f},{lon:.6f}"


            if st.button("🌍 Open location in Google Maps"):
                webbrowser.open(map_url)
        else:
            st.warning("GPS field exists, but no valid coordinates found.")
    else:
        st.info("No GPS coordinates found.")

    #METADATA section
    st.subheader("Metadata Information")

    if exif_data is None:
        st.write("No EXIF metadata found.")
    else:
        for tag_id, value in exif_data.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)

            if tag == "GPSInfo":
                st.write("**GPSInfo:** [GPS field present]")
            else:
                st.write(f"**{tag}:** {value}")


    # ---------- EXPORT METADATA SECTION ----------
    st.subheader("Export Metadata")

    if exif_data:

        # Convert metadata into readable dictionary
        metadata_dict = {}

        for tag_id, value in exif_data.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)

            # Convert bytes to string --- if needed
            if isinstance(value, bytes):
                try:
                    value = value.decode(errors="ignore")
                except:
                    value = str(value)

            metadata_dict[str(tag)] = str(value)

        # TXT EXPORT
        txt_buffer = io.StringIO()
        for key, value in metadata_dict.items():
            txt_buffer.write(f"{key}: {value}\n")

        st.download_button(
            label="Download Metadata as TXT",
            data=txt_buffer.getvalue(),
            file_name="metadata.txt",
            mime="text/plain"
        )

        # JSON EXPORT
        json_buffer = io.StringIO()
        json.dump(metadata_dict, json_buffer, indent=4)

        st.download_button(
            label="Download Metadata as JSON",
            data=json_buffer.getvalue(),
            file_name="metadata.json",
            mime="application/json"
        )

        # CSV EXPORT
        csv_buffer = io.StringIO()
        writer = csv.writer(csv_buffer)
        writer.writerow(["Tag", "Value"])

        for key, value in metadata_dict.items():
            writer.writerow([key, value])

        st.download_button(
            label="Download Metadata as CSV",
            data=csv_buffer.getvalue(),
            file_name="metadata.csv",
            mime="text/csv"
        )

    else:
        st.info("No metadata available to export.")


    # METADATA removal
    st.subheader("Remove Metadata")

    if st.button("🧹 Remove Metadata from Image"):
        clean_image = Image.new(image.mode, image.size)
        clean_image.putdata(list(image.getdata()))

        buffer = io.BytesIO()
        clean_image.save(buffer, format="JPEG")
        buffer.seek(0)

        st.success("Metadata removed successfully!")

        st.download_button(
            label="⬇ Download Clean Image",
            data=buffer,
            file_name="image_without_metadata.jpg",
            mime="image/jpeg"
        )

