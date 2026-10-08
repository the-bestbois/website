from typing import Optional

from flask import Blueprint, redirect, render_template, request, session, url_for

bp = Blueprint('core', __name__)

# TODO: add Makers page


@bp.route('/')
def index():
    return render_template('index.html.jinja')


@bp.route('/lore')
def lore():
    return render_template('lore.html.jinja')


@bp.route('/team')
def team():

    social_icons = {
        "website": "socicon-internet",
        "twitter": "socicon-twitter",
        "tumblr": "socicon-tumblr",
        "mastodon": "socicon-mastodon",
        "youtube": "socicon-youtube",
        "sketchfab": "socicon-sketchfab",
        "deviantart": "socicon-deviantart",
        "flag": "flag-icon-nl flag-icon",
    }

    # TODO: Move all this data somewhere else (JSON or SQLite maybe)

    user_data = {
        "Zexc": {
            "avatar": {"url": "zexc.png"},
            "links": [{"type": "twitter", "url": "https://x.com/ZexisZexc"}],
        },
        "Foxbright": {
            "avatar": {"url": "rustydustyfox.png", "background-position": "50% 35%"},
            "links": [],
        },
        "WBGaming": {
            "avatar": {"url": "wbgaming.jpg", "background-position": "50% 45%"},
            "links": [],
        },
        "Myaggu": {"avatar": {"url": "myaggic.png"}, "links": []},
        "Demirramon": {
            "avatar": {"url": "demirramon.jpg", "background-position": "28% 28%"},
            "links": [
                {"type": "website", "url": "https://demirramon.com/about"},
                {"type": "mastodon", "url": "https://cyberfurz.social/@demirramon"},
                {"type": "youtube", "url": "https://www.youtube.com/@demirramon"},
            ],
        },
        "koslie": {
            "avatar": {"url": "koslie.png", "background-position": "50% 15%"},
            "links": [
                {"type": "website", "url": "https://eoiasrt.com/"},
                {
                    "type": "youtube",
                    "url": "https://www.youtube.com/channel/UC0DVuxuG-3Db8EYhjf88jWg",
                },
            ],
        },
        "Cobra Witch": {"avatar": {"url": "cobrawitch.jpg"}, "links": []},
        "Journey": {"avatar": {"url": "journey.jpg"}, "links": []},
        "Rulfam": {"avatar": {"url": "rulfam.png"}, "links": []},
        "Eevibow": {"avatar": {"url": "eevibow.png"}, "links": []},
        "Samurai": {"avatar": {"url": "samurai.png"}, "links": []},
        "Asper Fel'Ok": {"avatar": {"url": "theautisticdragon.png"}, "links": []},
        "Banshee": {"avatar": {"url": "banshee.png"}, "links": []},
        "TΛKӨDΛ☥": {"avatar": {"url": "dragonicankh.webp"}, "links": []},
        "Marz": {
            "avatar": {"url": "youseamarz.png", "background-position": "50% 28%"},
            "links": [],
        },
        "MaitakeShiba": {"avatar": {"url": "maitake.jpg"}, "links": []},
        "Timo": {
            "avatar": {"url": "timo.png"},
            "links": [{"type": "twitter", "url": "https://twitter.com/spicypolys"}],
        },
        "Whouse": {
            "avatar": {"url": "whouse.jpg"},
            "links": [
                {
                    "type": "twitter",
                    "url": "https://twitter.com/kouji_shimazu",
                }
            ],
        },
        "Cyphiegorawr": {
            "avatar": {"url": "cyphiegorawr.jpg"},
            "links": [{"type": "twitter", "url": "https://cyphiegorawr.gumroad.com/"}],
        },
        "Pammematth": {
            "avatar": {"url": "pammematth.jpg"},
            "links": [{"type": "twitter", "url": "https://twitter.com/DJBassFox28"}],
        },
        "Orze": {
            "avatar": {"url": "orze.jpg"},
            "links": [{"type": "twitter", "url": "https://twitter.com/orzeeee"}],
        },
        "VictonRoy": {
            "avatar": {"url": "victonroy.jpg"},
            "links": [{"type": "twitter", "url": "https://twitter.com/RoyVicton"}],
        },
        "Pelmeow": {
            "avatar": {"url": "pelmeow.jpg"},
            "links": [{"type": "tumblr", "url": "https://colatastic.tumblr.com/"}],
        },
        "DeliriousJax": {
            "avatar": {"url": "deliriousjax.jpg"},
            "links": [{"type": "twitter", "url": "https://twitter.com/deliriousjax"}],
        },
        "Wiah": {
            "avatar": {"url": "wiah.png"},
            "links": [{"type": "twitter", "url": "https://twitter.com/YanWiah"}],
        },
        "Dyze": {
            "avatar": {"url": "dyze.png"},
            "links": [{"type": "sketchfab", "url": "https://sketchfab.com/Dyze"}],
        },
        "Über Winfrey": {
            "avatar": {"url": "uber_winfrey.jpg"},
            "links": [{"type": "twitter", "url": "https://twitter.com/Uber_Winfrey"}],
        },
        "Rezillo Ryker": {
            "avatar": {"url": "rezillo_ryker.jpg"},
            "links": [{"type": "twitter", "url": "https://twitter.com/RezilloArt"}],
        },
        "Thekibblemeister": {
            "avatar": {"url": "thekibblemeister.png"},
            "links": [
                {
                    "type": "deviantart",
                    "url": "https://www.deviantart.com/thekibblemeister",
                }
            ],
        },
        "Julian": {
            "avatar": {"url": "julian.png", "background-position": "25% 70%"},
            "links": [{"type": "flag", "url": "/418"}],
        },
    }

    team_data = {
        "board": {
            "title": "Board members",
            "icon": "fa-crown",
            "members": [
                {
                    "name": "Zexc",
                    "subtitle": "A.K.A. zex",
                    "description": "Former project director.",
                },
                {
                    "name": "Foxbright",
                    "subtitle": "A.K.A. rustydustyfox",
                    "description": "Former project director.",
                },
                {"name": "WBGaming", "subtitle": "", "description": ""},
                {"name": "Myaggu", "subtitle": "A.K.A. myaggic", "description": ""},
                {"name": "Demirramon", "subtitle": "", "description": ""},
                {
                    "name": "koslie",
                    "subtitle": "",
                    "description": "\"Stop capitalizing my name!!\"",
                },
            ],
        },
        "moderation": {
            "title": "Moderators",
            "icon": "fa-balance-scale",
            "members": [
                {
                    "name": "Cobra Witch",
                    "subtitle": "Moderation team lead",
                    "description": "",
                },
                {
                    "name": "WBGaming",
                    "subtitle": "",
                    "description": "<i>\"Why are you in every team?\"<br>- Demi</i>",
                },
                {
                    "name": "koslie",
                    "subtitle": "",
                    "description": "\"Stop capitalizing my name!!\"",
                },
                {"name": "Demirramon", "subtitle": "", "description": ""},
            ],
        },
        "events": {
            "title": "Event hosts",
            "icon": "fa-users",
            "members": [
                {"name": "koslie", "subtitle": "Events team lead", "description": ""},
                {"name": "Rulfam", "subtitle": "", "description": ""},
                {"name": "Eevibow", "subtitle": "", "description": ""},
                {"name": "Cobra Witch", "subtitle": "", "description": ""},
                {
                    "name": "Samurai",
                    "subtitle": "",
                    "description": "Unfortunately, born and raised on a small island known as the UK.",
                },
                {
                    "name": "Demirramon",
                    "subtitle": "",
                    "description": "Always fashionably late. On purpose, of course.<br><i>Source: trust me bro.</i>",
                },
            ],
        },
        "art": {
            "title": "Art team",
            "icon": "fa-object-group",
            "members": [
                {
                    "name": "WBGaming",
                    "subtitle": "Art team lead",
                    "description": "Worked on HD updates and made the Quest version.",
                },
                {"name": "koslie", "subtitle": "", "description": ""},
                {"name": "Marz", "subtitle": "A.K.A. youseamarz", "description": ""},
                {
                    "name": "Foxbright",
                    "subtitle": "A.K.A. rustydustyfox",
                    "description": "Made many textures for public bestboi avatars.",
                },
                {
                    "name": "Demirramon",
                    "subtitle": "3D modeler & texture artist, VRCSDK specialist",
                    "description": "Did the initial Avatars 3.0 setup for the Bestboi HD, Toon, and Classic.",
                },
                {"name": "Eevibow", "subtitle": "", "description": ""},
                {"name": "Cobra Witch", "subtitle": "", "description": ""},
            ],
        },
        "former-3d-artists": {
            "title": "Former 3D artists",
            "icon": "socicon-sketchfab",
            "members": [
                {
                    "name": "MaitakeShiba",
                    "subtitle": "3D modeler & texture artist",
                    "description": "Main modeler responsible for the Chibi and Kemono models.",
                },
                {
                    "name": "Timo",
                    "subtitle": "3D modeler",
                    "description": "Main modeler for the Bestboi HD Edition.",
                },
                {
                    "name": "Whouse",
                    "subtitle": "3D modeler & rigging specialist",
                    "description": "Helped do rigging for bestboi HD, as well as custom blendshapes.",
                },
                {
                    "name": "Cyphiegorawr",
                    "subtitle": "3D modeler",
                    "description": "Made the 3.8 update for the Bestboi Toon model.",
                },
                {
                    "name": "Pammematth",
                    "subtitle": "Rigging Specialist",
                    "description": "Made the rig for the first version of the Bestboi Toon model.",
                },
                {
                    "name": "Orze",
                    "subtitle": "Texture Artist",
                    "description": "Base Texture artist for the Bestboi HD Edition.",
                },
                {
                    "name": "VictonRoy",
                    "subtitle": "3D modeler",
                    "description": "Responsible for the Bestboi Classic Update, as well as the Dutchie edit.",
                },
                {
                    "name": "Pelmeow",
                    "subtitle": "3D modeler & texture Artist",
                    "description": "Created the original sculpt and textures for the first version of the Bestboi Toon.",
                },
                {
                    "name": "DeliriousJax",
                    "subtitle": "3D modeler",
                    "description": "Made the v3 update for the Toon Bestboi.",
                },
                {
                    "name": "Wiah",
                    "subtitle": "3D modeler",
                    "description": "Created the Sculpt for the Bestboi HD edition",
                },
                {
                    "name": "Dyze",
                    "subtitle": "3D modeler & texture artist",
                    "description": "Created the Bestboi Staff outfits, as well as the winter outfit and many yet unreleased outfits.",
                },
                {
                    "name": "Über Winfrey",
                    "subtitle": "3D modeler & texture artist",
                    "description": "Created the Bestboi HD Hoodie outfit alongsite other outfits still in the works.",
                },
                {
                    "name": "Rezillo Ryker",
                    "subtitle": "3D modeler.",
                    "description": "Assisted with the creation of the Bestboi HD edition.",
                },
                {
                    "name": "Thekibblemeister",
                    "subtitle": "3D modeler & texture artist",
                    "description": "Creator of the OG Bestboi model (classic).<br>Lead the original Bestboi community from its creation on 2017 to early 2018. He then retired and allowed the community to split and choose their own leaders.",
                },
            ],
        },
        "website": {
            "title": "Website developers & maintainers",
            "icon": "mbrib-sites",
            "members": [
                {
                    "name": "Julian",
                    "subtitle": "Website creator & restoration assistant",
                    "description": "Just some 23 yo makin games and making free websites. mainly uses C#, Udon Graph, and some bash if im working in Linux.<br><br>Designed and created the website. For issues you can contact me on discord at <b>ryderuwu</b>",
                },
                {
                    "name": "Rulfam",
                    "subtitle": "Website maintainer",
                    "description": "<i>\"Why do you look so gay?\"<br>- Samurai</i>",
                },
                {
                    "name": "Demirramon",
                    "subtitle": "Website maintainer",
                    "description": "<i>\"Why are you in every team?\"<br>- Koslie</i>",
                },
            ],
        },
    }

    return render_template(
        'team.html.jinja', teams=team_data, users=user_data, socicons=social_icons
    )


@bp.route('/418')
@bp.app_errorhandler(418)
def im_a_teapot(_error: Optional[Exception] = None):
    return render_template('errors/418.html.jinja'), 418


@bp.route('/set-lang/<locale>')
def set_language(locale: str):
    session['language'] = locale

    return redirect(request.referrer or url_for('core.index'))
