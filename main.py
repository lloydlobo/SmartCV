import os
import shutil
import sys

import yaml
from jinja2 import Environment
from jinja2 import FileSystemLoader

YAML_FILE_PATH = ".SmartCV.data.yml"
template_dir, template_file = "templates", "resume_template.html"
css_file = "style_resume_template.css"
build_dir = "build"

# ------------------------------------------------------------------------------

yaml_data: any
with open(YAML_FILE_PATH, "r") as base_data_file:
    yaml_data = yaml.safe_load(base_data_file)
yaml_output = yaml.dump(yaml_data, default_flow_style=False, sort_keys=False)

# ------------------------------------------------------------------------------


class SmartCV:
    """ """

    def __init__(self, name):
        self.name = name

    def generate_resume(self):
        """ """
        resume = []
        resume.append(f"Name: {self.name}")

        return "\n".join(resume)


# ------------------------------------------------------------------------------


def generate_resume(yaml_file, template_file, output_pdf):
    """

    :param yaml_file:
    :param template_file:
    :param output_pdf:

    """
    # --------------------------------------------------------------------------
    # Load YAML data
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # --------------------------------------------------------------------------
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("resume_template.html")

    # --------------------------------------------------------------------------
    # Render the template with YAML data
    rendered_resume = template.render(data=data)
    return rendered_resume

    # --------------------------------------------------------------------------
    # Generate PDF using WeasyPrint
    # HTML(string=rendered_resume).write_pdf(output_pdf)


def main():
    """ """
    dir_root = os.path.dirname(os.path.dirname(__file__))
    template_file = os.path.join(dir_root, "resume_template.html")

    html_resume = generate_resume(
        ".SmartCV.data.yml", template_file, "output_resume.pdf"
    )

    # dir_build = os.path.join(dir_root, "build")
    os.makedirs("build", exist_ok=True)
    with open(
        os.path.join("build", "resume.html"), "w", encoding="utf-8"
    ) as html_output_file:
        print(html_resume)
        html_output_file.write(html_resume)
        shutil.copy(
            src=os.path.join(template_dir, css_file),
            dst=os.path.join(build_dir, css_file),
        )


if __name__ == "__main__":
    sys.exit(main())
