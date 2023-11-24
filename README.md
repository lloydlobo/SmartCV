# SmartCV

Craft personalized resumes with `SmartCV` using `CSS` precision and on-the-fly
`YAML` configuration.

SmartCV is a Python script that generates a CV (Curriculum Vitae) from YAML data
using Jinja2 templates.

## Features

- **Flexible YAML Data:** Single source for loading data via a `yaml` file.
  No more jumping around while editing CVs.
- **Configuration:** Easily configurable through the `SmartCVConfig` class.
- **Easy Templating:** Ability to edit and style as one pleases. (Just the
  basics of `HTML` and `CSS` are required.) Uses Jinja2 templates to render the
  CV content.
- **Output Formats:** Generates HTML output and copies associated CSS file.
- **Automation:** Automated configuration setup and file handling.
    - Edit CV in any text-editor and watch changes in the browser.
    - [ ] TODO: Add hot-reloading for the `python` compilation script.

## Sample Preview

<details>
  <summary>Preview Input Data</summary>
  <p>

### Input `yaml` Data

  ```yaml
  name: Jane Smith
  contact:
    email: janesmith@example.com
    phone: +1234567891
    address: Abbey Road
    website: https://example.com
  summary: >-
    I enjoy creating meaningful programs and collaborating for quality results.
    Eager to contribute my skills to an integrity-driven software environment.
  experience:
    - company: Amazon
      title: Data Engineer
      dates: 2021–Present
      responsibilities:
        - Implemented data processing pipelines using Python and Spark.
        - Collaborated with diverse teams for successful project delivery.
        - Optimized and maintained data infrastructure to ensure data quality, integrity, and availability.
    - company: Microsoft
      title: Software Developer
      dates: 2016–2021
      responsibilities:
        - Built web applications using TypeScript and Angular.
        - Collaborated with cross-functional teams to meet project deadlines.
        - Participated in code reviews and provided constructive feedback to enhance code quality and maintainability.
    - company: Apple
      title: iOS Developer
      dates: 2014–2016
      responsibilities:
        - Developed user-friendly iOS applications using Swift.
        - Collaborated with UX/UI designers to enhance app visuals.
        - Conducted debugging, testing, and optimization of iOS applications to ensure a smooth user experience.
  projects:
    - name: Exciting travel app
      description: Explore new places while checking real-time weather details.
      url: https://gitsample.com/exciting-travel-app
    - name: Innovative finance app
      description: Manage your finances with ease using this cutting-edge app.
      url: https://gitsample.com/innovative-finance-app
    - name: Futuristic health app
      description: Stay fit and healthy with personalized health insights.
      url: https://gitsample.com/futuristic-health-app
  skills:
    - languages:
        - TypeScript
        - Python
        - HTML
        - CSS
        - JavaScript
        - Java
        - Kotlin
    - traits:
        - Problem Solver
        - Team Player
        - Innovative Thinker
    - talents:
        - User Experience Design
        - Agile Development
  education:
    - institution: Harvard University
      degree: Bachelor of Science
      major: Computer Science
      dates: 2012–2016
    - institution: Stanford University
      degree: Master of Science
      major: Computer Science
      dates: 2016–2018
  ```

  </p>
</details>


<details>
  <summary>Preview Output CV</summary>
  <p>

### Output CV PDF Image

![SmartCV_example](https://github.com/lloydlobo/SmartCV/assets/76430758/e3ddfaff-3f08-482e-be84-0749b8cd2d13)

  </p>
</details>

## Prerequisites

- Python 3.x
- Required Python packages can be installed using:

  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. Configure SmartCV by editing the `SmartCVConfig` class in the script.
2. Ensure your YAML data is in the specified format in the input file.
3. Run the script:

    ```shell
    python main.py
    ```

4. Check the `build` directory for the generated CV HTML file (`cv.html`) and
   associated CSS file.

## Configuration

Edit the `SmartCVConfig` class in the script to customize the CV generation:

- `build_dir`: Directory for generated files.
- `css_file`: Name of the CSS file.
- `input_yaml`: Input YAML file with CV data.
- `templates_dir`: Directory containing Jinja2 templates.
- `template_file`: Name of the Jinja2 template file.
- `output_html`: Name of the generated HTML file.
- <s>`output_pdf`: Name of the generated PDF file (currently in the
  backlog).</s>

## License

This project is licensed under the AGPL-3.0 license - see the [LICENSE](LICENSE)
file for details.

## Acknowledgments

- [Jinja2](https://jinja.palletsprojects.com/) - Template engine used.
- [PyYAML](https://pyyaml.org/) - YAML parser for Python.

[//]: # (- [WeasyPrint]&#40;https://weasyprint.org/&#41; - In the backlog for PDF generation.)