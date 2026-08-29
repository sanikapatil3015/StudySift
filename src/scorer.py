def calculate_score(
    word_count,
    sentence_count,
    paragraph_count,
    keyword_count
):
    """
    Calculate a basic document quality score
    between 0 and 100.
    """

    score = 0

    # --------------------------------
    # 1. Content Length
    # Maximum: 25 points
    # --------------------------------

    if word_count >= 100:
        score += 25

    elif word_count >= 50:
        score += 15

    elif word_count >= 20:
        score += 10

    # --------------------------------
    # 2. Sentence Structure
    # Maximum: 25 points
    # --------------------------------

    if sentence_count >= 5:
        score += 25

    elif sentence_count >= 3:
        score += 15

    elif sentence_count >= 1:
        score += 10

    # --------------------------------
    # 3. Paragraph Structure
    # Maximum: 25 points
    # --------------------------------

    if paragraph_count >= 3:
        score += 25

    elif paragraph_count >= 2:
        score += 15

    elif paragraph_count >= 1:
        score += 10

    # --------------------------------
    # 4. Keyword Diversity
    # Maximum: 25 points
    # --------------------------------

    if keyword_count >= 8:
        score += 25

    elif keyword_count >= 5:
        score += 15

    elif keyword_count >= 2:
        score += 10

    # Make sure score never goes above 100
    return min(score, 100)