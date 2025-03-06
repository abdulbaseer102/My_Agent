#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from research_agent.crew import ResearchAgent

warnings.filterwarnings("ignore", category=SyntaxWarning)

def run():
    """Run the Crew"""
    inputs = {
        'image_path': 'https://photographylife.com/wp-content/uploads/2014/09/Nikon-D750-Image-Samples-2.jpg',
        'current_year': str(datetime.now().year)
    }
    
    try:
        ResearchAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """Train the Crew"""
    inputs = {
        "image_path": "https://photographylife.com/wp-content/uploads/2014/09/Nikon-D750-Image-Samples-2.jpg",
        'current_year': str(datetime.now().year)
    }
    try:
        ImageAnalysisCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """Replay the Crew Execution"""
    try:
        ImageAnalysisCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """Test the Crew Execution"""
    inputs = {
        "image_path": "images/sample.jpg"
    }
    try:
        ImageAnalysisCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
