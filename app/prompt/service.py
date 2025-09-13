from openai import OpenAI
import os
import json
from asyncio.log import logger
from fastapi import HTTPException
from dotenv import load_dotenv
from app.prompt.schema import GenerateReportRequest
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

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

### Market analysis with key market_analysis
[Insert a concise market insight about demand, competition, or local trends in {country} for {project_category}. Include 1–2 key risks.]

### Marketing strategy with key marketing_strategy
[Insert 3 bullet points of actionable marketing strategies. Each point should start with a relevant emoji: 🔍, 🤝, 📱, 🎯, or 💡. Keep each item short and practical.]

### Timing decisions (6 months) with key timing_decisions
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

    async def generate_report_v2(request_body: GenerateReportRequest):
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
- The recommendations should be specific to the project and personalized based on the local context, available budget, and project description provided, avoiding any generic or general advice.
- Each recommendation should be concise and practical.
### 4. Estimated Break-Even Timeline (if applicable)
Based on typical performance in the {project_category} sector in {country}, estimate a realistic timeframe to break even (e.g., 12–18 months), or explain why break-even may not be achievable with the current budget.

Be realistic, data-informed, and avoid overly optimistic assumptions. Prioritize practicality and local market knowledge.

Respond in clear, professional {language}. Do not use markdown. Use headings exactly as above.
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
