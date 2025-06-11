from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Practice 1
# load_dotenv()
# Api_Key = os.getenv("Api_Key")

# # Check if the API key is present; if not, raise an error
# if not Api_Key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# #Reference: https://ai.google.dev/gemini-api/docs/openai
# external_client = AsyncOpenAI(
#     api_key=Api_Key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )
     

# agent = Agent(
#     name = "Translator",
#     instructions = "You are a helpful translator. Always translate urdu sentences into clear and simple english"
# )

# response =  Runner.run_sync(
#     agent,
#     input = "میں روز صبح جلدی اٹھتا ہوں۔پھر فجر کی نماز پڑھتا ہوں۔",
#     run_config = config
#     )

# print(response)


# Practice 2

# load_dotenv()
# Api_Key= os.getenv("Api_Key")

# # Check if the API key is present; if not, raise an error
# if not Api_Key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# #Reference: https://ai.google.dev/gemini-api/docs/openai
# external_client = AsyncOpenAI(
#     api_key=Api_Key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# agent=Agent(
#     name = "Cooker",
#     instructions = "You will help people to tell recipe of food"
# )

# result = Runner.run_sync(
#     agent,
#     input = "Tell me the recipe of french toast",
#     run_config = config

# )
# print(result)

# practice 3

# load_dotenv()
# Api_Key = os.getenv("Api_Key")

# # Check if the API key is present; if not, raise an error
# if not Api_Key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# #Reference: https://ai.google.dev/gemini-api/docs/openai
# external_client = AsyncOpenAI(
#     api_key=Api_Key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# agent = Agent(
#     name = "Teacher",
#     instructions= "You will help student to solve inquiries"
# )

# Response = Runner.run_sync(
#     agent,
#     input = "Definition of Newton's second law of motion with example.",
#     run_config= config 
# )
# print(Response)

# Practice 4

load_dotenv()
Api_Key = os.getenv("Api_Key")

# Check if the API key is present; if not, raise an error
if not Api_Key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=Api_Key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name = "Assistant",
    instructions= "You will help developer to help coding"
)

response = Runner.run_sync(
    agent,
    input = "solve this error in code ," 
    "number = 5, text = apples ,print(number + text)",
    run_config= config
      )
print(response)
