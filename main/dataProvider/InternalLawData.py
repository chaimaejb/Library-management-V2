import json
from mappers.InternalLawMapper import InternalLawMapper
from model.InternalLaw import InternalLaw

class InternalLawData:

    FILE = "data/internalLaw.json"
    
    @staticmethod
    def save_rules(obj):
        data = InternalLawMapper.to_dict(obj)
        with open(InternalLawData.FILE, "w") as f:
            json.dump(data, f)
    @staticmethod
    def load_rules():
        try:
            with open(InternalLawData.FILE, "r") as f:
                data = json.load(f)
                return InternalLawMapper.from_dict(data) 
        except FileNotFoundError:
            return InternalLaw(None,None,None)
