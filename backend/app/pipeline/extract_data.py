import spacy
from spacy.matcher import PhraseMatcher
from langdetect import detect
from deep_translator import GoogleTranslator

from config.skills import SKILLS_LIST, SKILLS_THAT_CONTAIN_OTHER_SKILLS
from logger.logging_utils import print_progress_bar, start_timing, finish_timing, log


def extract_data(data):

    data = _translate_descriptions(data)

    data = _extract_skills(data)

    return data


def _translate_descriptions(data):
     
    start = start_timing("TRANSLATING DESCRIPTIONS")
    translated_count = 0

    # Translate description for every posting that is not in English
    for index, row in data.iterrows():
        
        # Print progress info
        print_progress_bar(index+1, len(data))

        description = row["Description"]

        # Check the language is English and if not -> translate
        lang = detect(description)
        if lang != "en":

            translated_count += 1

            translated_description = ""

            chunk_size = 4999

            chunks = [description[i:i+chunk_size] for i in range(0, len(description), chunk_size)]
            
            for chunk in chunks:
                translated_description += GoogleTranslator(source="auto", target="en").translate(chunk)

            # Add results to the dataframe
            data.at[index, "Description"] = translated_description

    log(f"TRANSLATED: {translated_count} / {len(data)}")
    finish_timing(start, progress_bar=True)

    return data


def _extract_skills(data):

    start = start_timing("EXTRACTING SKILLS FROM DESCRIPTIONS")
    
    # Add new column
    if "Skills" in data.columns:
        data["Skills"] = None # reset skills if column already exists (in case the data is loaded from csv in development process)
    else:
        data.insert(7, "Skills", None)

    # Create and configure the phrase matcher
    nlp = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(
        nlp.vocab,
        attr="LOWER"
    )
    patterns = [
        nlp.make_doc(skill)
        for skill in SKILLS_LIST
    ]
    matcher.add(
        "SKILLS",
        patterns
    )

    # Extract skills for every posting
    for index, row in data.iterrows():
        
        # Print progress info
        print_progress_bar(index+1, len(data))

        description = row["Description"]
            
        # Convert description into spaCy doc
        doc = nlp(description)

        # Scan doc and find matches
        matches = matcher(doc)

        # Collect results
        found = set()
        for match_id, token_start, token_end in matches:

            # Check if this is a skill that may contain other skills in its name and handle it
            skill_text = doc[token_start:token_end].text.lower()
            if skill_text in SKILLS_THAT_CONTAIN_OTHER_SKILLS:
                suffixes = SKILLS_THAT_CONTAIN_OTHER_SKILLS[skill_text]

                if token_end < len(doc) and doc[token_end].text.lower() in suffixes:
                    continue # skip the skill name if it is a part of another skill name in this context

            # Add skill
            found.add(doc[token_start:token_end].text)

        # Add results to the dataframe
        data.at[index, "Skills"] = sorted(found)

    finish_timing(start, progress_bar=True)

    return data
