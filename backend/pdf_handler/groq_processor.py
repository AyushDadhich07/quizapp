import groq

def process_pdf_content(text_content):
    client = groq.Groq()

    # Process the text content and ignore irrelevant content using Groq API
    prompt = f"""
    Analyze the following text extracted from a PDF and identify the main topics, key concepts, and important information. Ignore any irrelevant content or formatting issues.

    Text: {text_content}

    Output a summary of the main points in a structured format.
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",  # Groq's Llama model
        max_tokens=1000,
    )
    
    return response.choices[0].message.content
