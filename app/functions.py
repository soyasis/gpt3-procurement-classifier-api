import openai


def get_categories(text_query):
    
    restart_sequence = "\n"

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"The following is a list of queries and the categories they fall into.\n\nExample of possible categories:\n\"Cleaning\", \"Hotel & catering supplies\", \"Shipping, packaging\", \"Building services engineering\", \"Medical, therapy, laboratory supplies\", \"Industrial\", \"Occupational safety\", \"Office & warehouse equipment\", \"Electronics\", \"Professional Tools\", \"Computers & accessories\", \"Stationery\"\n\nquery: I need a cleaning trolley\ncategories: Cleaning, Household, Industrial\n\nquery: I need office tables\ncategories: Office & warehouse equipment, Furniture\n\nquery: I need ink for the printer\ncategories: Computers & accessories, Stationary\n\nquery: I need cooking utensils\ncategories: Hotel & catering supplies, Kitchen\n\nquery: I need a new computer\ncategories: Computers & accessories, Electronics\n\nquery: {text_query}\ncategories:",
    temperature=0.19,
    max_tokens=31,
    top_p=1,
    best_of=3,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
    )
    return [response['choices'][0]['text']]