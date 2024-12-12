import os
import shutil
from copystatic import copy_files_recursive
from generatepage import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
content_path = "./content/index.md"
template_path = "./template.html"
output_path = "./public/index.html"

def main():
    print("deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating HTML page")
    generate_page(content_path, template_path, output_path)    
    
main()
