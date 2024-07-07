import os

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser

from prompt_template import system_template_text, user_template_text
from output_parser_model import RedBookModel

def generate_redbook_scheme(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=RedBookModel)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })

    return result

if __name__ == '__main__':
    r = generate_redbook_scheme("langchain框架", os.getenv("OPENAI_API_KEY"))
    print(r)
