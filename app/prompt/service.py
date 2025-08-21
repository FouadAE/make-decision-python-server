from openai import OpenAI
import os
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

    def generate_feasibility_prompt(request : GenerateReportRequest):
        try:
            country = request.country
            project_category = request.category
            budget = request.project_budget  # Assuming description contains budget info
            description = request.description
            prompt = f"""
You are an expert business consultant with deep experience in startup validation, risk assessment, and market feasibility analysis across various industries and global regions.

Your task is to evaluate the feasibility of a proposed project based on the following inputs:

- **Project Category**: {project_category}
- **Country**: {country}
- **Available Budget**: ${budget:,.2f}
- **Project Description**: "{description}"

Based on this information, provide a comprehensive analysis in the following structured format:

### 1. Feasibility Assessment
Provide a clear verdict: "Feasible", "Conditionally Feasible", or "Not Feasible".  
Justify your verdict with logical reasoning based on market conditions, typical costs in the {country} market, industry standards for {project_category}, and budget adequacy.

### 2. Key Risks
List the top 3–5 risks associated with this project in {country}, including but not limited to:
- Market demand
- Regulatory or legal challenges
- Operational difficulties
- Financial sustainability
- Competition

For each risk, briefly explain its potential impact and likelihood.

### 3. Recommendations
Provide 3–5 actionable recommendations to improve the chances of success. These may include:
- Budget allocation advice
- Market entry strategies
- Legal or licensing requirements in {country}
- Partnerships or hires
- Phased rollout plans

### 4. Estimated Break-Even Timeline (if applicable)
Based on typical performance in the {project_category} sector in {country}, estimate a realistic timeframe to break even (e.g., 12–18 months), or explain why break-even may not be achievable with the current budget.

Be realistic, data-informed, and avoid overly optimistic assumptions. Prioritize practicality and local market knowledge.

Respond in clear, professional English. Do not use markdown. Use headings exactly as above.
"""
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.0,  
                top_p=1.0,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Error in generate_cv: {e}")
            raise HTTPException(status_code=500, detail=str(e))
