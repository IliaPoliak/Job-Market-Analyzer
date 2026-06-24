# Default Config

```py
LOG_FILENAME="pipeline_progress.log"

LOCATION = "bratislava"
FIELD = "informacne-technologie"
```

# `LOG_FILENAME`

You can change the pipeline logging file destination by changing this variable

e.g.

```py
LOG_FILENAME="logger/pipeline_progress.log"
```

# `LOCATION`

You can change the job location to search by choosing a different value for this variable from below

P.S. most jobs are in Slovakia because the project extracts data from Slovak job posting website

```py
# All Locations

LOCATION = ""

# Slovakia

LOCATION = "bratislavsky-kraj"
LOCATION = "bratislava"
LOCATION = "okres-malacky"
LOCATION = "okres-pezinok"
LOCATION = "okres-senec"

LOCATION = "trnavsky-kraj"
LOCATION = "okres-trnava"
LOCATION = "okres-dunajska-streda"
LOCATION = "okres-galanta"
LOCATION = "okres-hlohovec"
LOCATION = "okres-piestany"
LOCATION = "okres-senica"
LOCATION = "okres-skalica"

LOCATION = "trenciansky-kraj"
LOCATION = "okres-trencin"
LOCATION = "okres-banovce-nad-bebravou"
LOCATION = "okres-ilava"
LOCATION = "okres-myjava"
LOCATION = "okres-nove-mesto-nad-vahom"
LOCATION = "okres-partizanske"
LOCATION = "okres-povazska-bystrica"
LOCATION = "okres-prievidza"
LOCATION = "okres-puchov"

LOCATION = "nitriansky-kraj"
LOCATION = "okres-nitra"
LOCATION = "okres-komarno"
LOCATION = "okres-levice"
LOCATION = "okres-nove-zamky"
LOCATION = "okres-sala"
LOCATION = "okres-topolcany"
LOCATION = "okres-zlate-moravce"

LOCATION = "zilinsky-kraj"
LOCATION = "okres-zilina"
LOCATION = "okres-bytca"
LOCATION = "okres-cadca"
LOCATION = "okres-dolny-kubin"
LOCATION = "okres-kysucke-nove-mesto"
LOCATION = "okres-liptovsky-mikulas"
LOCATION = "okres-martin"
LOCATION = "okres-namestovo"
LOCATION = "okres-ruzomberok"
LOCATION = "okres-turcianske-teplice"
LOCATION = "okres-tvrdosin"

LOCATION = "banskobystricky-kraj"
LOCATION = "okres-banska-bystrica"
LOCATION = "okres-banska-stiavnica"
LOCATION = "okres-brezno"
LOCATION = "okres-detva"
LOCATION = "okres-krupina"
LOCATION = "okres-lucenec"
LOCATION = "okres-poltar"
LOCATION = "okres-revuca"
LOCATION = "okres-rimavska-sobota"
LOCATION = "okres-velky-krtis"
LOCATION = "okres-zvolen"
LOCATION = "okres-zarnovica"
LOCATION = "okres-ziar-nad-hronom"

LOCATION = "presovsky-kraj"
LOCATION = "okres-presov"
LOCATION = "okres-bardejov"
LOCATION = "okres-humenne"
LOCATION = "okres-kezmarok"
LOCATION = "okres-levoca"
LOCATION = "okres-medzilaborce"
LOCATION = "okres-poprad"
LOCATION = "okres-sabinov"
LOCATION = "okres-snina"
LOCATION = "okres-stara-lubovna"
LOCATION = "okres-stropkov"
LOCATION = "okres-svidnik"
LOCATION = "okres-vranov-nad-toplou"

LOCATION = "kosicky-kraj"
LOCATION = "kosice"
LOCATION = "okres-gelnica"
LOCATION = "okres-michalovce"
LOCATION = "okres-roznava"
LOCATION = "okres-sobrance"
LOCATION = "okres-spisska-nova-ves"
LOCATION = "okres-trebisov"

# Abroad

LOCATION = "zahranicie"         # All Abroad

LOCATION = "ceska-republika"    # Czech Republic
LOCATION = "polsko"             # Poland
LOCATION = "madarsko"           # Hungary
LOCATION = "rumunsko"           # Romania
LOCATION = "chorvatsko"         # Croatia

LOCATION = "nemecko"            # Germany
LOCATION = "rakusko"            # Austria
LOCATION = "svajciarsko"        # Switzerland

LOCATION = "holandsko"          # Netherlands
LOCATION = "belgicko"           # Belgium

LOCATION = "francuzsko"         # France
LOCATION = "spanielsko"         # Spain
LOCATION = "taliansko"          # Italy

LOCATION = "svedsko"            # Sweden
LOCATION = "finsko"             # Finland
LOCATION = "norsko"             # Norway
LOCATION = "dansko"             # Denmark

LOCATION = "grecko"             # Greece
LOCATION = "cyprus"             # Cyprus
LOCATION = "malta"              # Malta

LOCATION = "usa"                # USA
LOCATION = "velka-britania"     # United Kingdom
LOCATION = "irsko"              # Ireland

LOCATION = "zahranicie-ostatne" # Abroad Others
```

# `FIELD`

You can change the job field to search by choosing a different value for this variable from below

P.S. the skills are chosen specifically for IT jobs and may not work properly for other fields

```py
FIELD = ""                                                  # All Fields

# A                                                         # A

FIELD = "umenie-a-kultura"                                  # Art and Culture
FIELD = "polnohospodarstvo-a-potravinarstvo"                # Agriculture and Food Industry
FIELD = "administrativa"                                    # Administration
FIELD = "automobilovy-priemysel"                            # Automotive Industry
FIELD = "pomocne-prace"                                     # Auxiliary/Manual Labor

# B                                                         # B

FIELD = "bankovnictvo"                                      # Banking

# C                                                         # C

FIELD = "zakaznicka-podpora"                                # Customer Support
FIELD = "stavebnictvo-a-reality"                            # Construction and Real Estate
FIELD = "chemicky-priemysel"                                # Chemical Industry

# E                                                         # E

FIELD = "skolstvo-vzdelavanie-veda-vyskum"                  # Education, Training, Science, Research
FIELD = "ekonomika-financie-uctovnictvo"                    # Economics, Finance, Accounting
FIELD = "elektrotechnika-a-energetika"                      # Electrical Engineering and Energy

# H                                                         # H

FIELD = "zdravotnictvo-a-socialna-starostlivost"            # Healthcare and Social Care
FIELD = "ludske-zdroje-a-personalistika"                    # Human Resources and Personnel

# I                                                         # I

FIELD = "poistovnictvo"                                     # Insurance
FIELD = "informacne-technologie"                            # Information Technology

# J                                                         # J

FIELD = "zurnalistika-polygrafia-media"                     # Journalism, Printing, Media

# L                                                         # L

FIELD = "leasing"                                           # Leasing
FIELD = "pravo-a-legislativa"                               # Law and Legislation

# M                                                         # M

FIELD = "vyroba"                                            # Manufacturing/Production
FIELD = "strojarstvo"                                       # Mechanical Engineering
FIELD = "banictvo-hutnictvo"                                # Mining, Metallurgy
FIELD = "manazment"                                         # Management
FIELD = "marketing-reklama-pr"                              # Marketing, Advertising, PR

# P                                                         # P

FIELD = "farmaceuticky-priemysel"                           # Pharmaceutical Industry
FIELD = "statna-sprava-samosprava"                          # Public Administration, Local Government

# Q                                                         # Q

FIELD = "manazment-kvality"                                 # Quality Management

# S                                                         # S

FIELD = "bezpecnost-a-ochrana"                              # Security and Protection
FIELD = "sluzby"                                            # Services

# T                                                         # T

FIELD = "prekladatelstvo-a-tlmocnictvo"                     # Translation and Interpreting
FIELD = "obchod"                                            # Trade/Commerce
FIELD = "doprava-spedicia-logistika"                        # Transport, Forwarding, Logistics
FIELD = "cestovny-ruch-gastro-hotelierstvo"                 # Tourism, Gastronomy, Hospitality
FIELD = "technika-rozvoj"                                   # Technology, Development
FIELD = "telekomunikacie"                                   # Telecommunications
FIELD = "textilny-koziarsky-a-odevny-priemysel"             # Textile, Leather and Apparel Industry
FIELD = "vrcholovy-manazment"                               # Top Management

# W                                                         # W

FIELD = "drevospracujuci-priemysel"                         # Wood Processing Industry
FIELD = "vodohospodarstvo-lesnictvo-zivotne-prostredie"     # Water Management, Forestry, Environment
```
