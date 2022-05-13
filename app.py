import streamlit as st
import pandas as pd
import json
import os
import webbrowser
import xml.etree.ElementTree as ET
from medicament import Medicament
from validator import validate
from PIL import Image
from io import StringIO

st.set_page_config(
    page_title="Parser",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Parser-XML şi informaţie structurată")
show = pd.DataFrame({
    'options': ['Show XML', 'XML Parser', "Show JSON", 'JSON Parser', 'Validate XML : XSD', "Show XSD", "Show XSL", "Show DTD", "Show XML with XSL"]
})
option = st.sidebar.selectbox('Show:', show['options'])

if option == "XML Parser":
    uploaded_xml = st.file_uploader("Choose XML file", type=['xml'])
    if uploaded_xml is not None:
        mytree = ET.parse(uploaded_xml)
        myroot = mytree.getroot()
        mds_lst_xml = []
        for elem in myroot.findall('medicament'):
            nume = elem.find('nume').text
            afectiuni = ', '.join(
                [e.text for e in elem.findall('afectiune_medicala')])
            pret = elem.find('pret').text
            producator = (elem.find('producator').text,
                          elem.find('producator').attrib)
            cod_producator = '#' + producator[1]['cod']
            mod_administrare = elem.find('prospect/mod_administrare').text
            reactii_adverse = ', '.join([e.text for e in elem.findall(
                'prospect/reactie_adversa')])
            substante_active = [(e.text, e.attrib)
                                for e in elem.findall('prospect/substanta_activa')]
            mds_lst_xml.append(Medicament(nume, afectiuni, cod_producator,
                               producator[0], mod_administrare, reactii_adverse, substante_active, pret))

        st.table(Medicament.meds_to_df(mds_lst_xml))

elif option == "JSON Parser":
    uploaded_json = st.file_uploader("Choose JSON file", type=['json'])
    if uploaded_json is not None:
        mds_lst_json = []
        stringio = StringIO(uploaded_json.getvalue().decode("utf-8"))
        string_data = stringio.read()
        medicament_json = json.loads(string_data)
        for med in medicament_json['medicament']:
            nume = med['nume']
            afectiuni = ', '.join(med['afectiune_medicala'])
            pret = med['pret']
            producator = med['producator']['text']
            cod_producator = '#' + med['producator']['cod']
            mod_administrare = med['prospect']['mod_administrare']
            reactii_adverse = ', '.join(
                med['prospect']['reactie_adversa'] if 'reactie_adversa' in med['prospect'].keys() else [])
            substante_active = [(e['text'], {'gramaj': e['gramaj']})
                                for e in med['prospect']['substanta_activa']]
            pret = med['pret']
            mds_lst_json.append(Medicament(nume, afectiuni, cod_producator, producator,
                                mod_administrare, reactii_adverse, substante_active, pret))

        st.table(Medicament.meds_to_df(mds_lst_json))

elif option == "Validate XML : XSD":
    uploaded_files = st.file_uploader("Choose XML & XSD file", type=[
                                      'xml', 'xsd'], accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        _, file_extension = os.path.splitext(uploaded_file.name)
        if file_extension == '.xml':
            xml_file = uploaded_file
        elif file_extension == '.xsd':
            xsd_file = uploaded_file
    try:
        if xml_file and xsd_file:
            result = validate(xml_file, xsd_file)
            if result:
                st.subheader('XML valideaza schema(XSD)!')
            else:
                st.subheader('INVALID!')
    except:
        st.subheader('Adauga fisierele pentru validare!')
elif option == "Show XML":
    image = Image.open('assets/xml_pic.PNG')
    st.image(image, caption='Fisierul XML')
elif option == "Show XSD":
    image = Image.open('assets/xsd_pic.PNG')
    st.image(image, caption='Fisierul XSD')
elif option == "Show XSL":
    image = Image.open('assets/xsL_pic.PNG')
    st.image(image, caption='Fisierul XSL')
elif option == "Show DTD":
    image = Image.open('assets/dtd_pic.PNG')
    st.image(image, caption='Fisierul DTD')
elif option == "Show XML with XSL":
    # xml_file_path = os.getcwd() + '/farmacie.xml'
    xml_file_path= r'C:\\Users\\ianghel\Desktop\\xis\\farmacie.xml'
    webbrowser.open_new_tab(xml_file_path)
    image = Image.open('assets/xml_xsl.PNG')
    st.image(image, caption='Fisierul DTD')
elif option == "Show JSON":
    f = open('farmacie.json')
    medicament_json = json.load(f)
    f.close()
    st.json(medicament_json, expanded=True)
