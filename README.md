# Intelligent Recruitment System

This project is an **Intelligent Recruitment System** designed to evaluate candidates' resumes and match them with job vacancies based on their skills, experience, and qualifications. The system integrates various AWS services to create an efficient, scalable, and automated solution for processing candidate data and training machine learning models.

---

## Architecture Overview

The system's architecture consists of the following key components:

1. **Data Sources**: Input data is collected in CSV format, including:
   - Candidate information (`Candidates`)
   - Job vacancies (`Vacants`)
   - Work experience (`Work Experience`)

2. **Data Storage**:
   - CSV files are imported into an on-premises **Microsoft SQL Server**.
   - SQL Server is replicated to **Amazon RDS** for scalable cloud-based data management.

3. **Data Transformation**:
   - **AWS Glue** is used for ETL (Extract, Transform, Load) processes to clean and transform the data for further analysis.

4. **Data Storage and Access**:
   - Transformed data is stored in **Amazon S3** for scalable and secure storage.

5. **Machine Learning**:
   - **Amazon SageMaker** is used to train machine learning models that:
     - Analyze candidate compatibility with job vacancies.
     - Rank candidates based on skills and experience.

6. **Visualization**:
   - Processed data and results are visualized using a third-party BI tool or custom dashboard.

---

## Project Structure

The repository is structured as follows:

```
.
├── data/                     # Sample input CSV files
├── scripts/                  # ETL and preprocessing scripts
├── models/                   # Machine learning models and training scripts
├── notebooks/                # Jupyter notebooks for analysis and experimentation
├── aws-config/               # AWS Glue and SageMaker configurations
├── visualizations/           # Scripts or tools for creating dashboards
├── README.md                 # Project documentation
└── LICENSE                   # Project license
```

---

## Getting Started

### Prerequisites

1. **AWS Account**: Ensure you have an AWS account with access to the following services:
   - Amazon RDS
   - AWS Glue
   - Amazon S3
   - Amazon SageMaker
2. **Microsoft SQL Server**: Set up a local or cloud SQL Server instance to import initial data.
3. **Python**: Install Python 3.8 or above.
4. **AWS CLI**: Install and configure the AWS CLI for deployment.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/intelligent-recruitment-system.git
   cd intelligent-recruitment-system
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure AWS credentials:
   ```bash
   aws configure
   ```

### Data Preparation

1. Place CSV files in the `data/` folder.
2. Import data into the Microsoft SQL Server instance.
3. Ensure the RDS instance is set up and synchronized with SQL Server.

### Running the ETL Process

1. Upload scripts to AWS Glue.
2. Trigger the Glue job to transform and store data in Amazon S3.

### Training the Model

1. Use SageMaker training scripts in the `models/` directory.
2. Deploy the model for prediction using the SageMaker endpoint.

---

## AWS Services

- **Amazon RDS**: Scalable relational database.
- **AWS Glue**: ETL service for data transformation.
- **Amazon S3**: Storage for transformed data.
- **Amazon SageMaker**: Model training and deployment.

---

## Future Improvements

- Add real-time data processing pipelines.
- Implement a web interface for job matching.
- Optimize ML models for better accuracy and performance.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributors

- [Your Name](https://github.com/your-username)
- [Other Contributors]

For questions or feedback, please open an issue in the repository or contact the contributors.


