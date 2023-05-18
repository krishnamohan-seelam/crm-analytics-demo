from faker import Faker
from dataclasses import dataclass,field,asdict
from typing import List
import json

Faker.seed(42)
fake = Faker()




    
@dataclass
class Agent:

    name:str = field(default_factory=lambda : fake.bothify(text='Agent-#####'))
    


@dataclass
class PollingBooth:
    polling_agent:Agent
    polling_booth:str = field(default_factory=lambda : fake.bothify(text='PB-#####'))
    

@dataclass
class Constituency:
    
    polling_booths:List[PollingBooth]
    constituency_name:str = field(default_factory=lambda : fake.bothify(text='CNS-#####'))


def generate_data(no_of_booths=5):
    polling_booths = []
    for i in range(no_of_booths):
        agent =  Agent()
        polling_booth = PollingBooth(agent)
        polling_booths.append(polling_booth)
    cns = Constituency(polling_booths)
    return asdict(cns)

def create_json_file(data,file_path):
    with open(file_path, "w") as fp:
        json.dump(data,fp,indent=4)
    
def main():
    file_path ="constituency.json"
    constituency_data = generate_data()
    create_json_file(constituency_data,file_path)

if __name__ == "__main__" :
    main()
