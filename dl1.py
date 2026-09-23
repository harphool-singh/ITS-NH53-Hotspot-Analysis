import os
import requests

# Step 1: Create folder to save images
folder_path = "images"
os.makedirs(folder_path, exist_ok=True)

# Step 2: List of image URLs
image_urls = [
    "https://images.unsplash.com/photo-1581090700227-7e6f2e3a2b8c",
    "https://images.unsplash.com/photo-1593642634443-44adaa06623a",
    "https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d",
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085",
    "https://images.unsplash.com/photo-1517423440428-a5a00ad493e8",
    "https://images.unsplash.com/photo-1534081333815-ae5019106622",
    "https://images.unsplash.com/photo-1502764613149-7f1d229e230f",
    "https://images.unsplash.com/photo-1481277542470-605612bd2d61"
]

# Step 3: Download all images
for i, url in enumerate(image_urls, start=1):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(folder_path, f"img{i}.jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded img{i}.jpg")
    else:
        print(f"Failed to download image {i}")

print("All images downloaded successfully!")
