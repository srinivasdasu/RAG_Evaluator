# RAG Evaluation Program

This program performs a basic Retrieval-Augmented Generation (RAG) evaluation. It uses a predefined knowledge base to retrieve answers for specific questions, generate responses based on those answers, and evaluate the correctness and quality of the generated responses using ROUGE metrics.

## Types of RAG Evaluation

1. **Precision/Recall-based Evaluation**: 
   - Measures how effectively the retrieval system finds relevant documents and how many relevant documents are retrieved.

2. **Answer-Generation Quality**: 
   - Focuses on the quality of the output, using metrics like ROUGE to evaluate how well the generated text matches the expected answer.

3. **End-to-End Task Performance**: 
   - Evaluates the performance of the entire system in completing a task, such as accuracy or F1 score.

### Chosen Type of RAG Evaluation

The chosen evaluation method for this program is **Answer-Generation Quality**. This method is crucial for assessing how accurately the generated response conveys the correct answer to a question.

## Evaluation Metrics

### Correctness
This metric checks if the generated answer matches the expected answer. A binary evaluation determines whether the response is correct.

### ROUGE Scores
- **ROUGE-1**: Evaluates the overlap of unigrams (individual words) between the generated and reference answers.
- **ROUGE-2**: Assesses the overlap of bigrams (pairs of consecutive words) between the generated and reference answers.
- **ROUGE-L**: Analyzes the longest common subsequence between the generated and reference answers, considering word order.

### Context Recall
This can be added as an extension where the relevance of the retrieved context is assessed against the expected answers.

## Reasoning
- **Correctness** ensures the reliability of the answers provided by the system.
- **ROUGE Scores** offer a quantitative way to evaluate how well the generated responses align with the expected outputs, allowing for improvements in the generation process.

## Logger Implementation
The program uses Python’s logging library to record important evaluation results. The logging includes:
- Retrieved answers from the knowledge base.
- Generated answers based on the context.
- Evaluation of correctness.
- Calculation of ROUGE scores.

### Example Logging
```python
logger.info(f"Retrieved answer for '{question}': {answer}")
logger.info(f"Generated answer: {generated_answer}")
logger.info(f"Correctness for answer: {is_correct}")
logger.info(f"ROUGE Scores: {scores}")



## Installation
To run this program, install the required packages listed in `requirements.txt`.

### Requirements.txt



## Usage
1. Clone this repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
