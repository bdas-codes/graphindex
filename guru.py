import requests


class Guru:
    def __init__(self, endpoint: str = 'https://query.wikidata.org/sparql'):
        self.endpoint = endpoint

    def ask(self, question: str):
        sparql = ''
        if ' old ' in question:
            person_name = question.split("how old is ")[1]
            sparql = """
                        SELECT ?ageLabel
                        WHERE {
                                  ?person wdt:P569 ?birthdate.
                                  ?person rdfs:label "%s"@en.
                                  BIND(YEAR(NOW()) - YEAR(?birthdate) AS ?age)
                                  BIND(CONCAT(?age, " years old") AS ?ageLabel)
                                  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
                                } LIMIT 1""" % person_name
        elif ' population ' in question:
            city_name = question.split("what is the population of ")[1]
            sparql = """
                        SELECT ?populationLabel
                        WHERE {
                          ?city wdt:P31 wd:Q515;
                            rdfs:label "%s"@en;
                            wdt:P1082 ?population.
                          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
                        } LIMIT 1""" % city_name

        # Prepare the request headers and parameters
        headers = {'Accept': 'application/sparql-results+json'}
        params = {'query': sparql}

        # Send the HTTP GET request to the SPARQL endpoint
        response = requests.get(self.endpoint, headers=headers, params=params)
        # import pdb; pdb.set_trace()
        # Parse the response and extract the answer if available
        if response.status_code == 200:
            data = response.json()
            bindings = data.get('results', {}).get('bindings', [])
            heads = data.get('head', {}).get('vars')
            if bindings:
                answer = bindings[0].get(heads[0], {}).get('value')
                return answer

        # Return None if no answer is found or there's an error
        return None


# if __name__ == '__main__':
#     gu = Guru()
#     gu.ask('how old is Trump')
#     gu.ask('what is the population of New York City')
