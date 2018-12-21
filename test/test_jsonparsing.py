import pytest
import json
from botline import *
from jsonparsing import *

listLocale = '{"success":true,"data":["en","es"]}'
listSystems = '{"success":true,"data":["knave","maze_rats","mythic","osdw","perilous"]}'
listTables = '{"success":true,"data":["alignment.yml","armor.yml","background.yml","clothing.yml","dungeoneering_gear.yml","face.yml","general_gear_1.yml","general_gear_2.yml","hair.yml","helmet_and_shield.yml","misfortune.yml","pc.yml","physique.yml","skin.yml","speech.yml","vice.yml","virtue.yml"]}'

@pytest.mark.parametrize("jsonstring,length", [(listLocale,2), (listSystems,5), (listTables,17),]) 
def test_toTextList(jsonstring, length):
    data = json.loads(jsonstring)
    resultList = toTextList(data)

    assert isinstance(resultList, list) 
    assert len(resultList) == length

    for line in resultList:
        assert isinstance(line, botline)

