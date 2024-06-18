from shiny.ui import modal_show, modal, modal_button
from htmltools import TagList, tags

about_text = TagList(
    tags.h3("About"),
    tags.br(),
    tags.p(
        """
        La contaminació de l'aire sempre ha estat un problema 
        per al món i al llarg dels anys, però sobretot amb 
        la pandèmia. 

        A través d'aquesta aplicació, volem explorar la relació
        entre la mesura de les partícules PM2.5 i la taxa de 
        mortalitat (morts per 100.000 habitants) a causa de
        malalties respiratòries a tot el món al llarg dels anys.

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
    Seleccioneu les dates en el mapa.
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
    Per defecte, les dades d'Espanya apareixen
    dibuixades.
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
                    "https://data-explorer.oecd.org/vis?pg=0&snb=6&tm=PM2.5&vw=tb&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_AIR_POL%40DF_AIR_POLL&df%5Bag%5D=OECD.ENV.EPI&df%5Bvs%5D=1.0&pd=%2C&dq=.A.MEAN_POP...MCG_M3.&to%5BTIME_PERIOD%5D=false"
                ),
            )
        ),
        tags.li(
            tags.a(
                "OECD Data Explorer • Health risks • Respiratory system diseases mortality crude rate",
                href=(
                    "https://data-explorer.oecd.org/vis?pg=0&bp=true&snb=20&tm=MORTALITY&vw=tb&df%5Bds%5D=dsDisseminateFinalDMZ&df%5Bid%5D=DSD_REG_HEALTH%40DF_RISK&df%5Bag%5D=OECD.CFE.EDS&df%5Bvs%5D=1.0&pd=%2C&dq=A.CTRY...MORT_ICDJ_CRUDE_RATIO...&ly%5Brw%5D=REF_AREA&ly%5Bcl%5D=TIME_PERIOD&to%5BTIME_PERIOD%5D=false"
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
        1990, 1995, 2000, 2005, 2010 i 2010 en endavant..
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
