## SP2000 <img src="inst/figures/logo.png" align="right" width="140" />

This package programatically download catalogue of the Chinese known species of animals, plants, fungi and micro-organisms. There are __122280__ species & infraspecific taxa in [2020 Annual Checklist of Catalogue of Life China](http://sp2000.org.cn/2019), including __110231__ species and __12049__ infraspecific taxa.This package also supports access to catalogue of life global <http://catalogueoflife.org> and catalogue of life Taiwan <http://taibnet.sinica.edu.tw/home_eng.php?>.


## Overview 


[**Species 2000**](http://sp2000.org.cn) China node is a regional node of the international species 2000 project, proposed by the international species 2000 Secretariat in October 20, 2006, was officially launched in February 7, 2006. Chinese Academy of Sciences, biological diversity Committee (BC-CAS), together with its partners, to support and manage the construction of species 2000 China node. The main task of the species 2000 China node, according to the species 2000 standard data format, the classification information of the distribution in China of all species to finish and check, the establishment and maintenance of Chinese biological species list, to provide free services to users around the world.


## Installation

### Current official release:
```
pip install SP2000
```

## Usage

##### Note: You need to apply for the [*apiKey*](http://sp2000.org.cn/api/document) to run search_* functions of this package.

Import  the **SP2000** package
```python
from SP2000.sp2000 import sp2000
```
###### Search family IDs via family name, supports Latin and Chinese names
```python
sp2000.set_search_key("your apiKey")
sp2000.search_family_id("Cyprinidae")
```
```python
{'Rosaceae': ['F20171000000279']}
```
```python
sp2000.search_family_id('Rosaceae', 'Cyprinidae')
```
```python
{'Rosaceae': ['F20171000000279'], 'Cyprinidae': ['bf72e220caf04592a68c025fc5c2bfb7']} 
```
###### Search taxon IDs via familyID ,scientificName and commonName
```python
sp2000.search_taxon_id('F20171000000279', name='family_id')
```
```python
{'F20171000000279': ['T20171000054271', 'T20171000054269', 'T20171000054268', 'T20171000054267', 'T20171000054265', 'T20171000054263', 'T20171000054258', 'T20171000054253', 'T20171000054245', 'T20171000054243', 'T20171000054241', 'T20171000054237', 'T20171000054236', 'T20171000054232', 'T20171000054230', 'T20171000054224', 'T20171000054222', 'T20171000054221', 'T20171000054220', 'T20171000054219']}
```
```python
sp2000.search_taxon_id('Uncia uncia', 'Anguilla marmorata', name='scientific_name')
```
```python
{'Uncia uncia': ['b8c6a086-3d28-4876-8e8a-ca96e667768d'], 'Anguilla marmorata': ['e192fbc15df24049bcd0fd01d307affa']}
```
```python
sp2000.search_taxon_id('蚊', name='common_name')
```
```python
{'蚊': ['T20171000079490', 'T20171000073868', 'T20171000073868', 'T20171000064312', 'T20171000039615', 'c7b6a6fd-ccf5-4a00-a179-86c2542c73a4', '137450d2-e3a6-420b-a909-f21b65dd82bd', 'T2017100009286']}```
```
###### Download detailed lists via species or infraspecies ID
```python
sp2000.search_checklist('b8c6a086-3d28-4876-8e8a-ca96e667768d')
```
```python
{'b8c6a086-3d28-4876-8e8a-ca96e667768d': {'Synonyms': [{'synonym': 'Panthera uncia', 'refs': [{'[1]': 'Don E. Wilson and DeeAnn M. Reeder (eds.), 2005. Mammal Species of the World. Mammal Species of the World, 3rd edition, Baltimore:The Johns Hopkins University Press. '}]}, {'synonym': 'Felis uncia', 'refs': [{'[1]': 'Don E. Wilson and DeeAnn M. Reeder (eds.), 2005. Mammal Species of the World. Mammal Species of the World, 3rd edition, Baltimore:The Johns Hopkins University Press. '}]}], 'scientificName': 'Uncia uncia(Schreber,1775)', 'Refs': [{'[1]': 'WANG Sung WANG JiaJun and LUO YiNin, 1994. MAMMALIAN NAMES(LATIN, CHINESE AND ENGLISH). Beijing:Science Press. '}, {'[2]': 'WANG Sung, 1998. CHINA RED DATA BOOK OF ENDANGERED ANIMALES - MAMMALIA. Beijing, Hong Kong, New York:Science Press. '}, {'[3]': 'Don E. Wilson and DeeAnn M. Reeder (eds.), 2005. Mammal Species of the World. Mammal Species of the World, 3rd edition, Baltimore:The Johns Hopkins University Press. '}], 'Distribution': 'Shanxi, Gansu, Nei Mongol, Yunnan, Qinghai, Xizang, Sichuan, Xinjiang(四川省,新疆维吾尔自治区,内蒙古自治区,西藏自治区,甘肃省,云南省,山西省,青海省)', 'taxonTree': {'phylum': 'Chordata', 'genus': 'Uncia', 'species': 'uncia', 'infraspecies': '', 'family': 'Felidae', 'kingdom': 'Animalia', 'class': 'Mammalia', 'order': 'CARNIVORA'}, 'chineseName': '雪豹', 'CommonNames': ['草豹', '荷叶豹', 'Snow Leopard', '艾叶豹', '打马热(藏族)'], 'SpecialistInfo': [{'E-Mail': 'yangqs@ioz.ac.cn', 'Address': '1 Beichen West Road, Chaoyang District, Beijing 100101, P.R.China(北京市朝阳区北辰西路1号院5号 中国科学院动物研究所)', 'name': 'Yang Qi-Sen(杨奇森)', 'Institution': 'Institute of Zoology, Chinese Academy of Sciences(中国科学院动物研究所)'}]}}
```
###### Checklist lists convert data frame(this function is deprecated)
```python
c = sp2000.search_checklist('b8c6a086-3d28-4876-8e8a-ca96e667768d')
print(sp2000.list_df(c))
```
```python
                    b8c6a086-3d28-4876-8e8a-ca96e667768d
CommonNames     [草豹, 荷叶豹, Snow Leopard, 艾叶豹, 打马热(藏族)]
Distribution    Shanxi, Gansu, Nei Mongol, Yunnan, Qinghai, Xi...
Refs            [{'[1]': 'WANG Sung WANG JiaJun and LUO YiNin,...
SpecialistInfo  [{'E-Mail': 'yangqs@ioz.ac.cn', 'Address': '1 ...
Synonyms        [{'synonym': 'Panthera uncia', 'refs': [{'[1]'...
chineseName      雪豹
scientificName                         Uncia uncia(Schreber,1775)
taxonTree       {'phylum': 'Chordata', 'genus': 'Uncia', 'spec...
```

###### Get Catalogue of Life Global checklist via species name and id
```python
sp2000.get_col_global("Anguilla marmorata","Anguilla japonica","Anguilla bicolor","Anguilla nebulosa","Anguilla luzonensis",option="name")
```
```python
{'Anguilla marmorata': [{'id': '433e0a4fe332e565c1679fa149543d83', 'name': 'Anguilla marmorata', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=1275', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla marmorata</i> Quoy & Gaimard, 1824', 'url': 'http://www.catalogueoflife.org/col/details/species/id/433e0a4fe332e565c1679fa149543d83'}, {'id': '112e4021244116f929b8912bfc4a4c77', 'name': 'Anguilla marmorata', 'rank': 'Species', 'name_status': 'misapplied name', 'online_resource': '', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla marmorata</i>', 'url': 'http://www.catalogueoflife.org/col/details/species/id/94f902df44fd76bed84cdea361b24fd6/synonym/112e4021244116f929b8912bfc4a4c77', 'accepted_name': {'id': '94f902df44fd76bed84cdea361b24fd6', 'name': 'Anguilla bengalensis', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=1272', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla bengalensis</i> (Gray, 1831)', 'url': 'http://www.catalogueoflife.org/col/details/species/id/94f902df44fd76bed84cdea361b24fd6'}}], 'Anguilla japonica': [{'id': '82d254fc10ec94f0c028c5e57c433b28', 'name': 'Anguilla japonica', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=295', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla japonica</i> Temminck & Schlegel, 1846', 'url': 'http://www.catalogueoflife.org/col/details/species/id/82d254fc10ec94f0c028c5e57c433b28'}], 'Anguilla bicolor': [{'id': '678ebb7ac6b13bfb36576bf46ad7459c', 'name': 'Anguilla bicolor', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=1274', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla bicolor</i> McClelland, 1844', 'url': 'http://www.catalogueoflife.org/col/details/species/id/678ebb7ac6b13bfb36576bf46ad7459c'}, {'id': '80c2013bd23c23bc3e487cafbcc17e2c', 'name': 'Anguilla bicolor bicolor', 'rank': 'Infraspecies', 'name_status': 'synonym', 'online_resource': '', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla bicolor bicolor</i> McClelland, 1844', 'url': 'http://www.catalogueoflife.org/col/details/species/id/678ebb7ac6b13bfb36576bf46ad7459c/synonym/80c2013bd23c23bc3e487cafbcc17e2c', 'accepted_name': {'id': '678ebb7ac6b13bfb36576bf46ad7459c', 'name': 'Anguilla bicolor', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=1274', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla bicolor</i> McClelland, 1844', 'url': 'http://www.catalogueoflife.org/col/details/species/id/678ebb7ac6b13bfb36576bf46ad7459c'}}, {'id': 'cc1bd35e74a606f6f81f1a0ec7b123c0', 'name': 'Anguilla bicolor pacifica', 'rank': 'Infraspecies', 'name_status': 'synonym', 'online_resource': '', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla bicolor pacifica</i> Schmidt, 1928', 'url': 'http://www.catalogueoflife.org/col/details/species/id/678ebb7ac6b13bfb36576bf46ad7459c/synonym/cc1bd35e74a606f6f81f1a0ec7b123c0', 'accepted_name': {'id': '678ebb7ac6b13bfb36576bf46ad7459c', 'name': 'Anguilla bicolor', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=1274', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla bicolor</i> McClelland, 1844', 'url': 'http://www.catalogueoflife.org/col/details/species/id/678ebb7ac6b13bfb36576bf46ad7459c'}}], 'Anguilla nebulosa': [{'id': '8a83afeb81a10cf63568e6ce2b81e6a5', 'name': 'Anguilla nebulosa', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=11700', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla nebulosa</i> McClelland, 1844', 'url': 'http://www.catalogueoflife.org/col/details/species/id/8a83afeb81a10cf63568e6ce2b81e6a5'}, {'id': 'b5b5b241a07fdb6fb57af1146b2f2617', 'name': 'Anguilla nebulosa', 'rank': 'Species', 'name_status': 'misapplied name', 'online_resource': '', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla nebulosa</i>', 'url': 'http://www.catalogueoflife.org/col/details/species/id/a4217a19b0546b3ad9d708e24496dfac/synonym/b5b5b241a07fdb6fb57af1146b2f2617', 'accepted_name': {'id': 'a4217a19b0546b3ad9d708e24496dfac', 'name': 'Anguilla labiata', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=1273', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla labiata</i> (Peters, 1852)', 'url': 'http://www.catalogueoflife.org/col/details/species/id/a4217a19b0546b3ad9d708e24496dfac'}}, {'id': 'b8800cd7e1fdcf4d305633799e55730b', 'name': 'Anguilla nebulosa labiata', 'rank': 'Infraspecies', 'name_status': 'synonym', 'online_resource': '', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla nebulosa labiata</i> (Peters, 1852)', 'url': 'http://www.catalogueoflife.org/col/details/species/id/a4217a19b0546b3ad9d708e24496dfac/synonym/b8800cd7e1fdcf4d305633799e55730b', 'accepted_name': {'id': 'a4217a19b0546b3ad9d708e24496dfac', 'name': 'Anguilla labiata', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=1273', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla labiata</i> (Peters, 1852)', 'url': 'http://www.catalogueoflife.org/col/details/species/id/a4217a19b0546b3ad9d708e24496dfac'}}, {'id': '7453beda93c2dfe28bb01d7e8e8805e8', 'name': 'Anguilla nebulosa nebulosa', 'rank': 'Infraspecies', 'name_status': 'synonym', 'online_resource': '', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla nebulosa nebulosa</i> McClelland, 1844', 'url': 'http://www.catalogueoflife.org/col/details/species/id/8a83afeb81a10cf63568e6ce2b81e6a5/synonym/7453beda93c2dfe28bb01d7e8e8805e8', 'accepted_name': {'id': '8a83afeb81a10cf63568e6ce2b81e6a5', 'name': 'Anguilla nebulosa', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=11700', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla nebulosa</i> McClelland, 1844', 'url': 'http://www.catalogueoflife.org/col/details/species/id/8a83afeb81a10cf63568e6ce2b81e6a5'}}], 'Anguilla luzonensis': [{'id': '86d8e3f2eb7f6dabd7df18d77be70366', 'name': 'Anguilla luzonensis', 'rank': 'Species', 'name_status': 'accepted name', 'record_scrutiny_date': [], 'online_resource': 'http://www.fishbase.org/Summary/SpeciesSummary.php?ID=65262', 'is_extinct': 'false', 'source_database': 'FishBase', 'source_database_url': 'http://www.fishbase.org', 'bibliographic_citation': 'Froese R. & Pauly D. (eds). (2020). FishBase (version Feb 2018). In: Species 2000 & ITIS Catalogue of Life, 2020-04-16 Beta (Roskov Y.; Ower G.; Orrell T.; Nicolson D.; Bailly N.; Kirk P.M.; Bourgoin T.; DeWalt R.E.; Decock W.; Nieukerken E. van; Penev L.; eds.). Digital resource at www.catalogueoflife.org/col. Species 2000: Naturalis, Leiden, the Netherlands. ISSN 2405-8858.', 'name_html': '<i>Anguilla luzonensis</i> Watanabe, Aoyama & Tsukamoto, 2009', 'url': 'http://www.catalogueoflife.org/col/details/species/id/86d8e3f2eb7f6dabd7df18d77be70366'}]}
```

###### Find synonyms via species name from Catalogue of Life Global
```python
sp2000.find_synonyms("Anguilla anguilla")
```
```python
{'Anguilla anguilla': {'Anguilla nilotica', 'Anguilla microptera', 'Anguilla platycephala', 'Anguilla vulgaris fluviatilis', 'Anguilla altirostris', 'Anguilla melanochir', 'Anguilla septembrina', 'Muraena anguilla', 'Muraena oxyrhina', 'Anguilla marina', 'Anguilla mediorostris', 'Muraena platyrhina', 'Anguilla vulgaris', 'Leptocephalus brevirostris', 'Anguilla vulgaris platyura', 'Muraena anguilla marina', 'Anguilla aegyptiaca', 'Anguilla ancidda', 'Anguilla hibernica', 'Anguilla capitone', 'Anguilla anguillia', 'Anguilla kieneri', 'Anguilla latirostris', 'Angill angill', 'Anguilla eurystoma', 'Anguilla marginata', 'Anguilla savignyi', 'Muraena anguilla maculata', 'Anguilla acutirostris', 'Anguilla linnei', 'Anguilla morena', 'Anguilla cuvieri', 'Anguilla vulgaris ornithorhincha', 'Anguilla callensis', 'Anguilla cloacina', 'Anguilla oblongirostris', 'Anguilla anguillai', 'Anguilla platyrhynchus', 'Anguilla vulgaris lacustus', 'Anguilla vulgaris macrocephala', 'Anguilla anguilla macrocephala', 'Anguilla fluviatilis', 'Anguilla vulgaris marina', 'Anguilla brevirostris', 'Anguilla anguilla mucrocephala', 'Anguilla anguilla ornithorhyncha', 'Anguilla bibroni', 'Anguilla migratoria', 'Anguilla canariensis', 'Anguilla anguilla oxycephala'}}                         
```

###### Search Catalogue of Life Taiwan checklist
```python
sp2000.get_col_taiwan("Anguilla",level="species",option = "contain")
```
```python
[{'name_code': '380710', 'kingdom': 'Animalia', 'kingdom_c': '動物界', 'phylum': 'Chordata', 'phylum_c': '脊索動物門', 'class': 'Actinopterygii', 'class_c': '條鰭魚綱', 'order': 'Anguilliformes', 'order_c': '鰻形目', 'family': 'Anguillidae', 'family_c': '鰻鱺科', 'genus': 'Anguilla', 'genus_c': '鰻鱺屬', 'species': 'bicolor', 'infraspecies_marker': None, 'infraspecies': 'pacifica', 'infraspecies2_marker': None, 'infraspecies2': None, 'author': 'Schmidt, 1928', 'author2': None, 'common_name_c': '太平洋雙色鰻鱺;短鰭鰻;二色鰻', 'endemic': None, 'dataprovider': None}, {'name_code': '395489', 'kingdom': 'Animalia', 'kingdom_c': '動物界', 'phylum': 'Chordata', 'phylum_c': '脊索動物門', 'class': 'Actinopterygii', 'class_c': '條鰭魚綱', 'order': 'Anguilliformes', 'order_c': '鰻形目', 'family': 'Anguillidae', 'family_c': '鰻鱺科', 'genus': 'Anguilla', 'genus_c': '鰻鱺屬', 'species': 'celebesensis', 'infraspecies_marker': None, 'infraspecies': None, 'infraspecies2_marker': None, 'infraspecies2': None, 'author': 'Kaup, 1856', 'author2': None, 'common_name_c': '西里伯斯鰻鱺;西里伯斯鰻;鰻;黑鰻', 'endemic': None, 'dataprovider': None}, {'name_code': '380711', 'kingdom': 'Animalia', 'kingdom_c': '動物界', 'phylum': 'Chordata', 'phylum_c': '脊索動物門', 'class': 'Actinopterygii', 'class_c': '條鰭魚綱', 'order': 'Anguilliformes', 'order_c': '鰻形目', 'family': 'Anguillidae', 'family_c': '鰻鱺科', 'genus': 'Anguilla', 'genus_c': '鰻鱺屬', 'species': 'japonica', 'infraspecies_marker': None, 'infraspecies': None, 'infraspecies2_marker': None, 'infraspecies2': None, 'author': 'Temminck & Schlegel, 1846', 'author2': None, 'common_name_c': '日本鰻鱺;白鰻;日本鰻;正鰻;白鱔;鰻鱺;土鰻;淡水鰻', 'endemic': None, 'dataprovider': None}, {'name_code': '395491', 'kingdom': 'Animalia', 'kingdom_c': '動物界', 'phylum': 'Chordata', 'phylum_c': '脊索動物門', 'class': 'Actinopterygii', 'class_c': '條鰭魚綱', 'order': 'Anguilliformes', 'order_c': '鰻形目', 'family': 'Anguillidae', 'family_c': '鰻鱺科', 'genus': 'Anguilla', 'genus_c': '鰻鱺屬', 'species': 'luzonensis', 'infraspecies_marker': None, 'infraspecies': None, 'infraspecies2_marker': None, 'infraspecies2': None, 'author': 'Watanabe, Aoyama & Tsukamoto, 2009', 'author2': None, 'common_name_c': '呂宋鰻鱺;呂宋鰻;黃氏鱸鰻', 'endemic': None, 'dataprovider': None}, {'name_code': '380712', 'kingdom': 'Animalia', 'kingdom_c': '動物界', 'phylum': 'Chordata', 'phylum_c': '脊索動物門', 'class': 'Actinopterygii', 'class_c': '條鰭魚綱', 'order': 'Anguilliformes', 'order_c': '鰻形目', 'family': 'Anguillidae', 'family_c': '鰻鱺科', 'genus': 'Anguilla', 'genus_c': '鰻鱺屬', 'species': 'marmorata', 'infraspecies_marker': None, 'infraspecies': None, 'infraspecies2_marker': None, 'infraspecies2': None, 'author': 'Quoy & Gaimard, 1824', 'author2': None, 'common_name_c': '花鰻鱺;鱸鰻;花鰻;烏耳鰻;土龍;黑鰻', 'endemic': None, 'dataprovider': None}]
```

###### Query Redlist of Chinese Biodiversity
```python
sp2000.get_redlist_china(query= 'Anguilla', option = "Scientific Names", group='Inland Fishes')
```
```python
      family_c       family species_c  ... group_c     kingdom kingdom_c
11861      鳗鲡科  Anguillidae      日本鳗鲡  ...    内陆鱼类  Vertebrate     脊椎动物卷
11862      鳗鲡科  Anguillidae       花鳗鲡  ...    内陆鱼类  Vertebrate     脊椎动物卷
11863      鳗鲡科  Anguillidae      双色鳗鲡  ...    内陆鱼类  Vertebrate     脊椎动物卷
11864      鳗鲡科  Anguillidae      云纹鳗鲡  ...    内陆鱼类  Vertebrate     脊椎动物卷

[4 rows x 11 columns]
```
## Tips

You can use pprint to “pretty-print” arbitrary Python data structures
```python
pprint(sp2000.search_checklist('b8c6a086-3d28-4876-8e8a-ca96e667768d'))
```
```python
{'b8c6a086-3d28-4876-8e8a-ca96e667768d': {'CommonNames': ['草豹',
                                                          '荷叶豹',
                                                          'Snow Leopard',
                                                          '艾叶豹',
                                                          '打马热(藏族)'],
                                          'Distribution': 'Shanxi, Gansu, Nei '
                                                          'Mongol, Yunnan, '
                                                          'Qinghai, Xizang, '
                                                          'Sichuan, '
                                                          'Xinjiang(四川省,新疆维吾尔自治区,内蒙古自治区,西藏自治区,甘肃省,云南省,山西省,青海省)',
                                          'Refs': [{'[1]': 'WANG Sung WANG '
                                                           'JiaJun and LUO '
                                                           'YiNin, 1994. '
                                                           'MAMMALIAN '
                                                           'NAMES(LATIN, '
                                                           'CHINESE AND '
                                                           'ENGLISH). '
                                                           'Beijing:Science '
                                                           'Press. '},
                                                   {'[2]': 'WANG Sung, 1998. '
                                                           'CHINA RED DATA '
                                                           'BOOK OF ENDANGERED '
                                                           'ANIMALES - '
                                                           'MAMMALIA. Beijing, '
                                                           'Hong Kong, New '
                                                           'York:Science '
                                                           'Press. '},
                                                   {'[3]': 'Don E. Wilson and '
                                                           'DeeAnn M. Reeder '
                                                           '(eds.), 2005. '
                                                           'Mammal Species of '
                                                           'the World. Mammal '
                                                           'Species of the '
                                                           'World, 3rd '
                                                           'edition, '
                                                           'Baltimore:The '
                                                           'Johns Hopkins '
                                                           'University '
                                                           'Press. '}],
                                          'SpecialistInfo': [{'Address': '1 '
                                                                         'Beichen '
                                                                         'West '
                                                                         'Road, '
                                                                         'Chaoyang '
                                                                         'District, '
                                                                         'Beijing '
                                                                         '100101, '
                                                                         'P.R.China(北京市朝阳区北辰西路1号院5号 '
                                                                         '中国科学院动物研究所)',
                                                              'E-Mail': 'yangqs@ioz.ac.cn',
                                                              'Institution': 'Institute '
                                                                             'of '
                                                                             'Zoology, '
                                                                             'Chinese '
                                                                             'Academy '
                                                                             'of '
                                                                             'Sciences(中国科学院动物研究所)',
                                                              'name': 'Yang '
                                                                      'Qi-Sen(杨奇森)'}],
                                          'Synonyms': [{'refs': [{'[1]': 'Don '
                                                                         'E. '
                                                                         'Wilson '
                                                                         'and '
                                                                         'DeeAnn '
                                                                         'M. '
                                                                         'Reeder '
                                                                         '(eds.), '
                                                                         '2005. '
                                                                         'Mammal '
                                                                         'Species '
                                                                         'of '
                                                                         'the '
                                                                         'World. '
                                                                         'Mammal '
                                                                         'Species '
                                                                         'of '
                                                                         'the '
                                                                         'World, '
                                                                         '3rd '
                                                                         'edition, '
                                                                         'Baltimore:The '
                                                                         'Johns '
                                                                         'Hopkins '
                                                                         'University '
                                                                         'Press. '}],
                                                        'synonym': 'Panthera '
                                                                   'uncia'},
                                                       {'refs': [{'[1]': 'Don '
                                                                         'E. '
                                                                         'Wilson '
                                                                         'and '
                                                                         'DeeAnn '
                                                                         'M. '
                                                                         'Reeder '
                                                                         '(eds.), '
                                                                         '2005. '
                                                                         'Mammal '
                                                                         'Species '
                                                                         'of '
                                                                         'the '
                                                                         'World. '
                                                                         'Mammal '
                                                                         'Species '
                                                                         'of '
                                                                         'the '
                                                                         'World, '
                                                                         '3rd '
                                                                         'edition, '
                                                                         'Baltimore:The '
                                                                         'Johns '
                                                                         'Hopkins '
                                                                         'University '
                                                                         'Press. '}],
                                                        'synonym': 'Felis '
                                                                   'uncia'}],
                                          'chineseName': '雪豹',
                                          'scientificName': 'Uncia '
                                                            'uncia(Schreber,1775)',
                                          'taxonTree': {'class': 'Mammalia',
                                                        'family': 'Felidae',
                                                        'genus': 'Uncia',
                                                        'infraspecies': '',
                                                        'kingdom': 'Animalia',
                                                        'order': 'CARNIVORA',
                                                        'phylum': 'Chordata',
                                                        'species': 'uncia'}}}
```

## Contribution

Contributions to this package are welcome. 
The preferred method of contribution is through a GitHub pull request. 
Feel also free to contact us by creating an issue.

## Acknowledgment

The development of this SP2000 package were supported by the Biodiversity Survey and Assessment Project of the Ministry of Ecology and Environment, China ([**2019HJ2096001006**](http://www.mee.gov.cn/xxgk/zfcg/zbxx09/201906/t20190620_707171.shtml)) and the Yunnan University's Research Innovation Fund for Graduate Students.
