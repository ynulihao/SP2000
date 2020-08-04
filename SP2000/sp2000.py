import requests
import json
import pandas as pd
import re
from xml.etree import ElementTree
import warnings


class SP2000:
    def __init__(self):
        self.key = None

    def set_search_key(self, key):
        """SP2000 API keys
        Apply for the apiKey variable to be used by all search_* functions,
        register for http://sp2000.org.cn/api/document and use an API key. This function allows users to set this key.
        :param key: Value to set apiKey(i.e. your API key).
        :return: None
        """
        self.key = key

        # checkAPI
        data = json.loads(requests.get('http://www.sp2000.org.cn/api/v2/getFamiliesByFamilyName',
                                       params={'familyName': 'Cyprinidae', 'apiKey': self.key,
                                               'page': 1}).text)
        assert data['code'] != 401, 'Please check your apiKey.'

    def search_family_id(self, *queries, start=1, limit=20):
        """Search family IDs
        Search family IDs via family name, supports Latin and Chinese names.
        :param queries:Family name, or part of family name, supports Latin and Chinese names. Single or more query.
        :param start:intenger Record number to start at. If omitted, the results are returned from the first record
            (start=1). Use in combination with limit to page through results. Note that we do the paging internally for
            you, but you can manually set the start parameter.
        :param limit: intenger Number of records to return. This is passed across all sources,when you first query,
            set the limit to something smallish so that you can get a result quickly, then do more as needed.
        :return:
        """
        assert self.key, 'You need to apply for the apiKey from http://sp2000.org.cn/api/document'
        fids = {}
        for query in queries:
            page_num = limit // 20
            fid_list = []

            for idx in range(page_num):
                data = json.loads(requests.get('http://www.sp2000.org.cn/api/v2/getFamiliesByFamilyName',
                                               params={'familyName': query, 'apiKey': self.key,
                                                       'page': start + idx}).text)
                for entry in data['data']['familes']:
                    fid_list.append(entry['record_id'])
            fids[query] = fid_list
        return fids

    def search_taxon_id(self, *queries, name='scientificName', start = 1, limit = 20):
        """Search taxon IDs
        Search taxon IDs via familyID ,scientificName and commonName.
        :param queries: familyID ,scientificName or commonName. Single or more query.
        :param name: stype should in ("familyID","scientificName","commonName"),the default value is "scientificName".
        :param start:intenger Record number to start at. If omitted, the results are returned from the first record
            (start=1). Use in combination with limit to page through results. Note that we do the paging internally for
            you, but you can manually set the start parameter.
        :param limit: intenger Number of records to return. This is passed across all sources,when you first query,
            set the limit to something smallish so that you can get a result quickly, then do more as needed.
        :return:
        """
        assert self.key, ' You need to apply for the apiKey from http://sp2000.org.cn/api/document'
        assert name in ['familyId', 'scientificName', 'commonName'],\
            'name should in ("familyID","scientificName","commonName"),the default value is "scientificName".'
        taxon_id = {}
        if name == 'familyId':
            for query in queries:
                page_num = limit // 20
                fid_list = []

                for idx in range(page_num):
                    data = json.loads(requests.get('http://www.sp2000.org.cn/api/v2/getSpeciesByFamilyId',
                                                   params={'familyId': query, 'apiKey': self.key,
                                                           'page': start + idx}).text)
                    if data['data']['species'] is None:
                        continue
                    for entry in data['data']['species']:
                        fid_list.append(entry['namecode'])
                taxon_id[query] = fid_list

        elif name == 'scientificName':
            for query in queries:
                page_num = limit // 20
                fid_list = []

                for idx in range(page_num):
                    data = json.loads(requests.get('http://www.sp2000.org.cn/api/v2/getSpeciesByScientificName',
                                                   params={'scientificName': query, 'apiKey': self.key,
                                                           'page': start + idx}).text)
                    if data['data']['species'] is None:
                        continue
                    for entry in data['data']['species']:
                        fid_list.append(entry['accepted_name_info']['namecode'])
                taxon_id[query] = fid_list

        elif name == 'commonName':
            for query in queries:
                page_num = limit // 20
                fid_list = []

                for idx in range(page_num):
                    data = json.loads(requests.get('http://www.sp2000.org.cn/api/v2/getSpeciesByCommonName',
                                                   params={'commonName': query, 'apiKey': self.key,
                                                           'page': start + idx}).text)
                    if data['data']['species'] is None:
                        continue
                    for entry in data['data']['species']:
                        fid_list.append(entry['accepted_name_info']['namecode'])
                taxon_id[query] = fid_list
        return taxon_id

    def search_checklist(self, *queries):
        """Search Catalogue of Life China checklist
        Get checklist via species or infraspecies ID.
        :param queries: single or more query
        :return:
        """
        assert self.key, ' You need to apply for the apiKey from http://sp2000.org.cn/api/document'
        checklist = {}
        for taxon_id in queries:
            data  = json.loads(requests.get('http://www.sp2000.org.cn/api/v2/getSpeciesByNameCode',
                                           params={'nameCode': taxon_id, 'apiKey': self.key}).text)['data']
            if data is None:
                continue

            checklist[taxon_id] = data
        return checklist

    @staticmethod
    def list_df(checklist):
        """Catalogue of Life China list(s) convert data frame(deprecated)
        Checklist lists convert data frame.
        :param checklist: return from search_checklist
        :return:
        """
        warnings.warn('this function is deprecated', DeprecationWarning)
        return pd.DataFrame(checklist)

    @staticmethod
    def find_synonyms(*queries):
        """Find synonyms via species name
        Find synonyms via species name from Catalogue of Life Global.
        :param queries: species name.single or more query.
        :return: set
        """

        synonyms = {}
        for query in queries:
            synonyms_set = set()
            query_no_space = re.sub(' ', '+', query)
            data = json.loads(requests.get(
                'http://webservice.catalogueoflife.org/col/webservice?name={}'
                '&format=json&response=full'.format(query_no_space)).text)['results']
            for entry in data:
                if entry['name'] == query:
                    status = entry['name_status']
                    if status == 'synonym':
                        synonyms_set.add(entry['accepted_name']['name'])
                    elif status == 'accepted name':
                        for synonym in entry['synonyms']:
                            synonyms_set.add(synonym['name'])
            synonyms[query] = synonyms_set
        return synonyms

    @staticmethod
    def get_col_taiwan(*queries, level='species', option='equal', include_synonyms=True):
        """Search Catalogue of Life Taiwan checklist
        Get Catalogue of Life Taiwan checklist via advanced query.
        :param queries: The string to search for. single or more query
        :param level: Query by category tree, tree should in ("kingdom","phylum","class","order","family","genus","name"),the default value is "name".
        :param option: Query format, option should in ("contain","equal","beginning"),the default value is "equal".
        :param include_synonyms: Whether the results contain a synonym or not.
        :return:
        """

        assert level in ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species'],\
            'level should in ("kingdom","phylum","class","order","family","genus","species")'
        assert option in ['contain', 'equal', 'begging'],\
            'option should in ("contain","equal","beginning"),the default value is "equal".'

        col_taiwan_dict = {}

        for query in queries:
            col_taiwan_list = []

            if include_synonyms:
                url = 'http://taibnet.sinica.edu.tw/eng/taibnet_xml.php?R1={tree}&D1=&' \
                      'D2={tree}&D3={option}&T1={query}+&T2=&id=y&sy=y'.format(tree=level, option=option, query=query)
            else:
                url = 'http://taibnet.sinica.edu.tw/eng/taibnet_xml.php?R1={tree}&D1=&' \
                      'D2={tree}&D3={option}&T1={query}+&T2=&id=y&sy='.format(tree=level, option=option, query=query)
            x = requests.get(url).text
            tree = ElementTree.fromstring(x)

            for i in tree:
                if i.tag == 'record':
                    col_dict = dict()
                    for element in i:
                        col_dict[element.tag] = element.text
                    col_taiwan_list.append(col_dict)
            col_taiwan_dict[query] = col_taiwan_list
        return col_taiwan_dict

    @staticmethod
    def get_redlist_china(query='', option='Scientific Names', group = 'Amphibians'):
        """Query Redlist of Chinese Biodiversity
        Query Redlist of China’s Biodiversity of Vertebrate, Higher Plants and Macrofungi.
        :param query: string The string to query for.
        :param option: character There is one required parameter, which is either Chinese Names or Scientific Names.
            Give eithera Chinese Names or Scientific Names. If an Scientific Names is given, the Chinese Names parameter
            may not be used. Only exact matches found the name given will be returned. option=c(“Chinese Names”,
            “Scientific Names”).
        :param group: character There is one required parameter, group=c(“Amphibians”,“Birds”,“Inland Fishes”,
            “Mammals”,“Reptiles”,“Plants”,“Fungi”).
        :return: pandas DataFrame
        """

        assert option in ['Chinese Names','Scientific Names'], \
            'option should in ("Chinese Names","Scientific Names"),the default value is "Scientific Names".'

        assert group in ["Amphibians","Birds","Inland Fishes","Mammals","Reptiles","Plants","Fungi", ""],\
            'taxon should in ("Amphibians","Birds","Inland Fishes","Mammals","Reptiles","Plants","Fungi", "")'

        try:
            excel = pd.read_excel(open('RedlistChina.xlsx', 'rb'))
        except FileNotFoundError:
            data = requests.get('https://files.ynulhcloud.cn/RedlistChina.xlsx').content
            with open('RedlistChina.xlsx', 'wb') as f:
                f.write(data)
            excel = pd.read_excel(open('RedlistChina.xlsx', 'rb'))

        if query and group:
            if option == 'Chinese Names':
                df = excel[excel['species_c'].notna()][excel[excel['species_c'].notna()]
                ['species_c'].str.contains(query, regex=False)]
                df = df[df['group'] == group]
            else:
                df = excel[excel['species'].notna()][excel[excel['species'].notna()]
                ['species'].str.contains(query, regex=False)]
                df = df[df['group'] == group]
        elif query:
            df = excel[excel['species'].notna()][excel[excel['species'].notna()]
                ['species'].str.contains(query, regex=False)]
        elif group:
            df = excel[excel['group'] == group]
        else:
            df = None
        return df

    @staticmethod
    def get_col_global(*queries, option='name', response='terse', start=0, limit = 500):
        """Search Catalogue of Life Global checklist
        Get Catalogue of Life Global checklist via species name and id.
        :param query: The string to search for.
        :param option: There is one required parameter, which is either name or id. Give eithera name or an ID.
        If an ID is given, the name parameter may not be used, and vice versa.
        option should in ("id","name"),the default value is "name".
        Only exact matches found the name given will be returned.
        :param response: Type of response returned. Valid values are response=terse and response=full.
        if the response parameter is omitted, the results are returned in the default terse format.
        If format=terse then a minimum set of results are returned (this is faster and smaller, enough for name lookup),
        if format=full then all available information is returned,
        response=c("full","terse"),the default value is "terse".
        :param start: The first record to return. If omitted, the results are returned from the first record (start=0).
        This is useful if the total number of results is larger than the maximum number of results returned by a single
        Web service query (currently the maximum number of results returned by a single query is 500 for terse queries
        and 50 for full queries,the default value is 0.
        :param limit: integer Number of records to return. This is useful if the total number of results is larger than
         the maximum number of results returned by a single Web service query (currently the maximum number of results
          returned by a single query is 500 for terse queries and 50 for full queries,the default value is 500.Note that
           there is a hard maximum of 10,000, which is calculated as the limit+start, so start=99,00 and limit=2000
            won’t work.
        :return:
        """
        assert option in ['name', 'id'], 'option should in (name, id).'
        assert response in ['terse', 'full'], 'response should in (terse, full).'
        result_dict = {}

        for query in queries:

            if option == 'name':
                query_no_space = re.sub(' ', '+', query)
                result = json.loads(requests.get('http://webservice.catalogueoflife.org/col/webservice?name={}'
                                   '&format=json&response={}&start={}'.format(query_no_space, response, start)).text)\
                    .get('results', None)
            else:
                result = json.loads(requests.get('http://webservice.catalogueoflife.org/col/webservice?id={}'
                                   '&format=json&response={}&start={}'.format(query, response, start)).text)\
                    .get('results', None)[:limit]
            result_dict[query] = result
        return result_dict


sp2000 = SP2000()
set_search_key = sp2000.set_search_key
search_family_id = sp2000.search_family_id
search_taxon_id = sp2000.search_taxon_id
search_checklist = sp2000.search_checklist
list_df = sp2000.list_df
find_synonyms = sp2000.find_synonyms
get_col_taiwan = sp2000.get_col_taiwan
get_redlist_china = sp2000.get_redlist_china
get_col_global = sp2000.get_col_global



if __name__ == '__main__':
    from pprint import pprint
    api_key = 'null'

    sp2000.set_search_key(api_key)

    # print(sp2000.search_taxon_id('1233542354', stype='family_id'))
    # print(sp2000.search_taxon_id('Uncia uncia', stype='scientific_name'))
    # print(sp2000.search_taxon_id('Uncia uncia', 'Anguilla marmorata', stype='scientific_name'))
    # print(sp2000.search_checklist('b8c6a086-3d28-4876-8e8a-ca96e667768d'))
    # print(sp2000.find_synonyms('Anguilla anguilla'))
    # print(sp2000.get_col_taiwan("Anguilla marmorata","Anguilla japonica","Anguilla bicolor","Anguilla nebulosa", "Anguilla luzonensis", tree="name", option="contain"))
    # print(sp2000.search_taxon_id('bf72e220caf04592a68c025fc5c2bfb7', stype='family_id'))
    #
    # r = sp2000.get_col_taiwan(query="Anguilla",tree="name",option = "contain")
    # pprint(sp2000.search_checklist('b8c6a086-3d28-4876-8e8a-ca96e667768d'))
    # print(len(sp2000.get_col_global("Platalea leucorodia", option="name")['Platalea leucorodia']))
    # print(sp2000.get_col_taiwan("Anguilla", "Anguilla"))
    # print(sp2000.get_col_global("Anguilla marmorata","Anguilla japonica",
    # "Anguilla bicolor","Anguilla nebulosa","Anguilla luzonensis",option="name"))
    # print(sp2000.search_taxon_id('Actinidia arg', name = 'scientific_name'))
    # print(sp2000.search_checklist('123', 'T20171000100267', '123124'))
    # print(sp2000.get_redlist_china(query= 'Anguilla', option = "ScientificName", group='Inland Fishes'))


