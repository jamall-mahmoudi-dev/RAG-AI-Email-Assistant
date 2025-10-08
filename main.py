from rag_pipeline import generate_response

if __name__ == "__main__":
    user_email = input("Paste email text here:\n")
    response = generate_response(user_email)
    print("\n--- AI Response ---\n")
    print(response)
