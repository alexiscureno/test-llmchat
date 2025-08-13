import datetime
from pydantic_ai.agent import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

MODEL_LIST = {
	'Qwen3: 4b (Ollama)': OpenAIModel(
		model_name='qwen3:4b',
		provider=OpenAIProvider(base_url='http://localhost:11434/v1', api_key='ollama'),
	),
}

def init_agent():
    agent = Agent(
        model=MODEL_LIST['Qwen3: 4b (Ollama)'],
        system_prompt=['Reply in one sentence']
    )

    @agent.system_prompt
    def addtimestamp() -> str:
        return f'right now is {datetime.datetime.now()}'
    
    @agent.system_prompt
    def set_output_format() -> str:
        return 'Always Output in one sentence'
    
    return agent