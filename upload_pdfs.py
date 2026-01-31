import requests
import os

# Create directory for PDFs if it doesn't exist
os.makedirs("stored_pdfs", exist_ok=True)

def download_pdfs():
    # Ensure links.txt exists
    if not os.path.exists("links.txt"):
        print("No links.txt file found.")
        return

    with open("links.txt", "r") as f:
        links = [line.strip() for line in f if line.strip()]

    for url in links:
        filename = url.split('/')[-1]
        save_path = os.path.join("stored_pdfs", filename)

        print(f"Downloading {filename}...")
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(response.content)
            else:
                print(f"Failed to download {filename}: Status {response.status_code}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    download_pdfs()
