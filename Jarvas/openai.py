import requests


url = "https://chat-gtp-free.p.rapidapi.com/v1/chat/completions"

payload = {
	"chatId": "92d97036-3e25-442b-9a25-096ab45b0525",
	"messages": [
		{
			"role": "system",
			"content": "You are a virtual assistant. Your name is Karen and you would like to be a firefighter."
		},
		{
			"role": "user",
			"content": "Hi, what's your name? What would you like to be when you grow up?"
		}
	]
}
headers = {
	"x-rapidapi-key": "f7eaba5953msh17aea7db0d26924p10a024jsn0a900b09ebd4",
	"x-rapidapi-host": "chat-gtp-free.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())


