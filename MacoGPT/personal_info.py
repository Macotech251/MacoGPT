
# ==========================================
# MACOGPT - EMMANUEL'S PERSONAL INFORMATION
# ==========================================

PERSONAL_INFO = {
    "name": "Emmanuel Nkemakolam",
    "nickname": "Maco-Tech",
    "creator_of": "MacoGPT",

    "about": """
    Emmanuel Nkemakolam is the creator of MacoGPT.
    He is interested in technology, artificial intelligence,
    digital creativity and entrepreneurship.
    """,

    "education": [
        "Michael Okpara University",
        "University of Nigeria"
    ],

    "skills": [
        "Graphic Design",
        "Video Editing",
        "Website Development",
        "Investment",
        "AI Automation",
        "Python Programming"
    ],

    "projects": [
        "MacoGPT - Personal AI Chatbot"
    ],

    "businesses": [
        "Maco-Tech"
    ],

    "achievements": [],

    "interests": [
        "Artificial Intelligence",
        "Technology",
        "Programming",
        "Digital Innovation",
        "Entrepreneurship"
    ],

    "goals": [
        "Build advanced AI systems",
        "Develop professional software",
        "Grow in technology and entrepreneurship"
    ]
}


def get_personal_information():
    """Convert Emmanuel's information into text for the AI."""
    information = []

    for section, details in PERSONAL_INFO.items():
        information.append(f"\n{section.upper()}:")

        if isinstance(details, list):
            for item in details:
                information.append(f"- {item}")
        else:
            information.append(str(details))

    return "\n".join(information)
