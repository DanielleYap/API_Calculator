"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCqSGDEjYDRUWt8rQToDozG2oGgZ9gKZrk")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "I am going to give you various equations using the following functions: Add, Subtract, Multiply & Divide numbers, Evaluate expressions with Power, Trigonometry, Log and Exponent. Please provide the answer",
            ],
        },
        {
            "role": "model",
            "parts": [
                "I'm ready! Please provide the equations, and I'll do my best to solve them for you. Be sure to use clear and concise notation, and I'll be happy to calculate the results. \n\nFor example, you can write:\n\n* **Add:** 12 + 5\n* **Subtract:** 10 - 3\n* **Multiply:** 7 * 8\n* **Divide:** 20 / 4\n* **Power:** 3^2 (3 to the power of 2)\n* **Trigonometry:** sin(45 degrees)\n* **Log:** log10(100) (log base 10 of 100)\n* **Exponent:** e^2 (e to the power of 2)\n\nI'm excited to help you with your equations! 😊 \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "2+5-9+log(7)-3*e^5",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Here's how to break down the equation and find the answer:\n\n**1. Exponent:**\n\n* e^5 ≈ 148.41 (using a calculator to approximate e^5)\n\n**2. Multiplication:**\n\n* 3 * e^5 ≈ 3 * 148.41 ≈ 445.23\n\n**3. Logarithm:**\n\n* log(7) ≈ 0.845 (using a calculator to approximate the base-10 logarithm of 7)\n\n**4. Addition and Subtraction:**\n\n* 2 + 5 - 9 + 0.845 - 445.23 ≈ -446.54\n\n**Therefore, the approximate answer to the equation 2 + 5 - 9 + log(7) - 3 * e^5 is -446.54** \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "do not give a break down or any extra text, only the answer",
            ],
        },
        {
            "role": "model",
            "parts": [
                "-446.54 \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "3+5-9",
            ],
        },
        {
            "role": "model",
            "parts": [
                "-1 \n",
            ],
        },
        {
            "role": "user",
            "parts": [
                "e^(4)-6+8-(9-1)",
            ],
        },
        {
            "role": "model",
            "parts": [
                "48.59 \n",
            ],
        },
    ]
)


def send_input(equation):
    response = chat_session.send_message(equation)
    print(response.text)
    return response.text
