import genanki

css = """
.card {
  margin-top:100px;
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
.Front{
    font-size: 40px;
}
"""

chineseModel = genanki.Model(
  1400299068,
  'Chinese',
  fields=[
    {'name': 'Character'},
    {'name': 'Meaning'},
    {'name': 'Pinyin'},
  ],
  templates=[
    {
      'name': 'Common chinese character',
      'qfmt': '<div class="Front">{{Character}}</div>',
      'afmt': '{{FrontSide}}<hr id="answer">{{Pinyin}}<hr>{{Meaning}}',
    }],
    css=css
)

chinese = genanki.Deck(
    1995159697,
    "Chinese 1000 most common"
)

def generatePkg(df):
    for char,pinyin,meaning in zip(df["Simplified"],df["Pinyin"],df["Meaning"]):
        note = genanki.Note(model=chineseModel,fields=[char,meaning,pinyin])
        chinese.add_note(note)

    genanki.Package(chinese).write_to_file('output.apkg')


