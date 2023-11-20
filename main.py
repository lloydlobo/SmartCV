import os
import sys

import yaml
from jinja2 import Environment, FileSystemLoader

pdf_path = 'resume.pdf'
name = "John Doe"
output_pdf_file_path = f'{name.replace(' ', '_')}_resume.pdf'

# ------------------------------------------------------------------------------

YAML_FILE_PATH = '.SmartCV.data.yml'
yaml_data: any
with open(YAML_FILE_PATH, 'r') as base_data_file:
    yaml_data = yaml.safe_load(base_data_file)
yaml_output = yaml.dump(yaml_data, default_flow_style=False, sort_keys=False)


# ------------------------------------------------------------------------------

class SmartCV:
    def __init__(self, name):
        self.name = name

    def generate_resume(self):
        resume = []
        resume.append(f"Name: {self.name}")

        return '\n'.join(resume)


# ------------------------------------------------------------------------------

def generate_resume(yaml_file, template_file, output_pdf):
    # --------------------------------------------------------------------------
    # Load YAML data
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # --------------------------------------------------------------------------
    # Load Jinja2 template
    template_dir, template_file = "templates", "resume_template.html"
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('resume_template.html')

    # --------------------------------------------------------------------------
    # Render the template with YAML data
    rendered_resume = template.render(data=data)
    print(rendered_resume)
    return rendered_resume

    # --------------------------------------------------------------------------
    # Generate PDF using WeasyPrint
    # HTML(string=rendered_resume).write_pdf(output_pdf)


def main():
    dir_root = os.path.dirname(os.path.dirname(__file__))
    template_file = os.path.join(dir_root, 'resume_template.html')

    generate_resume('.SmartCV.data.yml', template_file, 'output_resume.pdf')


if __name__ == "__main__":
    sys.exit(main())
