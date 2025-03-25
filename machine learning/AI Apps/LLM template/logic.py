from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error
import torch

set_verbosity_error()

with open("formatted_prompt.txt", "r", encoding="utf-8") as file:
    guidelines = file.read()

MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"

def prompt_template(guidelines):
        template = PromptTemplate.from_template(
            "Provide practical advice (in Spanish language and wih around 400 tokens at most) for the following question, following the guidelines shown after the question\n\n"
            "User question: {question}\n\n"
            "Guidelines:"
            f"{guidelines}\n\n"
            "mark_model_answer:"
        )
        return template

def initialize_model1():  
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16,
            device_map="auto"
        )
     
        # Create a text generation pipeline
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=500,  # 1 token ≈ 0.75 words
            temperature=0.1,     # Lower = more deterministic, higher = more creative
            top_p=0.85,          # At each token, the model only considers the smallest set of tokens whose cumulative probability is at least 85%. So top_p=0.05 means that if the likely token is over 5% the model only take the likely token
            do_sample=True,      # activates random sampling during generation, meaning the model doesn't always choose the highest-probability token (which would be greedy decoding).
            repetition_penalty=1.2 #reduces the likelihood of generating tokens that have already been produced.
        )
        # Connect to LangChain
        llm1 = HuggingFacePipeline(pipeline=pipe)
        
        return llm1
    
    except Exception as e:
        print(f"Error initializing model1: {e}")
        
def get_answer_chain(template, llm):
        answer_chain = template | llm
        return answer_chain

def get_water_advice(question):
    template = prompt_template()
    llm1 = initialize_model1()
    answer_chain = get_answer_chain(template,llm1)

    try:
        # Generate the advice
        result = answer_chain.invoke({
            "question": question
        })
        
        # Clean up the result to extract just the advice
        if isinstance(result, str):
            answer_parts = result.split("mark_model_answer:")
            if len(answer_parts) > 1:
                only_answer = answer_parts[-1].strip()
                return only_answer
            return result.strip()
        return result
 
    except Exception as e:
        return f"Error generating water management advice: {e}."
