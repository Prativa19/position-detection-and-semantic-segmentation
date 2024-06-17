# position-detection-and-semantic-segmentation
## Requirements

- **Operating System:** FSOCO Tools are supported only on Linux. Ubuntu 18.04, 20.04, and 22.04 are tested and recommended.
- **Python:** Version 3.8 (Anaconda or virtualenv recommended).
- **Optional:** GPU for enhanced performance.

## Installation Steps

1. **Create a Python Environment**
   
   Use Conda to create a new environment with Python 3.8:
     ```bash
     conda create -n myenv python=3.8

2. **Activate the Environment**
     
     ```bash
     conda activate myenv
     
3. **Upgrade pip**

     Upgrade pip to version 19.3.0 or later.
     ```bash
     pip install --upgrade pip
     
4. **Install Setuptools**
   
     Install a compatible version of Setuptools (version 60.8.2 recommended due to a bug in 60.9.0):
     ```bash
      pip install setuptools==60.8.2
     
5. **Install FSOCO Tools**
   
   # Make sure you are in the tools directory, otherwise adjust the '.' path to point to it.
   # Use Setuptools configuration to install tools to environment
   # For usage of the CLI tools only
     ```bash
     pip install --editable .[sly]
    ## For development install additional dependencies from requirements.txt and set up pre-commit hooks:
    ```bash
    pip install -r requirements.txt
    pre-commit install

    ## you have just installed the FSOCO tools python package
  6. **Verify Installation**
     ```bash
     fsoco --help
     
