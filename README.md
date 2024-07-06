# Model Comparison API

This repository contains a Django-based backend system that allows users to evaluate and compare multiple language models on various natural language processing tasks. The system helps in analyzing the performance of different models and aids in model selection for specific use cases.

## Features Implemented

1. **RESTful API using Django**: The backend is implemented using Django, providing endpoints for various NLP tasks.
   
2. **Integration of Language Models**: Integrated several pre-trained language models from the Hugging Face Transformers library:
   - BERT (base and large versions)
   - RoBERTa
   - DistilBERT
   - ALBERT
   - XLNet
   - T5 (small and base versions)

3. **Implemented Endpoints for NLP Tasks**:
   - Text Classification
   - Named Entity Recognition (NER)
   - Question Answering (QA)
   - Text Summarization

4. **Additional Features**:
   - Benchmarking: Evaluate models on provided datasets and return performance metrics.
   - Health Check Endpoint: Verify service status and basic usage statistics.
   - Rate Limiting: Prevent abuse of the API.
   - Error Handling: Proper handling of errors and input validation.

5. **Usage of External Libraries**:
   - Transformers from Hugging Face for model management and inference.
   - Django REST Framework for building robust APIs.
   - Other Python libraries for metrics calculation and data handling.

## Setup and Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/model-comparison-api.git
   cd model-comparison-api
   ```

2. **Set up Python environment**:
   ```bash
   # Create a virtual environment (optional but recommended)
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Run Django migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

5. **Accessing the API**:
   - Once the server is running, you can access the API endpoints using tools like curl, Postman, or through your web browser.
   - Endpoints are typically accessed at `http://localhost:8000/api/`.

## API Endpoints

### `/api/task/` (POST)

This endpoint handles different NLP tasks based on the `task_type` parameter:

- **Parameters**:
  - `task_type` (string): Type of NLP task (`text-classification`, `ner`, `qa`, `summarization`).
  - `text` (string): Input text for the NLP task.

- **Example Request**:
  ```json
  {
      "task_type": "text-classification",
      "text": "Sample text for classification."
  }
  ```

- **Response**:
  Returns results from all integrated models for the specified NLP task.

### `/api/benchmark/` (POST)

This endpoint runs benchmarking on provided datasets for various NLP tasks:

- **Parameters**:
  - `task_type` (string): Type of NLP task (`text-classification`, `ner`, `qa`, `summarization`).
  - `dataset` (list of dicts): List of inputs for benchmarking.

- **Example Request**:
  ```json
  {
      "task_type": "text-classification",
      "dataset": [
          {"text": "Sample text 1"},
          {"text": "Sample text 2"}
      ]
  }
  ```

- **Response**:
  Returns performance metrics (e.g., accuracy, F1 score, BLEU score) for each model.

### `/api/health/` (GET)

This endpoint provides the health status of the API service:

- **Example Request**:
  ```bash
  GET /api/health/
  ```

- **Response**:
  ```json
  {
      "status": "ok"
  }
  ```

## Additional Notes

- Ensure you have Python installed (version 3.8+) and set up a virtual environment for the project.
- Make sure to install all dependencies listed in `requirements.txt`.
- For any issues or questions, please refer to the documentation or contact the repository owner.
