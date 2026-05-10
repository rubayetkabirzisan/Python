import concurrent.futures
import requests
import os

def downloadFile(url, name):
    try:
        print(f"Started Downloading {name}")
        response = requests.get(url)
        
        # Make sure the directory exists
        if not os.path.exists("files"):
            os.makedirs("files")
        
        # Write the image to the file
        with open(f"files/file{name}.jpg", "wb") as f:
            f.write(response.content)
        
        print(f"Finished Downloading {name}")
    except Exception as e:
        print(f"Error downloading file {name}: {e}")

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"
    
    # Create lists of URLs and corresponding names
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]

    # Using ProcessPoolExecutor for parallel download
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            pass  # No need to print r, the download process logs its own output

