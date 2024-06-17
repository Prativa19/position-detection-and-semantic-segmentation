# position-detection-and-semantic-segmentation
## Requirements

- **Operating System:** FSOCO Tools are supported only on Linux. Ubuntu 18.04, 20.04, and 22.04 are tested and recommended.
- **Python:** Version 3.8 (Anaconda or virtualenv recommended).
- **Optional:** GPU for enhanced performance.

## Installation Steps

1. **Create a Python Environment**

   Use Conda to create a new environment with Python 3.8:

   ```bash
   conda create -n fsoco python=3.8

  2. **Activate the Environment**
    conda activate myenv
  3.**Upgrade pip**
     pip install --upgrade pip
  4. **Install FSOCO Tools**
     pip install --editable .[sly]
     pip intsall -r requirements.txt
     pre-commit install
  5. **Verify Installation**
     fsoco --help
