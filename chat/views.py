
from django.shortcuts import render
from django.http import JsonResponse
from .utils import load_qa_from_csv
import csv
import string

def normalize_question(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).strip()

qa_data = {}
#qa_data = load_qa_from_csv('questions_answers.csv')

# csv_file = 'questions_answers.csv'

# with open(csv_file, mode='r', encoding='utf-8-sig') as file:
#     reader = csv.DictReader(file)
#
#     # kontrollo headers
#     print("CSV Headers:", reader.fieldnames)
#
#     for row in reader:
#         question_key = row['question']
#         answer_key = row['answer']
#
#         if question_key and answer_key:
#             question = normalize_question(question_key)
#             answer = answer_key
#             qa_data[question] = answer
#         else:
#             print("Row is missing 'question' or 'answer' key:", row)
# Load initial data from a default CSV file
def load_initial_data():
    global qa_data
    qa_data = {}
    with open('questions_answers.csv', mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question = normalize_question(row['question'])
            answer = row['answer']
            qa_data[question] = answer

# Call the function to load initial data
load_initial_data()


def chatbot_view(request):
    if request.method == 'POST':
        user_question = normalize_question(request.POST.get('question'))
        print("Normalized User Question:", user_question)

        print(f"User question: '{user_question}'")
        if user_question in qa_data:
            print("Question found in dictionary.")
        else:
            print("Question not found in dictionary.")


        answer = qa_data.get(user_question, "I'm sorry, the question is not related with this course. Make sure you have uploaded the correct csv file. For Algorithms questions is questions_answers.csv. For fun is greetings.csv :)")

        print(f"Received answer: {answer}")
        return JsonResponse({'answer': answer})
    return render(request, 'chat/chatbot.html')
def upload_csv_view(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({'success': False, 'message': 'No file uploaded.'})

        file = request.FILES['file']
        try:
            decoded_file = file.read().decode('utf-8-sig').splitlines()
            reader = csv.DictReader(decoded_file)
            new_qa_data = {}
            for row in reader:
                question = normalize_question(row['question'])
                answer = row['answer']
                new_qa_data[question] = answer
            global qa_data
            qa_data = new_qa_data
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
