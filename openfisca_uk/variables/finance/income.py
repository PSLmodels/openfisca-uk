from openfisca_core.model_api import *
from openfisca_uk.entities import *
from openfisca_uk.tools.general import *

class sublet_income(Variable):
    value_type = float
    entity = Person
    label = u'Income received from sublet agreements'
    definition_period = YEAR

class base_net_income(Variable):
    value_type = float
    entity = Person
    label = u'Existing net income for the person to use as a base in microsimulation'
    definition_period = YEAR

class net_income(Variable):
    value_type = float
    entity = Person
    label = u'Net income for the person'
    definition_period = YEAR

    def formula(person, period, parameters):
        base = person("base_net_income", period)
        modelling = person("tax_modelling", period)
        return base + modelling