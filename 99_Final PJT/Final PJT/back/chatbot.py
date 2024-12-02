# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )

# def chat_with_openai(user_input):
#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a capable movie recommender. User will tell you music genres that user likes. So you have to match music genres and movie genres. Then you have to recommend 3 or 4 movies similar with usre's music genre."
#             },
#             {
#                 "role": "user",
#                 "content": user_input
#             }
#         ],
#         temperature=0.7
#     )
#     return completion.choices[0].message.content

# def start_chatbot():
#     print("챗봇과 대화를 시작합니다. 종료하려면 'exit'를 입력하세요.")
#     while True:
#         user_input = input("사용자: ")
#         if user_input.lower() == 'exit':
#             print("대화를 종료합니다.")
#             break
#         response = chat_with_openai(user_input)
#         print(f"챗봇: {response}")

# if __name__ == "__main__":
#     start_chatbot()

import os
from openai import OpenAI
from dotenv import load_dotenv
import sqlite3

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_db_answer(question):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    # cursor.execute('SELECT answer FROM knowledge_base WHERE question LIKE ?', ('%' + question + '%',))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def chat_with_openai(user_input):
    db_answer = get_db_answer(user_input)
    if db_answer:
        return db_answer
    else:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a capable movie recommender. User will tell you music genres that user likes. So you have to match music genres and movie genres. Then you have to recommend 3 or 4 movies similar with usre's music genre. Also, you have to recommend movies what it is in db.sqlite3."},
                {"role": "user", "content": user_input}
            ]
        )
        return completion.choices[0].message.content

def start_chatbot():
    print("챗봇과 대화를 시작합니다. 종료하려면 'exit'를 입력하세요.")
    while True:
        user_input = input("사용자: ")
        if user_input.lower() == 'exit':
            print("대화를 종료합니다.")
            break
        response = chat_with_openai(user_input)
        print(f"챗봇: {response}")

if __name__ == "__main__":
    start_chatbot()