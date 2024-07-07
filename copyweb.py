import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
import hashlib
import shutil
from mimetypes import guess_extension

# Function to create directories if they don't exist
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to generate a hash for filenames
def hash_url(url):
    return hashlib.md5(url.encode('utf-8')).hexdigest()

# Function to download a file and determine its correct extension
def download_file(session, url, path):
    try:
        response = session.get(url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        extension = guess_extension(content_type.split(';')[0])
        if extension in ['.jpe', '.jpeg']:
            extension = '.jpg'
        full_path = f"{path}{extension}"
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} as {full_path}")
        return full_path
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None

# Function to download HTML and its assets
def download_website(url, save_dir):
    create_dir(save_dir)
    session = requests.Session()

    try:
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Save the main HTML file
        html_path = os.path.join(save_dir, 'index.html')
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        print(f"Saved main HTML file to {html_path}")

        # Download CSS files
        for link in soup.find_all('link', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            filename = hash_url(full_url)
            file_path = os.path.join(save_dir, 'css', filename)
            create_dir(os.path.dirname(file_path))
            new_path = download_file(session, full_url, file_path)
            if new_path:
                link['href'] = os.path.relpath(new_path, start=save_dir)

        # Download JS files
        for script in soup.find_all('script', src=True):
            src = script['src']
            full_url = urljoin(url, src)
            filename = hash_url(full_url)
            file_path = os.path.join(save_dir, 'js', filename)
            create_dir(os.path.dirname(file_path))
            new_path = download_file(session, full_url, file_path)
            if new_path:
                script['src'] = os.path.relpath(new_path, start=save_dir)

        # Download Images
        for img in soup.find_all('img', src=True):
            src = img['src']
            full_url = urljoin(url, src)
            filename = hash_url(full_url)
            file_path = os.path.join(save_dir, 'images', filename)
            create_dir(os.path.dirname(file_path))
            new_path = download_file(session, full_url, file_path)
            if new_path:
                img['src'] = os.path.relpath(new_path, start=save_dir)

        # Save the modified HTML file with updated paths
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        print(f"Updated HTML file saved to {html_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the main page {url}: {e}")

# Ask user for the URL
website_url = input("Please enter the URL of the website to download: ")
parsed_url = urlparse(website_url)
domain_name = parsed_url.netloc.replace('.', '_')
page_name = os.path.basename(parsed_url.path.strip('/')) or 'index'
save_directory = os.path.join(os.getcwd(), domain_name, page_name)

# Start the download process
print(f"Starting download of {website_url}...")
download_website(website_url, save_directory)

print(f"Website downloaded and saved to {save_directory}")
