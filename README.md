# Query Classification System

A machine learning-based system that classifies student queries into Academic, Course, and Technical categories using Word2Vec embeddings and Random Forest classification.

## Key Features

- **Multi-class Classification**: Categorizes queries into Academic, Course, and Technical types
- **Text Preprocessing**: Comprehensive text cleaning including slang conversion, punctuation removal, and emoji handling
- **Word2Vec Embeddings**: Custom-trained Word2Vec model on educational query data for better semantic understanding

## Tech Stack

### Programming Language
- **Python 3.x**

### Machine Learning & Data Processing
- **scikit-learn**: Random Forest classifier and model evaluation
- **gensim**: Word2Vec model training and embeddings
- **numpy**: Numerical computations
- **pandas**: Data manipulation and analysis

### Natural Language Processing
- **NLTK**: Text tokenization and preprocessing

### Additional Libraries
- **pickle**: Model serialization
- **json**: JSON data handling
- **warnings**: Warning management
- **string**: String processing utilities

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Query_Classification
```

2. Install required dependencies:
```bash
pip install flask scikit-learn gensim numpy pandas mysql-connector-python emoji nltk
```
4. Ensure model files are present:
   - `ngasce_word2vec.pkl`
   - `rf_classifier.pkl`

## Usage

### Running the Flask API

```bash
python app_classifier.py
```

The API will be available at `http://127.0.0.1:5000/`

### API Endpoint

**GET** `/result/<query>`

Example:
```
http://127.0.0.1:5000/result/when%20are%20the%20classes%20starting
```

Response:
- "Academic query" - For academic-related questions
- "Course query" - For course-specific questions
- "Technical query" - For technical/administrative issues
- "Invalid query" - For unclassifiable queries

### Using the Classifier Directly

```python
from classifier import result

query = "when are the classes starting"
classification = result(query)
print(classification)  # Output: "Academic query"
```

## Model Performance
- **Training Data**: 63,000+ queries from educational platform
- **Features**: 100-dimensional Word2Vec embeddings
- **Algorithm**: Random Forest with default hyperparameters

## Data Processing Pipeline

1. **Text Cleaning**: Convert to lowercase, remove punctuation
2. **Tokenization**: Split text into words
3. **Vectorization**: Convert to Word2Vec embeddings
4. **Classification**: Predict using Random Forest model