from openfisca_core.model_api import *
from openfisca_uk.entities import *
from openfisca_uk.tools.general import *


class benefit_cap(Variable):
    value_type = float
    entity = BenUnit
    label = u"Benefit cap for the family"
    definition_period = WEEK

    def formula(benunit, period, parameters):
        children = benunit("num_children", period.this_year) > 0
        region = benunit.value_from_first_person(
            benunit.members.household("region")
        )
        regions = benunit.members.household("region").possible_values
        in_london = region == regions.LONDON
        cap = parameters(period).benefit.benefit_cap
        rate = select(
            [
                children * in_london,
                children * not_(in_london),
                not_(children) * in_london,
                not_(children) * not_(in_london),
            ],
            [
                cap.london_children,
                cap.has_children,
                cap.london_no_children,
                cap.no_children,
            ],
        )
        exempt = benunit("is_benefit_cap_exempt", period.this_month)
        cap = where(exempt, np.inf * np.ones_like(children), rate)
        return cap


class is_benefit_cap_exempt(Variable):
    value_type = bool
    entity = BenUnit
    label = u"Whether exempt from the benefits cap"
    definition_period = MONTH

    def formula(benunit, period, parameters):
        QUAL_PERSONAL_BENEFITS = [
            "carers_allowance",
            "DLA_SC",
            "DLA_M",
            "ESA_contrib",
        ]
        qualifying = (
            add(benunit, period, ["working_tax_credit"], options=[DIVIDE])
            + add(benunit, period, ["ESA_income"], options=[ADD])
            + aggr(benunit, period, QUAL_PERSONAL_BENEFITS, options=[ADD])
            > 0
        )
        return qualifying
