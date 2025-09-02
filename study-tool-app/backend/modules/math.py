def get_math_topics():
    return [
        {"topic": "Algebra", "resources": ["Algebra Basics", "Solving Equations", "Graphing Functions"]},
        {"topic": "Geometry", "resources": ["Triangles", "Circles", "Area and Volume"]},
        {"topic": "Calculus", "resources": ["Limits", "Derivatives", "Integrals"]},
        {"topic": "Statistics", "resources": ["Mean, Median, Mode", "Probability", "Distributions"]},
        {"topic": "Trigonometry", "resources": ["Sine, Cosine, Tangent", "Trigonometric Identities", "Applications"]},
    ]

def get_math_resources(topic):
    topics = get_math_topics()
    for t in topics:
        if t["topic"].lower() == topic.lower():
            return t["resources"]
    return None

def get_math_quiz():
    return [
        {"question": "What is the derivative of x^2?", "options": ["2x", "x^2", "2"], "answer": "2x"},
        {"question": "What is the area of a circle with radius r?", "options": ["πr^2", "2πr", "πd"], "answer": "πr^2"},
        {"question": "What is the value of sin(90°)?", "options": ["0", "1", "0.5"], "answer": "1"},
    ]