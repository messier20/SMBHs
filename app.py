import pandas as pd

from googletrans import Translator

# Read a file
df = pd.read_csv("export.csv", delimiter=';', header=1)
df_processed = pd.read_csv("feedback.csv", delimiter='\t')
# df_processed = 0
translator = Translator()


translations = []
try:
    # print(len(df_processed))
    for index, comment in enumerate(df["Comment"][len(df_processed):len(df_processed)+1000], 0):
    # for index, comment in enumerate(df["Comment"][:5], 0):
        translator = Translator()
        print(index)
        comment = comment.encode('ascii', 'ignore').decode('ascii')
        comment_modified = translator.translate(comment, src='sv').text
        translations.append(comment_modified)
        # translations.append("comment")
finally:
    # df_to_write = pd.DataFrame({'comment_se': df["Comment"][:len(translations)], 'comment_en': translations, 'tags': df["Labels"][:len(translations)]})
    df_to_write = pd.DataFrame({'comment_se': df["Comment"][len(df_processed):len(df_processed)+len(translations)], 'comment_en': translations, 'tags': df["Labels"][len(df_processed):len(df_processed)+len(translations)]})
    df_to_write.to_csv("feedback.csv",
                        index=False,
                        header=False,
                        sep='\t',
                        mode='a')

print(translations)





# df_to_write = pd.DataFrame({'comment': translations, 'tags': df["Labels"][:100]})
# df_to_write.to_csv('comments.csv', index=False)