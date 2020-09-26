from openfisca_core.model_api import *
from openfisca_uk.entities import *
import numpy as np


class council_tax(Variable):
    value_type = float
    entity = Household
    label = u"label"
    definition_period = ETERNITY


class housing_cost(Variable):
    value_type = float
    entity = Household
    label = u"label"
    definition_period = ETERNITY


class household_net_income_bhc(Variable):
    value_type = float
    entity = Household
    label = u"label"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return household.sum(
            household.members("net_income", period)
        ) - household("council_tax", period)


class equiv_household_net_income_bhc(Variable):
    value_type = float
    entity = Household
    label = u"label"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return household("household_net_income_bhc", period) / household(
            "household_equivalisation", period
        )


class household_net_income_ahc(Variable):
    value_type = float
    entity = Household
    label = u"label"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return (
            household.sum(household.members("net_income", period))
            - household("council_tax", period)
            - household("housing_cost", period)
        )


class equiv_household_net_income_ahc(Variable):
    value_type = float
    entity = Household
    label = u"label"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return household("household_net_income_ahc", period) / household(
            "household_equivalisation", period
        )