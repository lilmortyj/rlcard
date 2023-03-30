''' Register rule-based models or pre-trianed models
'''
from rlcard.models.registration import register, load

register(
    model_id = 'leduc-holdem-cfr',
    entry_point='rlcard.models.pretrained_models:LeducHoldemCFRModel')

register(
    model_id = 'leduc-holdem-rule-v1',
    entry_point='rlcard.models.leducholdem_rule_models:LeducHoldemRuleModelV1')

register(
    model_id = 'leduc-holdem-rule-v2',
    entry_point='rlcard.models.leducholdem_rule_models:LeducHoldemRuleModelV2')

register(
    model_id = 'bigleduc-holdem-cfr',
    entry_point='rlcard.models.pretrained_models:BigleducHoldemCFRModel')

register(
    model_id = 'bigleduc-holdem-rule-v1',
    entry_point='rlcard.models.bigleducholdem_rule_models:BigleducHoldemRuleModelV1')

register(
    model_id = 'bigleduc-holdem-rule-v2',
    entry_point='rlcard.models.bigleducholdem_rule_models:BigleducHoldemRuleModelV2')

register(
    model_id = 'bigleduc-holdem-rule-v3',
    entry_point='rlcard.models.bigleducholdem_rule_models:BigleducHoldemRuleModelV3')

register(
    model_id = 'bigleduc-holdem-rule-v4',
    entry_point='rlcard.models.bigleducholdem_rule_models:BigleducHoldemRuleModelV4')

register(
    model_id = 'bigleduc-holdem-rule-v5',
    entry_point='rlcard.models.bigleducholdem_rule_models:BigleducHoldemRuleModelV5')

register(
    model_id = 'bigleduc-holdem-rule-v6',
    entry_point='rlcard.models.bigleducholdem_rule_models:BigleducHoldemRuleModelV6')

register(
    model_id = 'uno-rule-v1',
    entry_point='rlcard.models.uno_rule_models:UNORuleModelV1')

register(
    model_id = 'limit-holdem-rule-v1',
    entry_point='rlcard.models.limitholdem_rule_models:LimitholdemRuleModelV1')

register(
    model_id = 'doudizhu-rule-v1',
    entry_point='rlcard.models.doudizhu_rule_models:DouDizhuRuleModelV1')

register(
    model_id='gin-rummy-novice-rule',
    entry_point='rlcard.models.gin_rummy_rule_models:GinRummyNoviceRuleModel')
