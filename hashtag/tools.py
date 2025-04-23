
def generate_hashtags(caption: str, image_description: str) -> list[str]:
    """
    Generates a list of relevant and popular hashtags based on the provided caption and image description.
    """

    keywords = set(caption.lower().split()) | set(image_description.lower().split())
    hashtags = [f"#{word.strip('#.,!')}" for word in keywords if word.isalpha()]

    return list(hashtags)[:10]
