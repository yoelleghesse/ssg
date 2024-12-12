# Static Site Generator

This project is a simple static site generator that converts markdown files into HTML pages using a specified template. It also copies static files (like CSS and images) to the output directory.

## Features

- Converts markdown files to HTML
- Uses a template to generate consistent HTML pages
- Copies static files to the output directory
- Supports nested directories for content

## Project Structure
.
├── content
│   └── index.md
├── public
│   └── (generated HTML files and copied static files)
├── static
│   ├── index.css
│   └── images
│       └── rivendell.png
├── template.html
├── src
│   ├── main.py
│   ├── generatepage.py
│   ├── markdown_blocks.py
│   ├── htmlnode.py
│   ├── copystatic.py
│   └── (other source files)
└── main.sh

## Getting Started
### Prerequisites
- Python 3.x
- markdown library (install using pip install markdown)

### Installation
1. Clone the repo
```
git clone https://github.com/yourusername/static-site-generator.git
cd static-site-generator```

2. Install the required packages
```
pip install markdown```

## Usage
1. Place your markdown content files in the content directory.

2. Customize the template.html file to define the structure of your HTML pages.

3. Add any static files (CSS, images, etc.) to the static directory.

4. Run the main.sh script to generate the site and start a local web server: ``` ./main.sh ```

5. Open your web browser and navigate to http://localhost:8888 to view the generated site.