<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/adrbn/CopyWeb">
    <img src="images/copyweb_logo.png" alt="Logo" width="150" height="150">
  </a>

  <p align="center">
    A simple tool to download and save webpages locally!
    <br />
    <a href="https://github.com/adrbn/CopyWeb"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/adrbn/CopyWeb">View Demo</a>
    ·
    <a href="https://github.com/adrbn/CopyWeb/issues">Report Bug</a>
    ·
    <a href="https://github.com/adrbn/CopyWeb/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Example](#example)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

![Example Image](images/example.png)

CopyWeb is a Python script designed to download a web page and its assets, including HTML, CSS, JavaScript, and images, to a local directory. This tool is useful for creating offline copies of websites.

### Built With

* [Python](https://www.python.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://docs.python-requests.org/en/latest/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have the following installed:

* Python 3.x
* `requests` library
* `beautifulsoup4` library

You can install the required Python libraries using pip:

```
pip install requests beautifulsoup4
```

### Installation

1. Clone the repository:

```
git clone https://github.com/adrbn/CopyWeb.git
cd CopyWeb
```

2. Run the script:

```
python copyweb.py
```

<!-- USAGE EXAMPLES -->
## Usage

1. Enter the URL of the website you want to download when prompted.

2. The script will create a directory named after the domain of the website and save the downloaded files there.

### Example

If you run the script and enter `https://example.com`, the script will create a directory structure like this:

```
example_com/
└── index/
    ├── index.html
    ├── css/
    │   └── <hashed_filenames>.css
    ├── js/
    │   └── <hashed_filenames>.js
    └── images/
        └── <hashed_filenames>.<extension>
```

_For more examples, please refer to the [Documentation](https://github.com/adrbn/CopyWeb)_.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Othneil Drew - Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Choose an Open Source License](https://choosealicense.com)

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshot.png

