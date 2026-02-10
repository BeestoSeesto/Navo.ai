"""
Navo - Legal Situation Explainer
Helps people understand confusing legal situations in plain English
WITHOUT giving legal advice
"""

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

# Your exact system prompt
NAVO_SYSTEM_PROMPT = """You are an AI that helps users understand confusing situations by explaining things in simple, plain English. You do not give legal advice. You do not tell people what to do. You do not make predictions, evaluate case strength, or suggest strategy.

Your job is only to provide:

• What the situation might involve
• General themes or issues people in similar situations often describe
• What general factors usually matter in situations like this
• What people commonly think about or consider
• What questions people often ask when they later speak to counsel
• Emotional grounding and clarity
• Plain-English summaries

If the user asks for legal advice, strategy, predictions, timelines, or whether they "have a case," you MUST respond with:

"I can't give legal advice or tell you what to do. I can only explain the situation in general terms and show what people in similar situations often consider."

Keep all responses 6–8 sentences, simple, human, and clear. Avoid all legal instructions, directives, or recommendations.

OUTPUT FORMAT:

Follow this structure:

1. Plain-English Overview (What this might relate to)
2. Common Factors People Notice (Neutral, general)
3. What People in Similar Situations Often Think About (Not advice)
4. Questions People Often Ask Counsel (Safe + helpful)
5. Disclaimer: "This isn't legal advice — just a general explanation to help you understand what you're dealing with until you seek counsel."
"""


class NavoExplainer:
    """Core Navo explanation engine"""
    
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")
        )
    
    def explain_situation(self, user_situation: str) -> str:
        """
        Takes user's description of their situation
        Returns plain-English explanation (NOT legal advice)
        """
        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1500,
                system=NAVO_SYSTEM_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": user_situation
                    }
                ]
            )
            return message.content[0].text
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def format_explanation(self, explanation: str) -> str:
        """Format the explanation for display"""
        return f"""
{'='*80}
NAVO EXPLANATION
{'='*80}

{explanation}

{'='*80}
Remember: This is not legal advice. Speak with a qualified attorney for guidance
on your specific situation.
{'='*80}
"""


def main():
    """Command-line interface for Navo"""
    print("\n" + "="*80)
    print("NAVO - Legal Situation Explainer")
    print("="*80)
    print("\nDescribe your situation in plain English.")
    print("Navo will help you understand what might be going on.\n")
    print("Type 'quit' to exit.\n")
    
    explainer = NavoExplainer()
    
    while True:
        print("-" * 80)
        user_input = input("\nDescribe what happened: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nThanks for using Navo. Remember to consult with an attorney.")
            break
        
        if not user_input:
            print("Please describe your situation.")
            continue
        
        print("\n🔍 Analyzing your situation...\n")
        explanation = explainer.explain_situation(user_input)
        formatted = explainer.format_explanation(explanation)
        print(formatted)


if __name__ == "__main__":
    main()
