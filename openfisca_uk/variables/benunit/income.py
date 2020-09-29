from openfisca_core.model_api import *
from openfisca_uk.entities import *
import numpy as np


class benefit_modelling(Variable):
    value_type = float
    entity = BenUnit
    label = "Difference between reported benefits and simulated benefits"
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        MODELLED_BENEFITS = [
            "child_benefit",
            "child_tax_credit",
            "working_tax_credit",
            "income_support",
            "JSA_contributory",
            "JSA_income"
        ]
        return sum(
            map(
                lambda benefit: benunit(benefit, period)
                - benunit(f"{benefit}_reported", period),
                MODELLED_BENEFITS,
            )
        )


class benunit_income(Variable):
    value_type = float
    entity = BenUnit
    label = "Earned income of the benefit unit"
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        return benunit.sum(benunit.members("income", period))

class benunit_pension_income(Variable):
    value_type = float
    entity = BenUnit
    label = u'Pension income of the benefit unit'
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        return benunit.sum(benunit.members("pension_income", period))

class benunit_earnings(Variable):
    value_type = float
    entity = BenUnit
    label = u'Earnings of the benefit unit'
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        return benunit.sum(benunit.members("earnings", period))


class benunit_post_tax_income(Variable):
    value_type = float
    entity = BenUnit
    label = "Post-tax income of the benefit unit"
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        return benunit.sum(benunit.members("post_tax_income", period))


class benunit_gross_income(Variable):
    value_type = float
    entity = BenUnit
    label = "Gross income of the benefit unit"
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        return benunit.sum(benunit.members("gross_income", period))


class benunit_net_income(Variable):
    value_type = float
    entity = BenUnit
    label = "Net income of the benefit unit"
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        return benunit.sum(benunit.members("net_income", period))


class equiv_benunit_net_income(Variable):
    value_type = float
    entity = BenUnit
    label = "Equivalised net income of the benefit unit"
    definition_period = ETERNITY

    def formula(benunit, period, parameters):
        return benunit("benunit_net_income", period) / benunit(
            "benunit_equivalisation"
        )
