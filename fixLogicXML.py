import os
import xml.etree.ElementTree as ET

def process_xml(file_content):
    # ファイル内の文字列を取り出す
    loaded_xml = file_content

    # DOMの準備
    xmlDoc = ET.ElementTree(ET.fromstring(loaded_xml))

    # 読み込んだXMLのDOMを操作
    part_name_elements = xmlDoc.findall(".//part-name")
    
    # Select all the midi-program elements in the XML
    midi_program_elements = xmlDoc.findall(".//midi-program")
    instrument_name_elements = xmlDoc.findall(".//instrument-name")

    # Loop through the midi-program elements and set their content based on the condition
    for elem in midi_program_elements:
        if elem.text == "53":
            elem.text = "1"

    # Loop through the instrument-name elements and set their content based on the condition
    for elem in instrument_name_elements:
        if elem.text == "Choir Aahs":
            elem.text = "Piano"

    # 出力用Xmlを用意
    output_xml_text = ET.tostring(xmlDoc.getroot()).decode()

    return output_xml_text

def process_file(file_path):
    try:
        # ファイルを読み込む
        with open(file_path, 'r') as file:
            file_content = file.read()

        # XMLの処理
        processed_xml = process_xml(file_content)

        # ファイルを上書きする
        with open(file_path, 'w') as file:
            file.write(processed_xml)

        print(f"{file_path} の書き換えが成功しました。")

    except Exception as e:
        print(f"{file_path} の書き換え中にエラーが発生しました: {e}")

# 同じフォルダ内のXMLファイルを検索して処理する
current_directory = os.getcwd()

# 同じフォルダ内のXMLファイルをリストアップ
xml_files = [file for file in os.listdir(current_directory) if file.endswith('.xml')]

if xml_files:
    for xml_file in xml_files:
        # ファイルの処理を実行
        process_file(xml_file)
else:
    print("XMLファイルが見つかりませんでした。")
