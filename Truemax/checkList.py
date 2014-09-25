from Truemax import checkTransforms
import Truemax.checkNaming as checkNaming
import Truemax.detectHistory as detectHistory
from hfFixShading import hfCheckShading
import sys


reload(checkNaming)
reload(checkTransforms)
reload(detectHistory)


def check_list():
    checklist = [
        {"status": checkNaming.name_compare(), "error": "Objects have incorrect naming"},
        {"status": checkTransforms.check_transforms(), "error": "Objects have non zero transforms!"},
        {"status": hfCheckShading() is False, "error": "Face assignment detected!"},
        {"status": detectHistory.detect_history(), "error": "Objects have construction history/face assignment"},
    ]

    errors = []
    for c in checklist:
        if c["status"] is False:
            errors.append(c["error"])


    if len(errors):
        return False, errors
    else:
        sys.stdout.write("Object(s) checked. All is well, yay!\n")
        return True, ["All Perfect"]