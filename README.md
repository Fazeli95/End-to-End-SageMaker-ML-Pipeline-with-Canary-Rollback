# End-to-End SageMaker-ML-Pipeline-with-Canary-Rollback

**Author:** Pooya Fazeli  
**Email:** [pooya.fazeli@gmail.com](mailto:pooya.fazeli@gmail.com)  
**GitHub:** [github.com/fazeli95](https://github.com/fazeli95)

This project and its contents are the intellectual property of Pooya Fazeli. Unauthorized use, distribution, or reproduction of this work is prohibited. Please refer to the MIT License for permitted uses and conditions.

---


## Project Overview
This project demonstrates an end-to-end machine learning pipeline using Amazon SageMaker, including model training, hyperparameter tuning, deployment, and advanced deployment strategies such as canary rollback and shadow testing. The goal of this project is to ensure a robust and reliable model deployment process by validating the model in a production-like environment before fully deploying it.

### Key Features:
- **End-to-End ML Pipeline**: From data preprocessing to model deployment, the entire workflow is covered.
- **AWS SageMaker Integration**: The project leverages AWS SageMaker for training, tuning, and deploying the model.
- **Canary Rollback Strategy**: Gradual model deployment with the ability to rollback in case of failures.
- **Shadow Testing**: Parallel testing of a new model version without impacting end users.

## Project Structure
The project is organized into two main sections:
1. **Original Notebook**: The entire workflow is performed in a single Jupyter notebook, with all outputs preserved. This version is ideal for those who want to see the detailed step-by-step process, including intermediate results and outputs.
2. **Structured Project**: For better readability and modularity, the project has been refactored into a structured format with separate scripts and a clean notebook. This version is suitable for those who prefer a more organized and professional presentation of the code.

### Repository Contents:

End-to-End-SageMaker-ML-Pipeline-with-Canary-Rollback/

    │
    ├── README.md                                  # Project overview, setup instructions, and more
    ├── requirements.txt                           # List of dependencies to run the project
    ├── Full_Notebook.ipynb                    # Your original notebook with all outputs preserved
    └── structured_project/                        # Folder containing the structured version of the project
        ├── Structured_Notebook.ipynb              # The structured notebook without outputs (code only)
        ├── src/
        │   ├── data_preprocessing.py              # Script for data preprocessing
        │   ├── model_training.py                  # Script for model training
        │   ├── hyperparameter_tuning.py           # Script for hyperparameter tuning
        │   ├── deployment.py                      # Script for deploying the model
        │   └── inference.py                       # Script for performing inference using the deployed model


## Setup and Installation

To get started with the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/End-to-End-SageMaker-ML-Pipeline-with-Canary-Rollback.git
   cd End-to-End-SageMaker-ML-Pipeline-with-Canary-Rollback
   
2. **Install the required dependencies:**
   pip install -r requirements.txt

## Dataset
The dataset used in this project is the SBA-Loans-Case-Data-Set, which can be accessed from [OpenML](https://api.openml.org/d/43539). The data will be automatically downloaded when you run the notebook.

## Usage

### Running the Original Notebook:
- Open `Original_Notebook.ipynb` to view the full workflow, including all outputs.
- This notebook contains every step from data preprocessing to model deployment, including the outputs at each stage.

### Running the Structured Project:
- Navigate to the `structured_project/` folder.
- Open `Structured_Notebook.ipynb` to view the clean, modular version of the project.
- Alternatively, run the individual scripts in the `src/` folder for specific tasks such as data preprocessing, model training, or deployment.

## Canary Rollback and Shadow Testing

### Canary Rollback:
- **Description**: Gradual deployment of the new model version with a rollback mechanism in case of failures.
- **Implementation**: In the event of errors during deployment, the traffic is rolled back to the previous stable version to ensure reliability.

### Shadow Testing:
- **Description**: The new model version is deployed in parallel with the production model, receiving the same traffic without affecting users.
- **Purpose**: This allows for validation of the new model’s performance in a production-like environment before full deployment.

## Results
The model had reliable performance metrics during training and validation phases. Canary deployment and shadow testing ensured a robust and error-free transition to production.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
