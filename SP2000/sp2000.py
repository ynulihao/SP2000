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

    def search_family_id(self, *queries):
        """Search family IDs
        Search family IDs via family name, supports Latin and Chinese names.
        :param queries:Family name, or part of family name, supports Latin and Chinese names. Single or more query.
        :return:
        """
        assert self.key, 'You need to apply for the apiKey from http://sp2000.org.cn/api/document'
        fids = {}
        for query in queries:
            fids[query] = json.loads(requests.get('http://www.sp2000.org.cn/api/family/familyName/familyID/{}/{}'
                .format(query, self.key)).text)['fids']
        return fids

    def search_taxon_id(self, *queries, stype='scientific_name'):
        """Search taxon IDs
        Search taxon IDs via familyID ,scientificName and commonName.
        :param queries: familyID ,scientificName or commonName. Single or more query.
        :param stype: stype should in ("familyID","scientificName","commonName"),the default value is "scientificName".
        :return:
        """
        assert self.key, ' You need to apply for the apiKey from http://sp2000.org.cn/api/document'
        assert stype in ['family_id', 'scientific_name', 'common_name'],\
            'stype should in ("familyID","scientificName","commonName"),the default value is "scientificName".'
        taxon_id = {}
        if stype == 'family_id':
            for fid in queries:
                taxon_id[fid] = json.loads(requests.get('http://www.sp2000.org.cn/api/taxon/familyID/taxonID/{}/{}'
                    .format(fid, self.key)).text)['taxonIDs']

        elif stype == 'scientific_name':
            for fid in queries:
                taxon_id[fid] = json.loads(requests.get('http://www.sp2000.org.cn/api/taxon/scientificName/taxonID/{}/{}'
                    .format(fid, self.key)).text)['taxonIDs']

        elif stype == 'common_name':
            for fid in queries:
                taxon_id[fid] = json.loads(requests.get('http://www.sp2000.org.cn/api/taxon/commonName/taxonID/{}/{}'
                    .format(fid, self.key)).text)['taxonIDs']
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
            checklist[taxon_id] = json.loads(requests.get(' http://www.sp2000.org.cn/api/taxon/species/taxonID/{}/{}'
                                    .format(taxon_id, self.key)).text)
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
    def get_col_taiwan(query, tree, option='equal', include_synonyms=True):
        """Search Catalogue of Life Taiwan checklist
        Get Catalogue of Life Taiwan checklist via advanced query.
        :param query: The string to search for.
        :param tree: Query by category tree, tree should in ("kingdom","phylum","class","order","family","genus","name"),the default value is "name".
        :param option: Query format, option should in ("contain","equal","beginning"),the default value is "equal".
        :param include_synonyms: Whether the results contain a synonym or not.
        :return:
        """

        assert tree in ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'name'],\
            'tree should in ("kingdom","phylum","class","order","family","genus","name")'
        assert option in ['contain', 'equal', 'begging'],\
            'option should in ("contain","equal","beginning"),the default value is "equal".'

        if include_synonyms:
            url = 'http://taibnet.sinica.edu.tw/eng/taibnet_xml.php?R1={tree}&D1=&' \
                  'D2={tree}&D3={option}&T1={query}+&T2=&id=y&sy=y'.format(tree=tree, option=option, query=query)
            pass
        else:
            url = 'http://taibnet.sinica.edu.tw/eng/taibnet_xml.php?R1={tree}&D1=&' \
                  'D2={tree}&D3={option}&T1={query}+&T2=&id=y&sy='.format(tree=tree, option=option, query=query)
        x = requests.get(url).text
        tree = ElementTree.fromstring(x)
        col_taiwan_list = []
        for i in tree:
            if i.tag == 'record':
                col_dict = dict()
                for element in i:
                    col_dict[element.tag] = element.text
                col_taiwan_list.append(col_dict)
        return col_taiwan_list

    @staticmethod
    def get_redlist_china():
        # todo
        pass

    @staticmethod
    def get_col_global(query, option='name', response='terse', start=0):
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
        :return:
        """
        assert option in ['name', 'id'], 'option should in (name, id).'
        assert response in ['terse', 'full'], 'response should in (terse, full).'

        if option == 'name':
            query_no_space = re.sub(' ', '+', query)
            result = json.loads(requests.get('http://webservice.catalogueoflife.org/col/webservice?name={}'
                               '&format=json&response={}&start={}'.format(query_no_space, response, start)).text)\
                .get('results', None)
        else:
            result = json.loads(requests.get('http://webservice.catalogueoflife.org/col/webservice?id={}'
                               '&format=json&response={}&start={}'.format(query, response, start)).text)\
                .get('results', None)
        return result


sp2000 = SP2000()


if __name__ == '__main__':
    api_key = 'You api key'

    sp2000.set_search_key(api_key)
    l = sp2000.search_family_id('Rosaceae', 'Cyprinidae')
    print(l)

    print(sp2000.search_taxon_id('1233542354', stype='family_id'))
    print(sp2000.search_taxon_id('Uncia uncia', stype='scientific_name'))
    print(sp2000.search_taxon_id('Uncia uncia', 'Anguilla marmorata', stype='scientific_name'))
    print(sp2000.search_checklist('b8c6a086-3d28-4876-8e8a-ca96e667768d'))
    d = sp2000.find_synonyms('Anguilla anguilla')
    print(d)
    print(sp2000.get_col_taiwan(query="Anguilla", tree="name", option="contain"))
    print(sp2000.search_taxon_id('bf72e220caf04592a68c025fc5c2bfb7', stype='family_id'))

    r = sp2000.get_col_taiwan(query="Anguilla",tree="name",option = "contain")
    print(r)
    print(len(r))

    c = sp2000.search_checklist('b8c6a086-3d28-4876-8e8a-ca96e667768d')
    print(sp2000.list_df(c))
    
    print(sp2000.get_col_global(query="Platalea leucorodia", option="name"))
