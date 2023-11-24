from os import makedirs, path
from shutil import copy
from sys import exit

from jinja2 import Environment, FileSystemLoader, Template
from yaml import safe_load


class SmartCVConfig:
    """ """

    def __init__(self, dir_root):
        # Directory path where the script was executed.
        self.dir_root = dir_root

        # ----------------------------------------------------------------------
        # User Config.
        self.build_dir = "build"
        self.css_file = "style_cv_template.css"
        self.input_yaml = ".SmartCV.sample-data.yaml"
        self.templates_dir = "templates"
        self.template_file = "cv_template.html"
        self.output_html = "cv.html"
        self.output_pdf = "output_cv.pdf"

        # ----------------------------------------------------------------------
        # Automated Config.
        self.path_dst_css_file = path.join(self.build_dir, self.css_file)
        self.path_dst_cv_html = path.join(self.build_dir, self.output_html)
        self.path_src_css_file = path.join(self.templates_dir, self.css_file)
        self.path_src_template_file = path.join(self.dir_root, self.template_file)


def generate_cv(config: SmartCVConfig) -> str:
    """

    :param config: SmartCVConfig:
    :param config: SmartCVConfig:
    :param config: SmartCVConfig: 

    """
    # ----------------------------------------------------------------------
    # Load YAML data.
    with open(file=config.input_yaml, mode="r", encoding="utf-8") as file:
        data = safe_load(file)

    # ----------------------------------------------------------------------
    # Load Jinja2 template.
    env = Environment(loader=FileSystemLoader(config.templates_dir))
    template: Template = env.get_template(config.template_file)

    # ----------------------------------------------------------------------
    # Render the template with YAML data.
    rendered_cv: str = template.render(data=data)

    # >> BACKLOG: Generate PDF using WeasyPrint.
    # >> HTML(string=rendered_cv).write_pdf(output_pdf)
    return rendered_cv


def main() -> int:
    """ """
    # ----------------------------------------------------------------------
    # Initialize configuration data class.
    config = SmartCVConfig(dir_root=path.dirname(path.dirname(__file__)))

    # ----------------------------------------------------------------------
    # Generate CV content.
    html_cv: str = generate_cv(config=config)

    # ----------------------------------------------------------------------
    # Write HTML output file and copy CSS file.
    makedirs(config.build_dir, exist_ok=True)  # Ensure build directory exists.
    with open(config.path_dst_cv_html, "w", encoding="utf-8") as dst_html_file:
        dst_html_file.write(html_cv)
        copy(
            src=config.path_src_css_file,
            dst=config.path_dst_css_file,
        )

    return 0  # STATUS_OK.


if __name__ == "__main__":
    exit(main())
