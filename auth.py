import lxml.etree
import lxml.builder
from configuration import *

# read user.config
path_config = r'{path}\user.config'


def setting_config():
    tree = lxml.etree.parse(path_config)

    user_settings = tree.find('.//userSettings')
    monosnap_props = tree.find('.//Monosnap.Properties.Monosnap')
    if monosnap_props:
        user_settings.remove(monosnap_props)

    E = lxml.builder.ElementMaker()
    value = E.value
    setting = E.setting
    token = ""

    user_data = E(
        'Monosnap.Properties.Monosnap',
        # setting(
        #     value('kvacdopil'), name="UserName", serializeAs="String"
        # ),
        setting(
            value(token), name="Token", serializeAs="String"
        ),
        # setting(
        #     value('test@mail.ru'), name="Email", serializeAs="String"
        # ),
        # setting(
        #     value('id'), name="UserId", serializeAs="String"
        # ),
    )
    # вставляем это в имеющийся xml
    user_settings = tree.find('.//userSettings')
    # вставляем внутрь на первое место (перед Properties.Settings)
    user_settings.insert(0, user_data)
    with open(path_config, 'wb') as f:
        f.write(lxml.etree.tostring(tree, pretty_print=True))
