import folium
import json
from types import SimpleNamespace
from folium import plugins


class Mapa:

    with open("dumps.json") as f:
        dane = json.load(f)

    m = folium.Map(location=[51.5509, 19.0803])
    cluster = folium.plugins.MarkerCluster().add_to(m)

    print(dane)

    for kordy in dane:
        html = "<img src=\"" + dane[kordy]["filename"] + "\" style=\"width:450;margin:auto\">"

        iframe = folium.IFrame(html,
                               width=500,
                               height=500)

        folium.Marker(location=[dane[kordy]["lat"], dane[kordy]["lon"]],
                      popup=folium.Popup(iframe,
                                         parse_html=True,
                                         maxwidth=500)
        ).add_to(cluster)

    m.save('mapa.html')
