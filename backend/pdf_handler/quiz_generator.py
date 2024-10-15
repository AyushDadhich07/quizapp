import groq

def generate_quiz(text_content, num_questions=5):
    client = groq.Groq()

    # Craft a prompt to generate a quiz
    prompt = f"""
    Generate {num_questions} multiple-choice questions from the following text, each with 4 answer options and a correct answer identified. Format the output as JSON.

    Text: {text_content}

    Output format:
    {{
      "questions": [
        {{
          "question": "Question text here",
          "options": ["Option A", "Option B", "Option C", "Option D"],
          "correct_answer": "Correct option here"
        }},
        ...
      ]
    }}
    """

    # Make API call to Groq for Llama 3.1
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",  # Groq's Llama model
        max_tokens=2048,
    )

    # Parse the response
    quiz_data = response.choices[0].message.content

    # TODO: Add error handling for invalid response or formatting issues
    return quiz_data

def chunk_text(text, chunk_size=1000):
    # Break text into manageable chunks
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
