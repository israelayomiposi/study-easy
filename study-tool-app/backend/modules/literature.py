def get_literature_topics():
    return [
        "Poetry",
        "Prose",
        "Drama",
        "Literary Devices",
        "Famous Authors",
        "Literary Analysis",
        "Genres",
        "Critical Theories"
    ]

def get_literature_resources():
    return {
        "Poetry": [
            {"title": "The Poetry Foundation", "url": "https://www.poetryfoundation.org/"},
            {"title": "Poets.org", "url": "https://poets.org/"}
        ],
        "Prose": [
            {"title": "Project Gutenberg", "url": "https://www.gutenberg.org/"},
            {"title": "Literary Hub", "url": "https://lithub.com/"}
        ],
        "Drama": [
            {"title": "National Theatre", "url": "https://www.nationaltheatre.org.uk/"},
            {"title": "American Theatre Magazine", "url": "https://www.americantheatre.org/"}
        ]
    }

def get_literature_quizzes():
    return [
        {"title": "Shakespeare Quiz", "url": "/quizzes/shakespeare"},
        {"title": "Famous Novels Quiz", "url": "/quizzes/novels"},
        {"title": "Poetry Terms Quiz", "url": "/quizzes/poetry-terms"}
    ]