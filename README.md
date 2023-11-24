# SmartCV

Craft personalized resumes with `SmartCV` using `CSS` precision and on-the-fly
`YAML` configuration.

## Features

- One central source for truth in a `yaml` file. No more jumping around while
  editing CVs.
- Ability to edit and style as one pleases. (Just the basics of `HTML` and `CSS`
  are required.)
- Edit CV in any text-editor and watch changes in the browser.
  - [ ] TODO: Add hot-reloading for the `python` compilation script.

## Sample Preview

### Input `yaml`

```yaml
name: Jane Smith
contact:
  email: janesmith@example.com
  phone: (+987)-654-3210
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

### Output Resume

![SmartCV_example](https://github.com/lloydlobo/SmartCV/assets/76430758/e3ddfaff-3f08-482e-be84-0749b8cd2d13)
