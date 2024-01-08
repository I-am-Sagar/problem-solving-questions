import json
import openai
import os


# STEP 1: SETUP THE OPENAI API KEY
with open('key.json', 'r') as key:
    data = json.load(key)
api_key = data['main']
openai.api_key = api_key

# STEP 2: FUNCTION TO CALL GPT
def chatgpt(role, question):
    messages = [
        { 'role': 'system', 'content': role},
        { 'role': 'user', 'content': question}
    ]
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = messages
    )
    return str(response['choices'][0]['message']['content'])

# STEP 3: GENERATE THE PROMPT & RESPONSE IN FILES

# Following code is specialized for Competitive Programming

role_file_path = './input/static/role.txt'
topic_tag_file_path = './input/static/topic_tag_req.txt'
problem_req_file_path = './input/static/problem_req.txt'
solution_req_file_path = './input/static/solution_req.txt'
theory_req_file_path = './input/static/theory_req.txt'

problem_file_path = './input/problem.txt'
solution_file_path = './input/solution.txt'

with open(role_file_path, 'r', encoding='utf-8') as role_file, \
     open(problem_file_path, 'r', encoding='utf-8') as problem_file, \
     open(solution_file_path, 'r', encoding='utf-8') as solution_file, \
     \
     open(topic_tag_file_path, 'r', encoding='utf-8') as topic_tag_file, \
     open(problem_req_file_path, 'r', encoding='utf-8') as problem_req_file, \
     open(solution_req_file_path, 'r', encoding='utf-8') as solution_req_file, \
     open(theory_req_file_path, 'r', encoding='utf-8') as theory_req_file:
    
    # a) Define the role first
    role = str(role_file.read())
    # print(role)

    # b) Build the context
    problem = str(problem_file.read())
    solution = str(solution_file.read())

    context = f'\n\n##\n\nProblem Statement:"""{problem}"""\n\n##\n\nSolution:"""{solution}"""\n\n'
    # print(context)

    # c) We need the topic tag and problem name, so that we can create the folder with that tag name
    #    and the files within the folder with that problem name. 
    topic = str(topic_tag_file.read())
    message = topic + context
    # print(message)
    
    topic_response = chatgpt(role, message)
    # print(topic_response)

    # Try to get the topic_tag and problem_name. 
    topic_tag, problem_name = None, None
    try:
        lines = topic_response.strip().split('\n')
        result_dict = {}
        for line in lines:
            try:
                key, value = map(str.strip, line.split(':'))
                result_dict[key] = value
            except ValueError as ve:
                print(f"Error: {ve}. Skipping line: {line}")

        topic_tag, problem_name = list(result_dict.values())
    except Exception as e:
        print(f"Error: {e}. Could not resolve topic tag and problem name.")
    print(topic_tag, problem_name)

    # Try to create a folder with topic_tag in the parent directory 
    # and create a folder within it with the problem name.
    try:
        current_dir = os.getcwd()  # current working directory
        parent_dir = os.path.dirname(current_dir)  # parent directory
        
        topic_folder_path = os.path.join(parent_dir, topic_tag)
        if not os.path.exists(topic_folder_path):
            # Create the topic folder because it doesn't exist
            os.makedirs(topic_folder_path)

        # Remove quotation marks, spaces, and other invalid foldername chars from problem_name
        problem_name = problem_name.replace(" ", "_").replace("\"", "").replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_").replace("<", "_").replace(">", "_").replace("|", "_")

        # Create a subfolder with the problem_name inside the topic folder
        problem_folder_path = os.path.join(topic_folder_path, problem_name)
        os.makedirs(problem_folder_path, exist_ok=True)
    except Exception as e:
        print(f'Error: {e}. Could not create folders with topic tag name or problem name.')

    # d) Get the improved/modified problem statement based on the context provided. 
    #    Put the contents within the problem file. 
    problem_req = str(problem_req_file.read())
    message = problem_req + context
    # print(message)
    
    problem_response = chatgpt(role, message)
    contents = f'### {problem_name}\n<hr>\n\n' + problem_response + '\n<hr>\n'

    file_path = os.path.join(problem_folder_path, f"{problem_name}.md")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(contents)
        print(f"File {problem_name}.md created successfully with contents.")
    except Exception as e:
        print(f"Error: {e}")

    # e) Get the beautified code in multiple possible langauges.
    solution_req = str(solution_req_file.read())
    message = solution_req + context
    # print(message)
    
    solution_response = chatgpt(role, message)
    contents = f'### {problem_name} - Solutions\n<hr>\n\n' + solution_response + '\n<hr>\n'

    file_path = os.path.join(problem_folder_path, "Solution.md")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(contents)
        print(f"File 'Solution.md' created successfully with contents.")
    except Exception as e:
        print(f"Error: {e}")
     
    # f) Get a theory dose on the problem asked.
    theory_req = str(theory_req_file.read())
    message = theory_req + context
    # print(message)
    
    theory_response = chatgpt(role, message)
    contents = f'### {problem_name} - Theory\n<hr>\n\n' + theory_response + '\n<hr>\n'

    file_path = os.path.join(problem_folder_path, "Theory.md")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(contents)
        print(f"File 'Theory.md' created successfully with contents.")
    except Exception as e:
        print(f"Error: {e}")
