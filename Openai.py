# from langchain_anthropic import ChatAnthropic

# model = ChatAnthropic(
#     model="claude-3-opus-20240229",
#     temperature=0.4,
#     api_key="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"

# )

# response = model.invoke("who is the best prime minister of pakistan?")

# print(response.content)

# from langchain_openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI(model='gpt-4',temperature=0.4)
# result=model("give me roadmap for learning GenAi")
# print(result)

# import google.generativeai as genai

# genai.configure(api_key="AIzaSyD9xNYDt43cE2CbT6XWtjK2vNX8V1dLvps")

# model = genai.GenerativeModel("gemini-2.5-flash")

# response = model.generate_content("who is best PM of Pakistan")

# print(response.text)

# from huggingface_hub import InferenceClient

# # REPLACE THIS with your NEW (private) Classic Read Token
# MY_TOKEN = "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" 

# # We use Llama-3-8B because it has the best "Serverless" availability
# model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

# client = InferenceClient(token=MY_TOKEN)

# try:
#     # Standard Chat Completion call
#     response = client.chat_completion(
#         model=model_id,
#         messages=[{"role": "user", "content": "What is the capital of India?"}],
#         max_tokens=50
#     )
    
#     # Extract and print the content
#     answer = response.choices[0].message.content
#     print(f"Success! Response: {answer}")

# except Exception as e:
#     print(f"Connection Error: {e}")
#     print("\nTroubleshooting Tip: If you see '403 Forbidden', ensure you are using a 'Classic Read' token, not a Fine-grained one.")
# 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
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# # 1. Setup the LLM Endpoint
# # Use 'huggingfacehub_api_token' instead of 'api_token'
# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
#     task="text-generation",
#     max_new_tokens=100,
#     do_sample=False,
#     huggingfacehub_api_token="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" # <--- Fix this name
# )

# # 2. Wrap it in the Chat Model interface
# model = ChatHuggingFace(llm=llm)

# # 3. Invoke

# result = model.invoke("What is the capital of India?")
# print(result.content)

# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# import os

# os.environ['HF_HOME'] = 'D:/huggingface_cache'

# llm = HuggingFacePipeline.from_model_id(
#     model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     task='text-generation',
#     pipeline_kwargs=dict(
#         temperature=0.5,
#         max_new_tokens=100
#     )
# )
# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of India")

# print(result.content)