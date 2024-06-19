from shiny.ui import modal_show, modal, modal_button
from htmltools import TagList, tags

about_text = TagList(
    tags.h3("About"),
    tags.br(),
    tags.p(
        """
        La contaminació de l'aire sempre ha estat un problema 
        per al món i al llarg dels anys.

        A través d'aquesta aplicació, volem explorar la relació
        entre la mesura de les partícules PM2.5 i la taxa de 
        mortalitat a causa de
        malalties respiratòries a tot el món al llarg dels anys.
        (morts per 100.000 habitants)

        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

slider_text_map = tags.p(
    """
    Seleccioneu les dates per veure el mapa.
    La mida del cercle representa la taxa de mortalitat 
    i la intensitat de color representa la mesura de PM2.5
    """,
    style="""
    text-align: justify;
    word-break:break-word;
    hyphens: auto;
    """,
)

slider_text_plot = tags.p(
    """
    Arrossega per seleccionar el rang d'anys i
    desplega per seleccionar els països a comparar. 
   
    """,
    style="""
    text-align: justify;
    word-break:break-word;
    hyphens: auto;
    """,
)

dataset_information = TagList(
    tags.strong(tags.h3("Origen de les Dades")),
    tags.p(
        """
        Les dades provenen de World Bank i 
        Organisation for Economic Co-operation and Development (OECD).
       
        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
    tags.ul(
        tags.li(
            tags.a(
                "World Bank",
                href=(
                    "https://data.worldbank.org/indicator/"
                    + "EN.ATM.PM25.MC.M3"
                ),
            )
        ),
        tags.li(
            tags.a(
                "OECD Data Explorer • Exposure to air pollution",
                href=(
                    "https://stats.oecd.org/Index.aspx?DataSetCode=EXP_PM2_5#"
                ),
            )
        ),
        tags.li(
            tags.a(
                "OECD Data Explorer • Health risks • Respiratory system diseases mortality crude rate",
                href=(
                    "https://stats.oecd.org/Index.aspx?DataSetCode=EXP_PM2_5#"
                ),
            )
        ),
    ),
)

missing_note = TagList(
    tags.p(
        tags.strong("Nota: "),
        """
        Durant els anys 1990 a 2010, les dades de PM2.5
        es van recollir cada cinc anys. És a dir, les dades 
        de PM2.5 només són disponibles per
        1990, 1995, 2000, 2005, 2010 i 2010 en endavant.
        """,
        style="""
        font-size: 14px;
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)


def info_modal():
    modal_show(
        modal(
            tags.strong(tags.h3("Contaminació Ambiental")),
            tags.p(
                "Relació entre PM2.5 i la mort per Malalties Respiratòries"
            ),
            tags.hr(),
            tags.strong(tags.h4("Descripció del Problema")),
            tags.p(
                """
            L'exposició a PM2,5 es refereix a la inhalació de partícules 
            fines que tenen un diàmetre de 2,5 micròmetres o menys. 
            Aquestes partícules són prou petites per penetrar profundament
            en el sistema respiratori, arribar als pulmons i potencialment
            entrar al torrent sanguini. 
            """,
                style="""
            text-align: justify;
            word-break:break-word;
            hyphens: auto;
            """,
            ),
            tags.p(
                """
            PM2.5 és una barreja de partícules diminutes i gotes líquides 
            que poden incloure una varietat de components com ara àcids
            (per exemple, nitrats i sulfats), productes químics orgànics, 
            metalls i partícules de sòl o pols.
            """,
                style="""
            text-align: justify;
            word-break:break-word;
            hyphens: auto;
            """,
            ),
            tags.p(
                """
            Les partícules fines (PM2,5) són el contaminant atmosfèric que 
            suposa un major risc per a la salut a nivell mundial, 
            afectant més persones que qualsevol altre contaminant. 
            L'exposició crònica augmenta considerablement el risc de patir 
            malalties respiratòries i cardiovasculars (OMS, 2018)
            """,
                style="""
            text-align: justify;
            word-break:break-word;
            hyphens: auto;
            """,
            ),
            tags.hr(),
            dataset_information,
            tags.hr(),
            missing_note,
            size="l",
            easy_close=True,
            footer=modal_button("Close"),
        )
    )
