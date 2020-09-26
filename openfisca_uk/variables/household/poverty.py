from openfisca_core.model_api import *
from openfisca_uk.entities import *
import numpy as np


class in_poverty_bhc(Variable):
    value_type = bool
    entity = Household
    label = u"label"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return (
            household("equiv_household_net_income_bhc", period)
            < parameters(period).poverty.absolute_poverty
        )


class in_poverty_ahc(Variable):
    value_type = bool
    entity = Household
    label = u"label"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return (
            household("equiv_household_net_income_ahc", period)
            < parameters(period).poverty.absolute_poverty
        )