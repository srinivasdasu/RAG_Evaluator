import logging
from rouge_score import rouge_scorer
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RAGEvaluator:
    def __init__(self, knowledge_base, questions_and_answers):
        """
        Initializes the RAGEvaluator with a knowledge base and question-answer pairs.
        
        Args:
            knowledge_base (dict): A dictionary containing questions and their corresponding answers.
            questions_and_answers (dict): A dictionary of questions and expected answers for evaluation.
        """
        self.knowledge_base = knowledge_base
        self.questions_and_answers = questions_and_answers
        self.scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

    def retrieve_answer(self, question):
        """Retrieve the answer from the knowledge base for a given question."""
        answer = self.knowledge_base.get(question, "No information found.")
        logger.info(f"Retrieved answer for '{question}': {answer}")
        return answer

    def generate_answer(self, context):
        """
        Generate an answer based on the retrieved context.
        
        Args:
            context (str): The context retrieved for generating an answer.
        
        Returns:
            str: A generated answer based on the context.
        """
        # Simple generation logic for demonstration purposes
        generated_answer = f"Based on the context, {context}"
        logger.info(f"Generated answer: {generated_answer}")
        return generated_answer

    def evaluate_correctness(self, retrieved_answer, expected_answer):
        """Evaluate if the retrieved answer is correct compared to the expected answer."""
        is_correct = retrieved_answer == expected_answer
        logger.info(f"Correctness for answer: {is_correct}")
        return is_correct

    def evaluate_rouge(self, expected_answer, retrieved_answer):
        """
        Calculate ROUGE scores between the expected and retrieved answers.
        
        Args:
            expected_answer (str): The expected correct answer.
            retrieved_answer (str): The answer retrieved from the knowledge base.
        
        Returns:
            dict: ROUGE scores for 'rouge1', 'rouge2', and 'rougeL'.
        """
        try:
            scores = self.scorer.score(expected_answer, retrieved_answer)
            logger.info(f"ROUGE Scores: {scores}")
            return scores
        except Exception as e:
            logger.error(f"Error calculating ROUGE scores: {e}")
            return {}

    def evaluate(self):
        """Perform the RAG evaluation for all questions."""
        for question, expected_answer in self.questions_and_answers.items():
            try:
                # Step 1: Retrieve answer from the knowledge base
                retrieved_answer = self.retrieve_answer(question)
                
                # Step 2: Generate answer based on the retrieved context
                generated_answer = self.generate_answer(retrieved_answer)
                
                # Step 3: Evaluate correctness
                self.evaluate_correctness(generated_answer, expected_answer)
                
                # Step 4: Evaluate ROUGE scores
                self.evaluate_rouge(expected_answer, generated_answer)
            except Exception as e:
                logger.error(f"Error evaluating question '{question}': {e}")

if __name__ == "__main__":
    # Sample knowledge base
    knowledge_base = {
        "What is the capital of Andhra Pradesh?": "Amaravati is the capital of Andhra Pradesh.",
        "What languages are spoken in Andhra Pradesh?": "Telugu is the primary language spoken in Andhra Pradesh.",
        "When was Andhra Pradesh formed?": "Andhra Pradesh was formed on November 1, 1956.",
        "What is a popular festival celebrated in Andhra Pradesh?": "Sankranti is a popular festival celebrated in Andhra Pradesh.",
        "Which prominent temple is located in Andhra Pradesh?": "The Tirupati temple is a prominent temple in Andhra Pradesh."
    }

    # Sample questions and expected answers
    questions_and_answers = {
        "What is the capital of Andhra Pradesh?": "Based on the context, Amaravati is the capital of Andhra Pradesh.",
        "What languages are spoken in Andhra Pradesh?": "Based on the context, Telugu is the primary language spoken in Andhra Pradesh.",
        "When was Andhra Pradesh formed?": "Based on the context, Andhra Pradesh was formed on November 1, 1956.",
        "What is a popular festival celebrated in Andhra Pradesh?": "Based on the context, Sankranti is a popular festival celebrated in Andhra Pradesh.",
        "Which prominent temple is located in Andhra Pradesh?": "Based on the context, The Tirupati temple is a prominent temple in Andhra Pradesh."
    }

    evaluator = RAGEvaluator(knowledge_base, questions_and_answers)
    evaluator.evaluate()
