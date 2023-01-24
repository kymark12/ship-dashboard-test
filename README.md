# Ship Dashboard Test Automation

## Overview
This repo automates the tests for the following scenarios:
 
- Input validation
- Search result verification
- Front-end output and API response cross-reference validation

## How to set up the framework on your local

🔵 Add <b><a href="https://www.python.org/downloads/">Python</a></b> and <b><a href="https://git-scm.com/">Git</a></b> to your System PATH.

🔵 Using a <a href="https://github.com/seleniumbase/SeleniumBase/blob/master/help_docs/virtualenv_instructions.md">Python virtual env</a> is recommended.

### Install the dependencies
After setting up python and a virtual environment you can install the requirements via `requirements.txt`
```bash
pip install -r requirements.txt
```

## How to run the tests
### On local
You can simply run the tests by:
```bash
pytest -vv
```
The test may run fast to the point of not seeing it execute, to slow things down where we can view what's happening:
```bash
pytest --demo -vv
```

### Using GitHub Actions
<aside>
💡 Note: This is unusable now, since I have to deploy the web app on a cloud server
</aside>

But you can run the test (Although it will fail) via GitHub Actions on the Action tab of this repo:

- Click `CI Build`
- Click `Run Workflow`
- Then on the pop-up window click `Run Workflow` again
