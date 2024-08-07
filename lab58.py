import html
import random

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
question = html.unescape(trivia["question"])
correct_answer = html.unescape(trivia["correct_answer"])
incorrect_answers = [html.unescape(answer) for answer in trivia["incorrect_answers"]]

answers= incorrect_answers+[correct_answer]
random.shuffle(answers)

answer_options = ['A', 'B', 'C', 'D']
answer_dict = dict(zip(answer_options, answers))

print(f"Category: {trivia['category']}")
print(f"Question: {question}\n")

for option in answer_options:
    print(f"{option}: {answer_dict[option]}")

user_answer = input("\nYour answer (A,B,C, or D): ").strip().upper()

if answer_dict.get(user_answer) == correct_answer:
    print("Correct")
else:
    print("Incorrect. The correct answer is:", correct_answer)
