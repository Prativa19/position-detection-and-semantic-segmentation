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
     ```bash
     pip install --upgrade pip
     
  4. **Install Setuptools**
     Install a compatible version of Setuptools (version 60.8.2 recommended due to a bug in 60.9.0):
     ```bash
      pip install setuptools==60.8.2
  6. **Install FSOCO Tools**
  7. Navigate to the directory containing FSOCO Tools and install:
     ```bash
     pip install --editable .[sly]
    ## For development
    ```bash
    pip install -r requirements.txt
    pre-commit install
  8. **Verify Installation**
     ```bash
     fsoco --help
     
