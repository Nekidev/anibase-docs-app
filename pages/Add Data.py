import streamlit as st
from components.input import *
from translations import get_translated_string
import config

language = st.session_state["language"] if "language" in st.session_state else "English"
page = "Add Data"

st.title(get_translated_string(language, page, "title"))

with st.sidebar:
    langs = [
        "English",
        "Spanish (español)",
    ]
    language = st.session_state["language"] = st.selectbox(
        get_translated_string(language, page, "language"),
        langs,
        index=langs.index(language),
    )

st.write(get_translated_string(language, page, "description"))

st.write(
    f"""
## {get_translated_string(language, page, "user_information")}
"""
)

username = st.text_input(
    get_translated_string(language, page, "user_username"),
    placeholder="e.g. JohnDoe",
    key="user_username",
)

""

st.write(
    f"""
## {get_translated_string(language, page, "form")}
"""
)

add_tab, edit_tab = st.tabs(["Add new data", "Edit existent data"])

with add_tab:

    with st.form(key="form"):

        ""

        title_canonical = st.text_input(
            label=get_translated_string(language, page, "form_title_canonical"),
            placeholder="e.g. 'The Detective is Already Dead'",
        )

        ""

        title_english = st.text_input(
            label=get_translated_string(language, page, "form_title_english"),
            placeholder="e.g. 'The Detective is Already Dead'",
        )

        ""

        title_spanish = st.text_input(
            label=get_translated_string(language, page, "form_title_spanish"),
            placeholder="e.g. 'La Detective está Muerta'",
        )

        ""

        title_romaji = st.text_input(
            label=get_translated_string(language, page, "form_title_romaji"),
            placeholder="e.g. 'Tantei wa mou, shindeiru.'",
        )

        ""

        title_japanese = st.text_input(
            label=get_translated_string(language, page, "form_title_japanese"),
            placeholder="e.g. '探偵はもう、死んでいる。'",
        )

        ""

        description = st.text_area(
            label=get_translated_string(language, page, "form_description"),
            placeholder="e.g. 'My Hero Academia is a Japanese superhero manga series written and illustrated by Kōhei Horikoshi. The series has been serialized in Weekly Shōnen Jump since July 2014, with its chapters additionally collected into 28 tankōbon volumes as of March 2021.'",
        )

        ""

        media_type = st.selectbox(
            "Media type",
            [
                "Anime",
                "Manga",
            ],
            index=0,
        )

        ""

        show_type = st.selectbox(
            "Show type",
            [
                "TV",
                "Movie",
                "OVA",
                "ONA",
                "Special",
                "Music",
            ],
            index=0,
        )

        ""

        translated_genres = [
            get_translated_string(
                language, page, f"genre_{genre.lower().replace(' ', '').replace('-', '')}"
            )
            for genre in [
                "Action",
                "Adventure",
                "Comedy",
                "Drama",
                "Fantasy",
                "Hentai",
                "Horror",
                "Magic",
                "Mystery",
                "Psychological",
                "Romance",
                "Sci-Fi",
                "Slice of Life",
                "Supernatural",
            ]
        ]

        genres = st.multiselect(
            label=get_translated_string(language, page, "form_genres"),
            options=translated_genres,
        )

        ""

        cover = st.file_uploader(
            label=get_translated_string(language, page, "form_cover"),
            type=["png", "jpg", "jpeg"],
        )

        ""

        banner = st.file_uploader(
            label=get_translated_string(language, page, "form_banner"),
            type=["png", "jpg", "jpeg"],
        )

        ""

        related = st.text_area(label=get_translated_string(language, page, "form_related"), placeholder="Write the AniBase ID (if posible) of the related media here.\n\ne.g.:\n1 - Sequel\n2 - Side Story", height=144)

        ""
        
        st.caption("Make sure to have filled as much information as possible.")

        st.form_submit_button(label="Submit")

with edit_tab:

    st.info("In progress...")