import requests

ENDPOINT = "https://www.demarches-simplifiees.fe/api/v2/graphql"
HEADERS = {'Authorization: Bearer <Token>'}

def fetch_data(query):
    response = request.post(
            ENDPOINT,
            json={"query": query},
            headers=HEADERS
            )
    response.raise_for_status()
    return reponse.json()

query = '''

'''
