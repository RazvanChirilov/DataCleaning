highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")
highlighted_poems_stripped = highlighted_poems.strip()

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped)
highlighted_poems_details = highlighted_poems.split("\n")

highlighted_poems_details = []
for i in highlighted_poems_stripped:
    highlighted_poems_details.append(i.split(":"))

    titles = []
    poets = []
    dates = []

    for i in highlighted_poems_details:
        titles.append(i[0])
        poets.append(i[1])
        dates.append(i[2])

print(titles)
print(poets)
print(dates)


# The poem TITLE was published by POET in DATE

def highlighted_poems_details(titles, poets, dates):
    return f"The poem {titles} was published by {poets} in {dates}."
