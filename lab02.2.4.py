"""
According to data collected by the Unicode Consortium1,
the non-profit organization responsible for digitizing
the world's languages, "tears of joy" ( ) account for
more than 5% of all emojis used (the only other character
that comes close to it is the ). The top ten emojis used
worldwide are: .
When exchanging messages on Telegram
(or on your favorite messaging app),
which are the three emojis that you personally use most
frequently? Using the Unicode encoding information
collected here2, you cancreate a program that shows
a scheme for each of these three emojis:
I. the position in the ranking (rank);
II. the Unicode Number;
III. the Unicode Name;
IV. the emoji itself.
Format the output so that the information related
to each of the three emojis is collected on one line,
and the different fields are aligned vertically.
"""

#define the three emojis

emoji1 = "😂"
emoji2 = "😍"
emoji3 = "😘"

#define the information for each emoji

emoji1_info = (1, "U+1F602","face with tears of joy", emoji1)
emoji2_info = (5, "U+1F60D", "smiling face with heart-shaped eyes", emoji2)
emoji3_info = (8, "U+1F618", "face throwing a kiss", emoji3)

#print the information for each emoji

print("Rank:", emoji1_info[0], "Unicode Number:", emoji1_info[1], "Unicode Name:", emoji1_info[2], "Emoji:", emoji1_info[3])
print("Rank:", emoji2_info[0], "Unicode Number:", emoji2_info[1], "Unicode Name:", emoji2_info[2], "Emoji:", emoji2_info[3])
print("Rank:", emoji3_info[0], "Unicode Number:", emoji3_info[1], "Unicode Name:", emoji3_info[2], "Emoji:", emoji3_info[3])