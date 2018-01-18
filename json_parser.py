#!/usr/bin/python
import json

class JsonParser(object):

    def __init__(self,query_strings):

        # initializing query string list
        self.saved_temp_dict = list()

    def json_parser(self,query_strings):
        for part in query_strings:
            item = part.split('|')
            if item:
                data = {}
                data["id"] = item[1]
                p_name = item[2].split('>')
                p_data = []
                for i in p_name:
                    p_data.append(i.lstrip('<'))
                data["name"] = {"first": p_data[0],"middle": p_data[1], "last": p_data[2]}
                data["dob"] = item[3]
                p_loc = item[4].split('>')
                p_data = []
                for i in p_loc:
                    p_data.append(i.lstrip('<'))
                data["location"] = {"name": p_data[0],"coords":{"long":p_data[1],"lat":p_data[2]}}
                data["imageId"] = item[5]

                self.saved_temp_dict.append(data)

            else:
                print part + " is not a valid query_strings!"

        #saving data in the file data.json
        with open('data.json', 'a+') as outfile:
            json.dump(self.saved_temp_dict, outfile)


    #printing result by file read
    def print_result(self):
        f = open("data.json","r")
        print(f.readline())

    #erase file data
    def erase_file_data(self):
        open('data.json', 'w').close()

    # calling all operation functions
    def do_op(self):
        self.erase_file_data()
        self.json_parser(query_strings)
        self.print_result()


if __name__ == '__main__':
    # create list of parse strings
    query_strings = ['new_profile|siret87324sd1232|<Aamir><Hussain><Khan>|14-03-1965|<Mumbai><<72.872075><19.075606>>|siret87324sd1232.jpg','new_profile|jkdfgkjie9ir9977|<Amit><><Singh>||<Delhi><<><>>|jkdfgkjie9ir9977.jpg','new_profile|3466edrwsrdfs234|<Rahul><><>|13-12-1993|<Bangalore><<><>>|']

    try:
        obj = JsonParser(query_strings=query_strings)
        obj.do_op()
    except Exception, e:
        print e.message
        print 'Exception in JsonParser.py'
