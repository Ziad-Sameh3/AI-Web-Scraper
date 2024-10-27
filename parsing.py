import os
import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="AIzaSyBfsAw8DzZftg02Cs8MEgTaLpz23O4NDvg")

# Define the generation configuration
generation_config = {
    "temperature": 1.0,
}

# Read system instructions from a file or define directly
instruction = (
    "You are tasked with extracting specific information from the following text content: {splited_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the model with system instructions
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    generation_config=generation_config,
    system_instruction=instruction,
)


# Function to send the prompt to the Gemini API and receive the response
def parse_content(splited_content, parse_description):
    # Format the instruction with the content
    formatted_instruction = instruction.format(splited_content=splited_content)

    try:
        # Use the model to generate a response
        response = model.generate_content(
            formatted_instruction + "\n" + parse_description
        )
        if response and response.candidates:
            generated_text = response.candidates[0].content.parts[0].text
            print("Generated Content:", generated_text)
            return generated_text
        else:
            return "Error: No valid response from the model"
    except Exception as e:
        return f"Error: {str(e)}"