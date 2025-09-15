questions2ADAC_INF = {
    # HTTP Request-Response Fragen
    "Worauf lässt sich der Erfolg des WWW zurückführen?": {
        "a": "Das WWW wurde für eine benutzerfreundliche Möglichkeit entwickelt, einfach an Informationen zu kommen. Außerdem kann durch offene Standards jeder Webseiten erstellen.",
        "b": "Das WWW basiert auf proprietären Standards, die nur von wenigen genutzt werden können.",
        "c": "Das WWW wurde entwickelt, um nur Textinformationen zu übertragen.",
        "correct": "a"
    },
    "Was versteht man unter dem Request-Response-Schema?": {
        "a": "Der Server stellt eine Anfrage (Request) an den Client und der Client antwortet (Response).",
        "b": "Als Client stellt man eine Anfrage (Request) an einen Server, der einem Informationen liefern soll. Diese Anfrage enthält meist Details, was für Informationen verlangt werden (z.B GET/POST-Methoden). Darauf sendet der Server eine Antwort (Response), ob die Informationen erfolgreich überbracht wurden. Diese werden in Statuscodes an den Client überbracht.",
        "c": "Request-Response-Schema beschreibt den Austausch von Dateien zwischen zwei Servern.",
        "correct": "b"
    },
    "Worauf war die ursprüngliche Version von HTTP ausgerichtet?": {
        "a": "Auf die Übertragung von Bildern.",
        "b": "Auf die Übertragung von Hypertextdokumenten zwischen Server und Client.",
        "c": "Auf die Übertragung von Audio und Video.",
        "correct": "b"
    },
    "Wie können seit HTTP 1.1 in beide Richtungen mehr Informationen übergeben werden?": {
        "a": "Durch die Einführung von verschlüsselten Verbindungen.",
        "b": "Durch die Einführung von Headern und Cookies.",
        "c": "Durch die Verwendung von XML.",
        "correct": "b"
    },
    "Was bringt die Möglichkeit persistenter Verbindungen?": {
        "a": "Erhöhte Wartezeiten und Ressourcenverbrauch.",
        "b": "Die Notwendigkeit, für jede Anfrage eine neue Verbindung aufzubauen.",
        "c": "Sparung von Wartezeiten und effizientere Nutzung von Ressourcen.",
        "correct": "c"
    },
    "Beschreiben Sie den Ablauf einer HTTP-Verbindung (textuell oder grafisch)": {
        "a": "Der Server sendet eine Anfrage an den Client, der Client antwortet, und die Verbindung wird geschlossen.",
        "b": "Der Client öffnet eine TCP-Verbindung zum Server, stellt eine HTTP-Anfrage, der Server antwortet mit einem Statuscode und der Inhalt wird gerendert. Bei persistenten Verbindungen bleibt die Verbindung bestehen.",
        "c": "Der Client stellt eine Anfrage an den DNS-Server, der die IP-Adresse des Webservers liefert.",
        "correct": "b"
    },
    "Was bewirkt eine HTTP-Methode ohne Angabe eines Ziels?": {
        "a": "Die Anfrage ist erfolgreich, aber es wird keine Antwort gesendet.",
        "b": "Die HTTP-Anfrage ist unvollständig und führt zu einem fehlerhaften Request.",
        "c": "Der Server führt eine Standardaktion aus.",
        "correct": "b"
    },
    "Erklären Sie den Begriff Status-Code im Zusammenhang mit dem HTTP-Response.": {
        "a": "Status-Codes geben den Erfolg oder Misserfolg einer Anfrage an und werden in 5 Klassen unterteilt: 1xx, 2xx, 3xx, 4xx, 5xx.",
        "b": "Status-Codes sind nur bei Fehlermeldungen relevant.",
        "c": "Status-Codes werden verwendet, um die Geschwindigkeit einer Anfrage zu messen.",
        "correct": "a"
    },
    "Was versteht man unter einer Reason-Phrase im HTTP-Response?": {
        "a": "Eine Reason-Phrase ist ein numerischer Code, der den Erfolg einer Anfrage anzeigt.",
        "b": "Die Reason-Phrase beschreibt kurz, für was der jeweilige Statuscode steht.",
        "c": "Eine Reason-Phrase ist ein spezieller Header in HTTP-Anfragen.",
        "correct": "b"
    },
    "Was versteht man unter einer HTTP-Methode?": {
        "a": "Eine HTTP-Methode beschreibt, welche Aktion der Client versucht, auszuführen, wie GET oder POST.",
        "b": "Eine HTTP-Methode ist ein Sicherheitsprotokoll für Webanfragen.",
        "c": "Eine HTTP-Methode ist ein Netzwerkprotokoll für den Datenaustausch.",
        "correct": "a"
    },
    "Für was wird die HTTP-GET-Methode verwendet?": {
        "a": "Um Daten zum Server zu senden und neue Ressourcen zu erstellen.",
        "b": "Um Daten einer Ressource anzufordern.",
        "c": "Um eine bestehende Ressource zu löschen.",
        "correct": "b"
    },
    "Für was wird die HTTP-POST-Methode verwendet?": {
        "a": "Um Daten einer Ressource anzufordern.",
        "b": "Um eine bestehende Ressource zu löschen.",
        "c": "Um Daten zum Server zu senden und neue Ressourcen zu erstellen.",
        "correct": "c"
    },

    # HTML Teil 1 Fragen
    "Nennen Sie mind. 3 Themenbereiche für eine Webseite:": {
        "a": "E-Commerce, Information, Unternehmen",
        "b": "Sport, Freizeit, Mode",
        "c": "Reisen, Musik, Kunst",
        "correct": "a"
    },
    "Wie könnte man eine Webseite zum Geld verdienen nutzen?": {
        "a": "Durch Platzieren von Anzeigen und Affiliate-Links.",
        "b": "Durch das Vermeiden von Werbung.",
        "c": "Durch das kostenlose Anbieten aller Inhalte.",
        "correct": "a"
    },
    "Wie werden HTML-Tags geschrieben, was beschreibt ein HTML-Tag?": {
        "a": "Ein HTML-Tag enthält einen Tagnamen innerhalb von runden Klammern (()), der Inhalt des Tags steht zwischen einem Öffnungstag (tag) und einem Schließtag (/tag).",
        "b": "Ein HTML-Tag enthält einen Tagnamen innerhalb von eckigen Klammern ([]), der Inhalt des Tags steht zwischen einem Öffnungstag ([tag]) und einem Schließtag ([/tag]).",
        "c": "Ein HTML-Tag enthält einen Tagnamen innerhalb von spitzen Klammern (<>), der Inhalt des Tags steht zwischen einem Öffnungstag (<tag>) und einem Schließtag (</tag>).",
        "correct": "c"
    },
    "Was ist die Hauptaufgabe des Browsers?": {
        "a": "Die Webseiteninhalte korrekt darzustellen.",
        "b": "Die Webseiteninhalte zu blockieren.",
        "c": "Die Webseiteninhalte zu speichern.",
        "correct": "a"
    },
    "Was versteht man im Zusammenhang mit Browsern unter 'Rendering'?": {
        "a": "Das Blockieren von Werbung auf Webseiten.",
        "b": "Das Interpretieren von HTML-/CSS-/JavaScript-Code und die darauffolgende Darstellung der Inhalte vom Webserver.",
        "c": "Das Speichern von Webseiteninhalten auf dem Server.",
        "correct": "b"
    },
    "Wodurch entstehen geräteabhängige Unterschiede bei der Anzeige von Webseiten?": {
        "a": "Durch unterschiedliche Bildschirmauflösungen/-größen, Browserkompatibilität und Betriebssysteme.",
        "b": "Durch die Internetgeschwindigkeit des Nutzers.",
        "c": "Durch die Farbeinstellungen des Monitors.",
        "correct": "a"
    },
    "Wodurch entstehen herstellerabhängige Unterschiede bei der Anzeige von Webseiten?": {
        "a": "Durch verschiedene Browser-Engines, Webstandards oder neuwertige Funktionen, die nicht jeder Browser unterstützt.",
        "b": "Durch die Internetgeschwindigkeit des Nutzers.",
        "c": "Durch die Farbeinstellungen des Monitors.",
        "correct": "a"
    },
    "Welche Unterschiede können durch unterschiedliche Betriebssysteme erfolgen?": {
        "a": "Durch die Farbgebung der Benutzeroberfläche.",
        "b": "Durch die Art, wie Schriftarten gerendert werden oder ob sie vorhanden sind, sowie verschiedene UI-Stile und Dateisysteme.",
        "c": "Durch die Bildschirmauflösung.",
        "correct": "b"
    },
    "Welche Vorteile entstehen durch die Nutzung von HTML und CSS?": {
        "a": "HTML und CSS verbessern die Ladezeit von Webseiten drastisch.",
        "b": "HTML und CSS garantieren Konsistenz von Regeln und Anpassungsfähigkeit. Getrennte CSS-Inhalte machen den Code lesbarer und verbessern die Suchmaschinenoptimierung.",
        "c": "HTML und CSS verhindern, dass Webseiten gehackt werden.",
        "correct": "b"
    },

    # HTML Teil 2 Fragen
    "Was versteht man in der Web-Entwicklung unter mobile-first?": {
        "a": "Ansatz der Web-Entwicklung, bei dem das Design und die Entwicklung einer Website oder Anwendung zuerst für Desktop-Computer optimiert werden.",
        "b": "Ansatz der Web-Entwicklung, bei dem das Design und die Entwicklung einer Website oder Anwendung zuerst für mobile Endgeräte optimiert werden.",
        "c": "Ansatz der Web-Entwicklung, bei dem das Design und die Entwicklung einer Website oder Anwendung gleichzeitig für alle Gerätetypen optimiert werden.",
        "correct": "b"
    },
    "Was ist die Stärke von Flexbox in CSS?": {
        "a": "Flexbox kann komplexe Layouts auf einfache und flexible Weise erstellen. Vorteile sind zudem Responsive Design, das leichte Anordnen von Elementen und die Verteilung von Platz zwischen und innerhalb von Elementen.",
        "b": "Flexbox ist speziell für die Gestaltung von Tabellen gedacht.",
        "c": "Flexbox ist hauptsächlich für die Gestaltung von Formularen nützlich.",
        "correct": "a"
    },
    "Welche Arten von 'Links' gibt es?": {
        "a": "Text-Link, Bild-Link, Video-Link, Audio-Link",
        "b": "Text-Link, Bild-Link, E-Mail-Link, Telefonnummer-Link, Verweis auf ein Dokument, Verweis auf eine externe Webseite",
        "c": "Text-Link, Dokument-Link, Script-Link, PDF-Link",
        "correct": "b"
    },
    "Nennen Sie ein Argument warum verbundene Zellen innerhalb einer HTML-Table vermeiden soll?": {
        "a": "Verbundene Zellen machen die Tabelle hübscher.",
        "b": "Verbundene Zellen können die Struktur der Daten verzerren und die Zugänglichkeit beeinträchtigen, z.B bei Screenreadern.",
        "c": "Verbundene Zellen verbessern die Ladezeit der Tabelle.",
        "correct": "b"
    },
    "Wie sind HTML-Tabellen aufgebaut?": {
        "a": "<table>-Tag am Anfang, <tr>-Tag (Table Row) für Tabellenzeile, <td>-Tag (Table Data) für Inhalt der Zelle, <th> (Table Header) für Überschriften. Wahlweise mit <thead>, <tbody> und <tfoot> ergänzen.",
        "b": "<table>-Tag am Anfang, <row>-Tag für Tabellenzeile, <cell>-Tag für Inhalt der Zelle, <header> für Überschriften.",
        "c": "<table>-Tag am Anfang, <line>-Tag für Tabellenzeile, <data>-Tag für Inhalt der Zelle, <head> für Überschriften.",
        "correct": "a"
    },
    "Was ist der Unterschied zwischen einer 'id' und einer 'class'. Wie würde der CSS-Selektor für class='ziel' bzw. id='ziel' aussehen?": {
        "a": "Die 'id' ist ein eindeutiger Bezeichner für ein bestimmtes Element, während 'class' eine Gruppe von Elementen kennzeichnet. CSS-Selektor für id='ziel': .ziel, für class='ziel': #ziel.",
        "b": "Die 'id' ist ein Bezeichner für eine Gruppe von Elementen, während 'class' ein eindeutiger Bezeichner für ein bestimmtes Element ist. CSS-Selektor für id='ziel': #ziel, für class='ziel': .ziel.",
        "c": "Die 'id' ist ein eindeutiger Bezeichner für ein bestimmtes Element, während 'class' eine Gruppe von Elementen kennzeichnet. CSS-Selektor für id='ziel': #ziel, für class='ziel': .ziel.",
        "correct": "c"
    },
    "Nennen Bildformate mit verlustbehafteter Kompression? Welcher Vorteil wird welchem Nachteil bei Kompression entgegengestellt?": {
        "a": "JPEG, PNG, SVG: Vorteil: bessere Farbtreue, Nachteil: größere Dateigröße.",
        "b": "JPEG, WebP, GIF: Vorteil: Dateigröße wird erheblich reduziert, Nachteil: Qualitätsverlust im Bild, bei starken Kompressionsraten Unschärfen.",
        "c": "JPEG, BMP, TIFF: Vorteil: höhere Auflösung, Nachteil: längere Ladezeiten.",
        "correct": "b"
    },
    "Erklären Sie den Begriff Status-Code im Zusammenhang mit dem HTTP-Response.": {
        "a": "Der Status-Code beschreibt eine numerische Kennzeichnung, die den Zustand einer Anfrage an den Server widerspiegelt. Die erste Ziffer des Status-Codes gibt die allgemeine Kategorie des Status an: 1xx: Informational, 2xx: Success, 3xx: Redirection, 4xx: Client Error, 5xx: Server Error.",
        "b": "Der Status-Code beschreibt die Geschwindigkeit einer Anfrage an den Server.",
        "c": "Der Status-Code gibt an, welche Datei auf dem Server angefragt wurde.",
        "correct": "a"
    },
    "Was versteht man bei Bildern unter Transparenz? Bei welchen Bildformaten ist dies möglich?": {
        "a": "Transparenz bezieht sich darauf, dass es einen transparenten Hintergrund gibt, sodass der darunterliegende Inhalt sichtbar ist. Transparenz ist bei PNG, GIF, SVG und WebP möglich.",
        "b": "Transparenz bezieht sich auf die Fähigkeit eines Bildes, ohne Qualitätsverlust zu komprimieren. Transparenz ist bei JPEG, BMP und TIFF möglich.",
        "c": "Transparenz bezieht sich auf die Möglichkeit, ein Bild in verschiedenen Farbtiefen darzustellen. Transparenz ist bei BMP, TIFF und RAW möglich.",
        "correct": "a"
    },
}
questions3ADAC_INF = {
    "Welche wichtigen Gründe führten zur Entwicklung von Datenbanksystemen?": {
        "a": "Speicherung von Daten auf Papier",
        "b": "Vereinfachung der Hardwarekonfiguration",
        "c": "Verwaltung von großen Datenmengen und Reduzierung von Redundanzen",
        "correct": "c"
    },
    "Was sind Redundanzen in Datenbanken?": {
        "a": "Wiederholte Daten, die mehrfach ohne Notwendigkeit gespeichert sind",
        "b": "Eindeutige Daten, die nur einmal gespeichert sind",
        "c": "Daten, die immer auf die gleiche Weise abgefragt werden",
        "correct": "a"
    },
    "Was sind Inkonsistenzen in Datenbanken?": {
        "a": "Daten, die immer korrekt sind",
        "b": "Widersprüchliche oder unvollständige Daten",
        "c": "Eindeutige und konsistente Datenbeziehungen",
        "correct": "b"
    },
    "Was ist ein Mehrnutzerbetrieb in Datenbanken?": {
        "a": "Das Speichern von Daten auf einem einzelnen Rechner",
        "b": "Das gleichzeitige Arbeiten mehrerer Nutzer an der Datenbank",
        "c": "Das Arbeiten mit einer einzigen Benutzeroberfläche",
        "correct": "b"
    },
    "Welche Probleme können im Mehrnutzerbetrieb auftreten?": {
        "a": "Vollständige Datenkonsistenz",
        "b": "Keine Fehler bei Datenbankoperationen",
        "c": "Datenkonflikte und Zugriffsprobleme",
        "correct": "c"
    },
    "Was ist ein Datenbankmanagementsystem (DBMS)?": {
        "a": "Ein Netzwerk zur Verbindung von Datenbanken",
        "b": "Ein System zur physikalischen Speicherung von Daten",
        "c": "Ein Softwarepaket, das die Verwaltung der Datenbank und den Zugriff auf Daten regelt",
        "correct": "c"
    },
    "Welche Aufgaben hat ein DBMS?": {
        "a": "Stellt nur den Zugriff auf Daten zur Verfügung",
        "b": "Verarbeitet nur Datenbankabfragen",
        "c": "Stellt Daten zur Verfügung, gewährleistet Datenintegrität und Datensicherung",
        "correct": "c"
    },
    "Was ist ein Data Dictionary?": {
        "a": "Ein physisches Speichermedium für Daten",
        "b": "Ein Werkzeug zur Überwachung von Datenbankabfragen",
        "c": "Ein Datenlexikon, das Informationen über Datenbankobjekte speichert",
        "correct": "c"
    },
    "Welche Datenbankmodelle kennen Sie?": {
        "a": "Nur hierarchische und Netzwerk-Datenbanken",
        "b": "Nur relationale Datenbanken",
        "c": "Hierarchische, Netzwerk-, Relationale-, Spaltenorientierte-, Dokumentorientierte-, Objektorientierte- und NoSQL-Datenbanken",
        "correct": "c"
    },
    "Was ist das hierarchische Datenbankmodell?": {
        "a": "Daten werden in einer baumartigen Struktur mit eindeutigen Eltern-Kind-Beziehungen gespeichert",
        "b": "Daten werden als Objekte mit Attributen und Methoden gespeichert",
        "c": "Daten werden in einer flachen Struktur ohne Beziehungen gespeichert",
        "correct": "a"
    },
    "Was ist das relationale Datenbankmodell?": {
        "a": "Daten werden in einer baumartigen Struktur organisiert",
        "b": "Daten werden als Objekte mit Attributen und Methoden gespeichert",
        "c": "Daten werden in Tabellen gespeichert und durch Primär- und Fremdschlüssel miteinander verknüpft",
        "correct": "c"
    },
    "Welche physischen Datenbankarchitekturen gibt es?": {
        "a": "Nur zentralisierte DBS",
        "b": "Zentralisierte DBS, Verteilte DBS, Client-Server DBS, Parallele DBS",
        "c": "Nur verteilte und parallele DBS",
        "correct": "b"
    },
    "Was ist eine zentrale Datenbankarchitektur?": {
        "a": "Datenbanken sind auf mehreren geografisch entfernten Servern verteilt",
        "b": "Das gesamte DBMS und die Anwendungen sind auf einem einzelnen Rechner gespeichert",
        "c": "Daten werden auf mehreren Prozessoren gleichzeitig verarbeitet",
        "correct": "b"
    },
    "Was ist das Client-Server-Modell in Datenbanken?": {
        "a": "Ein Modell, bei dem alle Daten auf einem zentralen Server gespeichert werden",
        "b": "Ein System, bei dem zwei unabhängige Prozesse über eine Schnittstelle miteinander kommunizieren",
        "c": "Ein Modell, das mehrere physische Speicherorte für Daten nutzt",
        "correct": "b"
    },
    "Was ist eine Relation bzw. Was beschreibt Sie? Führen Sie drei Eigenschaften an.": {
        "a": "Eine Menge von Tupeln in Form einer Tabelle mit Spalten und Zeilen. Eigenschaften: Eindeutiger Name, mehrere Attribute, Primärschlüssel.",
        "b": "Eine Sammlung von Tabellen mit unterschiedlichen Datentypen und Formaten.",
        "c": "Eine Reihe von Spalten, die miteinander verknüpft sind.",
        "correct": "a"
    },
    "Was versteht man unter funktionaler Abhängigkeit? (mit eigenen Worten)": {
        "a": "Es gibt eine Beziehung, in der sich bestimmte Daten aufgrund eines anderen Wertes ändern.",
        "b": "Eine funktionale Abhängigkeit beschreibt, wie sich Datensätze im Laufe der Zeit verändern.",
        "c": "Die Funktionale Abhängigkeit besagt, dass ein Wert X immer einen anderen Wert Y beeinflusst, der sich nicht ändern kann.",
        "correct": "c"
    },
    "Was versteht man unter transitiver Abhängigkeit?": {
        "a": "Attribute sind in einer Kette zwischen anderen Attributen voneinander abhängig.",
        "b": "Es gibt eine direkte Beziehung zwischen Attributen, ohne Zwischenwerte.",
        "c": "Ein Attribut ist von einem anderen Attribut direkt abhängig, ohne Zwischenstationen.",
        "correct": "a"
    },
    "Was sind die Ziele der Normalisierung? Mind. 3.": {
        "a": "Verhindert Datenredundanz, Verhindert Dateninkonsistenz, Stellt eine einfache Datensicherung sicher.",
        "b": "Verhindert Redundanzen, Gewährleistet die Vollständigkeit der Datenbank, Macht Daten schwer zugänglich.",
        "c": "Verhindert Datenredundanz, Verhindert Dateninkonsistenz, Sicherheit bei Einfügen, Löschen oder Ändern von Datensätzen.",
        "correct": "c"
    },
    "Beschreiben Sie die 1:1 Beziehung und führen Sie ein Beispiel an:": {
        "a": "Ein Tupel aus einer Relation ist genau einem Tupel aus einer anderen Relation zugeordnet.",
        "b": "Ein Tupel aus einer Relation kann mehreren Tupeln aus einer anderen Relation zugeordnet sein.",
        "c": "Ein Tupel ist in keiner Weise mit anderen Tupeln verknüpft.",
        "correct": "a"
    },
    "Beschreiben Sie die 1:n Beziehung": {
        "a": "Jede Entität einer Entitätsmenge ist einer oder mehreren Entitäten einer anderen Entitätsmenge zugeordnet.",
        "b": "Jede Entität ist nur mit genau einer anderen Entität einer anderen Menge verbunden.",
        "c": "Jede Entität ist mit mehreren Entitäten aus der gleichen Entitätsmenge verbunden.",
        "correct": "a"
    },
    "Was ist ein Primärschlüssel?": {
        "a": "Ein Primärschlüssel ist ein eindeutiger Identifikator für eine Entität einer Entitätsmenge, dessen Wert nur einmal vorkommen kann.",
        "b": "Ein Primärschlüssel ist ein allgemeiner Identifikator, der nicht unbedingt eindeutig ist.",
        "c": "Ein Primärschlüssel ist ein sekundärer Schlüssel, der von anderen Tabellen referenziert wird.",
        "correct": "a"
    },
    "Was ist ein Fremdschlüssel?": {
        "a": "Ein Fremdschlüssel ist der Identifikator einer Fremd-Relation, der in der aktuellen Relation eingebunden wird, um eine Beziehung einzugehen.",
        "b": "Ein Fremdschlüssel ist ein Wert, der nur für die interne Nutzung innerhalb einer Tabelle verwendet wird.",
        "c": "Ein Fremdschlüssel ist ein genereller Schlüssel, der alle Daten einer Tabelle referenziert.",
        "correct": "a"
    },
    "Was versteht man unter NULL-Werten oder leeren Einträgen?": {
        "a": "NULL-Werte beschreiben die Abwesenheit von Werten, während leere Einträge mit einem Standardwert versehen sind.",
        "b": "Leere Einträge sind Werte, die vollständig fehlen, NULL-Werte sind Standardwerte.",
        "c": "NULL-Werte und leere Einträge sind dasselbe und können ohne Unterschied verwendet werden.",
        "correct": "a"
    },
    "Was ist eine Lösch-Anomalie?": {
        "a": "Wenn beim Löschen eines Datensatzes abhängige Datensätze mitgelöscht werden, ohne dass diese gesichert sind.",
        "b": "Wenn durch das Löschen eines Datensatzes alle Referenzen zu diesem Datensatz entfernt werden.",
        "c": "Wenn ein Datensatz durch ein Löschverfahren korrigiert wird.",
        "correct": "a"
    },
    "Wann befindet sich eine Relation in der 1. Normalform?": {
        "a": "Eine Relation befindet sich in der ersten Normalform, wenn jedes Attribut atomar ist und nur ein Wert pro Tupel erlaubt ist.",
        "b": "Eine Relation ist in der ersten Normalform, wenn alle Werte in einer Tabelle einmalig sind.",
        "c": "Eine Relation in der ersten Normalform erfordert keine Attribute mit mehreren Werten.",
        "correct": "a"
    },
    "Wann befindet sich eine Relation in der 2. Normalform?": {
        "a": "Wenn die 1. Normalform erfüllt ist und jedes Nicht-Schlüsselfeld vom Primärschlüssel abhängt.",
        "b": "Wenn die Relation keine redundanten Daten enthält.",
        "c": "Wenn jedes Attribut einer Tabelle atomar ist und keine transitiven Abhängigkeiten vorhanden sind.",
        "correct": "a"
    }
}