from openai import OpenAI
import os
import json
from asyncio.log import logger
from fastapi import HTTPException
from dotenv import load_dotenv
from app.prompt.schema import GenerateReportRequest
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print(f"OpenAI API Key: {api_key}")
if not api_key:
    raise ValueError(
        "No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# print(f"OpenAI API Key: {api_key}")
client = OpenAI(api_key=api_key)


class Service:
    def __init__(self):
        pass

    async def generate_report(request_body: GenerateReportRequest):
        try:
            country = request_body.country
            project_category = request_body.category
            budget = request_body.project_budget
            description = request_body.description
            language = request_body.language
            prompt = f"""
You are an expert business consultant with deep experience in startup validation, risk assessment, and market feasibility analysis across various industries and global regions.

Your task is to evaluate the feasibility of a proposed project based on the following inputs:

- **Project Category**: {project_category}
- **Country**: {country}
- **Available Budget in $**: ${budget:,.2f}
- **Project Description**: "{description}"


Provide your analysis in the exact format below. Use only plain text. Do not use markdown or code blocks.

### Analyse marché
[Insert a concise market insight about demand, competition, or local trends in {country} for {project_category}. Include 1–2 key risks.]

### Stratégie marketing
[Insert 3 bullet points of actionable marketing strategies. Each point should start with a relevant emoji: 🔍, 🤝, 📱, 🎯, or 💡. Keep each item short and practical.]

### Décisions timatif (6 months)
[Insert a numbered list of 3 concrete, time-bound actions to take in the first 6 months. Be specific about locations, budgets, or steps.]

Respond in {language}. Use clear, professional language suitable for a business decision-maker.
The answer must be in JSON format without any additional commentary or text:
"""
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
            )
            print(f"OpenAI response: {response.choices[0].message.content}")
            json_content = json.loads(response.choices[0].message.content)
            return json_content
        except Exception as e:
            logger.error(f"Error in generate_report: {e}")
            raise HTTPException(status_code=500, detail=str(e))
