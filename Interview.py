import tkinter as tk

# Questions dictionary
questions = {
    "Python": ["What is Python?", "Explain list comprehension."],
    "C++": ["What is a pointer?", "Explain OOP in C++."],
    "React": ["What is JSX?", "Explain props and state."]
}

# Keywords for simple evaluation
answers_keywords = {
    "Python": ["interpreted", "dynamic", "list comprehension"],
    "C++": ["memory", "object", "class", "pointer"],
    "React": ["component", "props", "state", "jsx"]
}

current_question = 0
selected_lang = "Python"

def start_interview():
    global current_question
    current_question = 0
    question_label.config(text=questions[selected_lang][current_question])

def next_question():
    global current_question
    user_answer = answer_entry.get().lower()
    keywords = answers_keywords[selected_lang]
    
    # Simple scoring
    score = sum(1 for k in keywords if k.lower() in user_answer)
    feedback_label.config(text=f"Score for this answer: {score}")
    
    current_question += 1
    if current_question < len(questions[selected_lang]):
        question_label.config(text=questions[selected_lang][current_question])
    else:
        question_label.config(text="Interview Finished!")

root = tk.Tk()
root.title("AI Interviewer")

# Language Selection
selected_lang_var = tk.StringVar(value="Python")
langs = ["Python", "C++", "React"]
tk.OptionMenu(root, selected_lang_var, *langs).pack()

def set_lang():
    global selected_lang
    selected_lang = selected_lang_var.get()
    start_interview()

tk.Button(root, text="Start Interview", command=set_lang).pack()

question_label = tk.Label(root, text="")
question_label.pack()

answer_entry = tk.Entry(root, width=50)
answer_entry.pack()

tk.Button(root, text="Submit Answer", command=next_question).pack()

feedback_label = tk.Label(root, text="")
feedback_label.pack()

root.mainloop()