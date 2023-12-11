import requests
from bs4 import BeautifulSoup
import json

# Replace with the actual URL you intend to scrape
URL = 'https://www.geeksforgeeks.org/some-page-with-code-snippets/'
HEADERS = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

# List to store the extracted code snippets
code_snippets = []

try:
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    
    # If the request is successful
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # We need to know the structure of the page and what you're looking for. This is just an example.
    # Find all code elements (this would depend on the actual structure of the GeeksForGeeks page)
    code_elements = soup.find_all('code')
    
    for code_element in code_elements:
        # Again, this would depend on how the page is structured and might require more complex parsing.
        description = code_element.get_text(strip=True)
        code_snippet = code_element.find_next_sibling(text=True)
        
        # Append to the list as a dictionary
        code_snippets.append({
            "description": description,
            "code": code_snippet.strip(),
            "tags": ["python", "example"]  # You would dynamically generate tags based on the content
        })
        
    # Convert the list to JSON
    json_object = json.dumps(code_snippets, indent=4)
    
    # Print or write the json to a file
    print(json_object)

except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'An error occurred: {err}')
