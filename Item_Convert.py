import json
from pykakasi import kakasi
import jaconv

# 伸ばし棒を母音に変換する
enable_vowelConvert = False

# 濁音・半濁音を変換する
enable_dullsConvert = True

# 拗音を変換する（例：ぁ→あ）
enable_contractedConvert = False

# 使用不可なアイテムをJSONファイルから削除しない
enable_unusableItemsKeep = True

# 使用不可なアイテムのアイテム名を変更する
enable_unusableItemsRename = True

# アイテム名変更が有効な場合、アイテム名に加える文字列を指定する
unusableItems_adding = "使用不可 "

kakasiObj = kakasi()

convertvowel = {"a": "あ", "i": "い", "u": "う", "e": "え", "o": "お"}
convertContracted = {"ぁ": "あ", "ぃ": "い", "ぅ": "う", "ぇ": "え", "ぉ": "お"}
convertChars = {"が": "か", "ぎ": "き", "ぐ": "く", "げ": "け", "ご": "こ",
                "ざ": "さ", "じ": "し", "ず": "す", "ぜ": "せ", "ぞ": "そ",
                "だ": "た", "ぢ": "ち", "づ": "つ", "で": "て", "ど": "と",
                "ば": "は", "び": "ひ", "ぶ": "ふ", "べ": "へ", "ぼ": "ほ",
                "ぱ": "は", "ぴ": "ひ", "ぷ": "ふ", "ぺ": "へ", "ぽ": "ほ", }
convertStrings = {"色": "いろ", "TNT": "てぃーえぬてぃー", "・": ""}
convertVA = {"ゔぁ": "は", "ゔぃ": "ひ", "ゔぇ": "へ", "ゔぉ": "ほ", "ゔ": "ふ"}

HIRA = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ"
HIRA += "まみむめもやゆよらりるれろわをん"
HIRA += "ぁぃぅぇぉゃゅょっー"

with open("ja_jp_items.json", "rb") as f:
    dict = json.load(f)

resultDict = {}

for key, val in dict.items():
    # 先にConvertStringで変換しておく
    result = val
    for key2, val2 in convertStrings.items():
        result = result.replace(key2, val2)
    # 漢字をひらがなへ
    result = "".join([i["hira"] for i in kakasiObj.convert(result)])
    # カタカナをひらがなへ
    result = jaconv.kata2hira(result)
    # 「おーくの」を削除
    result = result.replace("だーくおーくの", "replacing")
    result = result.replace("おーくの", "")
    result = result.replace("replacing", "だーくおーくの")
    # ヴぁ等を変換
    for key2, value2 in convertVA.items():
        result = result.replace(key2, value2)

    tmp = ""
    check = True
    for i, value in enumerate(result):
        # 伸ばし棒を、直前の文字列の母音に変換
        if i != 0 and value == "ー" and enable_vowelConvert:
            tmp += convertvowel["".join([i["hepburn"] for i in kakasiObj.convert(result[i - 1])])[-1]]
        elif value in convertChars and enable_dullsConvert:
            # convertCharsのように変換
            tmp += convertChars[value]
        elif value in convertContracted and enable_contractedConvert:
            # convertContractedのように変換
            tmp += convertContracted[value]
        else:
            tmp += value

        # 文字列がHIRAに含まれているか調べる
        if not (tmp[-1] in HIRA or tmp[-1] in convertChars):
            check = False
    result = tmp
    if check:
        resultDict[key] = result
    else:
        if enable_unusableItemsRename:
            result = unusableItems_adding + result
        if enable_unusableItemsKeep:
            resultDict[key] = result


with open("result_json/ja_jp_items.json", "w", encoding="UTF-8") as f:
    json.dump(resultDict, f, indent=4, ensure_ascii=False)
