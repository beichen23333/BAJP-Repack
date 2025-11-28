from google import genai

client = genai.Client(api_key="AIzaSyBe2kqb8XmD3nMg2ER38n_aPoDaqtr079g")

response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="Explain how AI works in a few words"
)
print(response.text)
