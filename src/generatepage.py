from markdown_blocks import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html(markdown)
    html_content = html_node.to_html()

    title = extract_title(markdown)

    page_content = template.replace("{{ Content }}", html_content).replace("{{ Title }}", title)

    with open(dest_path, "w") as f:
        f.write(page_content)