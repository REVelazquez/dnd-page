from handlers_ability_scores import ability_scores_api
from handlers_alignments import alignments_api
from handlers_classes import classes_api
from handlers_conditions import conditions_api
from handlers_proficiencies import proficiencies_api
from handlers_skills import skills_api
from handlers_spells import spells_api
from handlers_background import backgrounds_api
from handlers_damage_types import damage_types_api


if __name__ == '__main__':
    ability_scores_api()
    alignments_api()
    backgrounds_api()
    classes_api()
    conditions_api()
    damage_types_api()
    proficiencies_api()
    skills_api()
    spells_api()