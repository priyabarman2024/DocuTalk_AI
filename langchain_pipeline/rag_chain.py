from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import StrOutputParser

def load_rag_chain(llm):
    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful assistant. Use the following context to answer the question.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )
    
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        output_parser=StrOutputParser()  # Ensures clean string response
    )
    
    return chain
