from config.skills import SKILLS_DICT
from logger.logging_utils import start_timing, finish_timing


def clean_data(data):

    start = start_timing("CLEANING DATA")

    data = _clean_skills(data)

    finish_timing(start)

    return data


def _clean_skills(data):
    
    # Remove words that are likely not skills
    not_skills = ["go", "rest", "react", "less", "express", "assembly", "linear"]

    for index, row in data.iterrows():
        for word in not_skills:
            if word in row["Skills"]:
                row["Skills"].remove(word)

    # Standardize the skills spelling
    for index, row in data.iterrows():
        for skill in row["Skills"]:
            for conventional_skill, aliases in SKILLS_DICT.items():

                # Standardize the case based on the spelling in `SKILLS` variable
                if skill.lower() == conventional_skill.lower():
                    i = row["Skills"].index(skill)
                    row["Skills"][i] = conventional_skill
                
                # Use Alieses e.g. "GoLang" -> "Go"
                elif skill.lower() in [a.lower() for a in aliases]:
                    i = row["Skills"].index(skill)
                    row["Skills"][i] = conventional_skill

    # Remove dubplicates if any within one posting
    for index, row in data.iterrows():
        data.at[index, "Skills"] = list(set(row["Skills"])) # `set` removes duplicates and `list` converts it back to array

    return data