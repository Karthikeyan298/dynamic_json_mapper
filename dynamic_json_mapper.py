class DynamicJsonMapper:

    def __get_data(self, mapping_json, data_json, string, data_identifier):
        data = None
        for key in mapping_json:
            if type(mapping_json) == list and len(mapping_json) > 0:
                index = 0
                for item in mapping_json:
                    if type(item) != dict:
                        if item != data_identifier:
                            index += 1
                        else:
                            break

                if type(data_json[index]) == dict:
                    data = self.__get_data(mapping_json[index], data_json[index], string,
                                           data_identifier)
                else:
                    data = data_json[index]
            elif mapping_json[key] == data_identifier:
                data = data_json[key.replace(string, "")]
            elif type(mapping_json[key]) == dict or type(mapping_json[key]) == list:
                data = self.__get_data(mapping_json[key], data_json[key.replace(string, "")], string,
                                       data_identifier)
            else:
                continue
        return data

    def map_json(self, mapping_json, data_json, dst_identifier, src_identifier, data_identifier):

        _json = {}
        for key in mapping_json:
            if dst_identifier in key:
                _json[key.replace(dst_identifier, "")] = {} if type(mapping_json[key]) == dict else []
                _json[key.replace(dst_identifier, "")] = self.map_json(mapping_json[key], data_json, dst_identifier,
                                                                       src_identifier, data_identifier)
            elif src_identifier in key:
                return self.__get_data(mapping_json, data_json, src_identifier, data_identifier)
        return _json
