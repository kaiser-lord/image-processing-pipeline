import os
from google.cloud import storage
from PIL import Image
from io import BytesIO
def process_image(event, context):
    """Triggered by Cloud Storage upload event."""
    # Get event details
    bucket_name = event['bucket']
    file_name = event['name']
    print(f"Processing file: {file_name} from bucket: {bucket_name}")
    # Initialize Storage client
    storage_client = storage.Client()
    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(file_name)
    # Download image to memory
    image_data = source_blob.download_as_bytes()
    image = Image.open(BytesIO(image_data))
    # Resize to thumbnail (200x200)
    thumbnail = image.resize((200, 200))
    thumbnail_io = BytesIO()
    thumbnail.save(thumbnail_io, format=image.format)
    thumbnail_io.seek(0)
    # Upload thumbnail to output bucket
    output_bucket_name = 'gcp-output-images'  # Replace with your output bucket
    output_bucket = storage_client.bucket(output_bucket_name)
    output_blob = output_bucket.blob(f"thumbnail_{file_name}")
    output_blob.upload_from_file(thumbnail_io, content_type=source_blob.content_type)
    print(f"Thumbnail created: thumbnail_{file_name} in {output_bucket_name}")