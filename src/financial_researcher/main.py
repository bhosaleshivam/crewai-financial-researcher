#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from dotenv import load_dotenv
from financial_researcher.crew import ResearchCrew

# Load environment variables from .env file
load_dotenv()

# Debug: Print if API key is loaded (remove this after debugging)
api_key = os.getenv('SERPER_API_KEY')
if not api_key:
    print("WARNING: SERPER_API_KEY is not set in environment variables!")
else:
    print("SERPER_API_KEY is loaded (first 4 chars):", api_key[:4] + "..." if api_key else "None")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    inputs = {
        'company': 'Apple'
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()