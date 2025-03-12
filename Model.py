import google.generativeai as genai
import os
from dotenv import load_dotenv

class MyModel:
    def __init__(self):
        # api in .env file loading it 
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        # inserting the api key to the google generative ai
        genai.configure(api_key=self.API_KEY)
        # Model selection
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Define system prompt
        self.system_prompt = """You are an AI assistant specialized in providing cost of living insights. You should:
- Provide detailed cost breakdowns for different locations
- Include information about housing, utilities, food, and transportation
- Compare costs with national averages
- Suggest budget-friendly alternatives
- Be clear and specific with numbers and statistics
- Format responses in an easy-to-read manner"""

    def generate_response(self, user_prompt):
        try:
            formatted_prompt = f"""You are an AI assistant specialized in providing cost of living insights. 
            
For the following location query: "{user_prompt}"

Please provide:
- Detailed cost breakdowns
- Try to bold the amount of money reqiured
- do not use table format instead use bullet points
- Housing costs (rent and property prices)
- Utility costs (electricity, water, internet)
- Food and grocery expenses
- Transportation costs
- Healthcare costs
- Entertainment and leisure expenses
- Comparison with national averages
- Budget-friendly tips for this location
- At Last give the total cost of living for the location per month

Format the response in a clear, structured manner with specific numbers and statistics."""

            response = self.model.generate_content(formatted_prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                return """Server Error Please try again later.. :("""
            return f"An error occurred: {str(e)}"