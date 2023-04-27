import json
import xml.etree.ElementTree as ET


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def get_xml_text(self, data):
        for key, value in self.__dict__.items():
            ET.SubElement(data, key).text = str(value)

    def convert_to_xml(self):
        human_data = ET.Element('Human')
        self.get_xml_text(human_data)
        return ET.tostring(human_data, encoding='utf8').decode('utf8')

    @classmethod
    def convert_to_json_or_xml(cls, command, *args):
        human = cls(*args)
        if command == 'json':
            json_data = human.convert_to_json()
            print(json_data)
            with open('human.json', 'w') as file:
                file.write(json_data)
        elif command == 'xml':
            xml_data = human.convert_to_xml()
            print(xml_data)
            with open('human.xml', 'w') as file:
                file.write(xml_data)
        else:
            print(f'Invalid command: {command}. Please enter "json" or "xml".')


if __name__ == '__main__':
    Human.convert_to_json_or_xml('json', 'Alex', 76, 'female', 1956)
    Human.convert_to_json_or_xml('xml', 'Victor', 18, 'male', 1999)